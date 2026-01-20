# /// script
# dependencies = ["torch", "transformers"]
# ///
import argparse
import shlex
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

parser = argparse.ArgumentParser(
    description="Qwen REPL: tokens, next-token probs, attentions, generation."
)
parser.add_argument(
    "--base-model",
    default="Qwen/Qwen2.5-1.5B",
    help="Base model name or local path.",
)
parser.add_argument(
    "--chat-model",
    default="Qwen/Qwen2.5-1.5B-Instruct",
    help="Chat/instruct model name or local path.",
)
parser.add_argument(
    "--model",
    dest="base_model",
    help="Alias for --base-model.",
)
parser.add_argument("--top-k", type=int, default=5, help="Default top-k for `next`.")
parser.add_argument(
    "--max-new-tokens", type=int, default=30, help="Default tokens for `gen`."
)
parser.add_argument(
    "--attn-impl",
    choices=["auto", "eager", "sdpa", "flash_attention_2"],
    default="auto",
    help="Attention implementation. 'eager' is most compatible for attention maps.",
)
args = parser.parse_args()

base_model_name = args.base_model
chat_model_name = args.chat_model

use_mps = torch.backends.mps.is_available()
device = torch.device("mps" if use_mps else "cpu")
dtype = torch.float32

attn_impl = args.attn_impl
tokenizer = None
model = None
model_name = None

def load_model(name):
    global tokenizer, model, model_name
    model_name = name
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model_kwargs = {"dtype": dtype}
    if attn_impl != "auto":
        model_kwargs["attn_implementation"] = attn_impl
    model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
    model.to(device)
    if attn_impl != "auto":
        model.set_attn_implementation(attn_impl)
    model.eval()

load_model(base_model_name)

# Normalize whitespace for display (Qwen uses a mix of token markers).
def display_ws(text):
    return text.replace("\\", "\\\\").replace("\n", "\\n")

def quote_token(text):
    return f"\"{text}\""

def tok2str(i):
    if tokenizer.special_tokens_map and i in tokenizer.all_special_ids:
        return display_ws(tokenizer.convert_ids_to_tokens([i])[0])
    text = tokenizer.decode([i], clean_up_tokenization_spaces=False)
    return display_ws(text.replace("\r", ""))

def show_topk_next_token(outputs, k=5):
    logits = outputs.logits.float()[0, -1]
    probs = torch.softmax(logits, dim=-1)
    probs = torch.nan_to_num(probs, nan=0.0, posinf=0.0, neginf=0.0)
    top_probs, top_indices = torch.topk(probs, k)
    for prob, token in zip(top_probs, top_indices):
        print(f"{quote_token(tok2str(token)):>15s} : {prob*100:.2f}%")

def generate_with_cache(inputs, max_new_tokens=20, do_sample=False, temperature=1.0):
    generated = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]
    past_key_values = None

    for _ in range(max_new_tokens):
        with torch.no_grad():
            outputs = model(
                input_ids=generated if past_key_values is None else generated[:, -1:],
                attention_mask=attention_mask,
                use_cache=True,
                past_key_values=past_key_values,
            )
        past_key_values = outputs.past_key_values
        logits = outputs.logits[:, -1]
        if do_sample:
            logits = logits / max(temperature, 1e-6)
            probs = torch.softmax(logits, dim=-1)
            probs = torch.nan_to_num(probs, nan=0.0, posinf=0.0, neginf=0.0)
            next_token = torch.multinomial(probs, num_samples=1)
        else:
            next_token = torch.argmax(logits, dim=-1, keepdim=True)
        generated = torch.cat([generated, next_token], dim=-1)
        attention_mask = torch.cat(
            [attention_mask, torch.ones_like(next_token, device=attention_mask.device)],
            dim=-1,
        )
    return generated

def generate_with_cache_until(inputs, max_new_tokens, stop_ids):
    generated = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]
    past_key_values = None

    for _ in range(max_new_tokens):
        with torch.no_grad():
            outputs = model(
                input_ids=generated if past_key_values is None else generated[:, -1:],
                attention_mask=attention_mask,
                use_cache=True,
                past_key_values=past_key_values,
            )
        past_key_values = outputs.past_key_values
        logits = outputs.logits[:, -1]
        next_token = torch.argmax(logits, dim=-1, keepdim=True)
        generated = torch.cat([generated, next_token], dim=-1)
        attention_mask = torch.cat(
            [attention_mask, torch.ones_like(next_token, device=attention_mask.device)],
            dim=-1,
        )
        if stop_ids and int(next_token.item()) in stop_ids:
            break
    return generated

def apply_escapes(text):
    return text.replace("\\n", "\n")

def strip_wrapping_quotes(text):
    if len(text) >= 2 and text[0] == text[-1] and text[0] in ("'", '"'):
        return text[1:-1]
    return text

def parse_text_arg(raw):
    raw = raw.lstrip()
    if not raw:
        return ""
    parts = shlex.split(raw, posix=True)
    if not parts:
        return ""
    return apply_escapes(" ".join(parts))

def tokenize_text(text):
    inputs = tokenizer(text, return_tensors="pt")
    return {k: v.to(device) for k, v in inputs.items()}

def show_tokens(text):
    inputs = tokenize_text(text)
    tokens = [tok2str(i) for i in inputs["input_ids"][0]]
    entries = [f"{idx}:{quote_token(tok)}" for idx, tok in enumerate(tokens)]
    print("Tokens:", "[" + ", ".join(entries) + "]")

def format_token_list(token_ids):
    items = [quote_token(tok2str(i)) for i in token_ids]
    return "[" + ", ".join(items) + "]"

def show_next(text, k):
    inputs = tokenize_text(text)
    with torch.no_grad():
        outputs = model(**inputs, use_cache=False)
    print("Top next-token probabilities:")
    show_topk_next_token(outputs, k=k)

def ensure_attn_impl():
    global attn_impl
    if attn_impl == "auto":
        attn_impl = "eager"
        model.set_attn_implementation(attn_impl)

def format_cell(val):
    cell = int(round(val))
    if cell <= 0:
        return "  "
    if cell > 99:
        cell = 99
    return f"{cell}".rjust(2)

def show_attn(text, idx):
    ensure_attn_impl()
    inputs = tokenize_text(text)
    tokens = [tok2str(i) for i in inputs["input_ids"][0]]
    if idx < 0 or idx >= len(tokens):
        print("Index out of range. Use `tokens` to list indices.")
        return
    with torch.no_grad():
        outputs = model(**inputs, output_attentions=True, use_cache=False)
    if outputs.attentions is None:
        print("No attentions returned.")
        return
    layers = outputs.attentions
    cols = 28
    layer_count = min(cols, len(layers))
    attn_layers = [layers[i][0].mean(dim=0) for i in range(layer_count)]
    row_count = idx + 1
    labels = [f"{row_idx}:{quote_token(tokens[row_idx])}" for row_idx in range(row_count)]
    label_width = max(len(label) for label in labels) if labels else 0

    for row_idx in range(row_count):
        label = labels[row_idx].rjust(label_width)
        cells = []
        for col in range(cols):
            if col >= layer_count:
                cells.append("  ")
                continue
            val = attn_layers[col][idx, row_idx].item() * 100.0
            cells.append(format_cell(val))
        print(f"{label} " + " ".join(cells))

def show_pattern(text, layer_id):
    ensure_attn_impl()
    inputs = tokenize_text(text)
    tokens = [tok2str(i) for i in inputs["input_ids"][0]]
    with torch.no_grad():
        outputs = model(**inputs, output_attentions=True, use_cache=False)
    if outputs.attentions is None:
        print("No attentions returned.")
        return
    layers = outputs.attentions
    if layer_id < 0 or layer_id >= len(layers):
        print("Layer out of range.")
        return
    attn = layers[layer_id][0].mean(dim=0)
    labels = [f"{row_idx}:{quote_token(tokens[row_idx])}" for row_idx in range(len(tokens))]
    label_width = max(len(label) for label in labels) if labels else 0

    for row_idx in range(len(tokens)):
        label = labels[row_idx].rjust(label_width)
        cells = []
        for col in range(len(tokens)):
            val = attn[row_idx, col].item() * 100.0
            cells.append(format_cell(val))
        print(f"{label} " + " ".join(cells))

def show_gen(text, count):
    inputs = tokenize_text(text)
    base_len = inputs["input_ids"].shape[1]
    stop_ids = []
    if count is None:
        im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
        if im_end_id is not None and im_end_id != tokenizer.unk_token_id:
            stop_ids = [int(im_end_id)]
        elif tokenizer.eos_token_id is not None:
            stop_ids = [int(tokenizer.eos_token_id)]
        generated = generate_with_cache_until(
            inputs,
            max_new_tokens=args.max_new_tokens,
            stop_ids=stop_ids,
        )
    else:
        generated = generate_with_cache(inputs, max_new_tokens=count, do_sample=False)
    new_tokens = generated[0, base_len:]
    token_ids = [int(i) for i in new_tokens]
    if stop_ids and token_ids and token_ids[-1] in stop_ids:
        token_ids = token_ids[:-1]
    print("Generated:")
    if mode == "chat":
        text_out = tokenizer.decode(token_ids, clean_up_tokenization_spaces=False)
        print(text_out.replace("\r", ""))
    else:
        print(format_token_list(token_ids))
    return None

def show_variations(text, count, tokens_per=10):
    inputs = tokenize_text(text)
    base_len = inputs["input_ids"].shape[1]
    for idx in range(count):
        generated = generate_with_cache(
            inputs,
            max_new_tokens=tokens_per,
            do_sample=True,
            temperature=1.0,
        )
        new_tokens = generated[0, base_len:]
        print(f"{idx + 1}: {format_token_list([int(i) for i in new_tokens])}")

def print_help():
    print("Commands:")
    print('  load "text ..."   Replace the context.')
    print('  add "text ..."    Append to the context.')
    print("  status           Show current model, mode, and context.")
    print("  model <chat|base> Set mode and load the matching model.")
    print("  msg <role> <text> Add a message (roles: system/user/assistant).")
    print("  msg add <text>    Append to the last message.")
    print("  msg clear         Clear all messages.")
    print("  template         Show the tokenizer's chat template.")
    print("  messages         Show current message list.")
    print("  tokens           Show tokens with indices.")
    print("  next [k]          Show top-k next-token probabilities.")
    print("  attn <idx>        Per-layer attention (28 cols) for each row j to column idx.")
    print("  pattern <layer>   NxN attention for a layer (avg heads).")
    print("  gen [count]       Generate tokens (greedy, default: until <|im_end|>).")
    print("  variations <n>    N sampled completions (10 tokens each).")
    print("  help             Show this help.")
    print("  quit/exit         Leave the REPL.")

context = ""
messages = []
mode = "base"

def get_effective_messages():
    if messages:
        return messages, False
    if context:
        return [{"role": "user", "content": context}], True
    return [], False

def get_current_context():
    if mode == "chat":
        msg_list, _ = get_effective_messages()
        if not msg_list:
            return ""
        return tokenizer.apply_chat_template(
            msg_list,
            tokenize=False,
            add_generation_prompt=True,
        )
    return context

def show_messages():
    msg_list, synthetic = get_effective_messages()
    if not msg_list:
        print("No messages.")
        return
    if synthetic:
        print("Messages (synthetic from context):")
    else:
        print("Messages:")
    for idx, msg in enumerate(msg_list):
        role = msg.get("role", "unknown")
        content = display_ws(msg.get("content", ""))
        print(f"{idx}: {role}: {content}")

def count_base_tokens(text):
    if not text:
        return 0
    return len(tokenizer(text, add_special_tokens=False)["input_ids"])

def build_status_line():
    if mode == "chat":
        msg_list, _ = get_effective_messages()
        msg_count = len(msg_list)
        return f"LLM REPL (chat mode, {model_name}, {msg_count} message context)"
    token_count = count_base_tokens(context)
    return f"LLM REPL (base mode, {model_name}, {token_count} token context)"

def show_status():
    current = get_current_context()
    print(build_status_line())
    if current:
        print("Context:")
        print(current)

print(build_status_line())
print("Type `help` for commands.")
while True:
    try:
        raw = input(">> ")
    except EOFError:
        break
    if not raw.strip():
        continue

    lower = raw.strip().lower()
    if lower in ("quit", "exit"):
        break
    if lower == "help":
        print_help()
        continue
    if lower == "status":
        show_status()
        continue
    if lower == "messages":
        show_messages()
        continue
    if lower == "template":
        if mode != "chat":
            print("Chat template is only available in chat mode. Use `model chat`.")
            continue
        if tokenizer.chat_template is None:
            print("No chat template available.")
        else:
            print(tokenizer.chat_template)
        continue

    if lower == "load" or lower.startswith("load "):
        text = parse_text_arg(raw[len("load"):])
        if not text and raw.strip().lower() == "load":
            print('Usage: load "text ..."')
            continue
        context = text
        print("Context loaded.")
        continue

    if lower == "add" or lower.startswith("add "):
        text = parse_text_arg(raw[len("add"):])
        if not text and raw.strip().lower() == "add":
            print('Usage: add "text ..."')
            continue
        if context and text and not context[-1].isspace() and not text[0].isspace():
            context += " "
        context += text
        print("Context updated.")
        continue

    parts = raw.strip().split(maxsplit=1)
    cmd = parts[0].lower()
    arg = parts[1] if len(parts) > 1 else ""

    if cmd == "model":
        if not arg:
            print("Usage: model <chat|base>")
            continue
        if arg not in ("chat", "base"):
            print("Usage: model <chat|base>")
            continue
        mode = arg
        target_model = chat_model_name if mode == "chat" else base_model_name
        if model_name != target_model:
            load_model(target_model)
        context = ""
        messages = []
        print(f"Mode set to {mode}. Active model: {model_name}. Context cleared.")
        continue
    if cmd == "msg":
        if not arg:
            print("Usage: msg <system|user|assistant> <text> | msg add <text>")
            continue
        subparts = arg.split(maxsplit=1)
        subcmd = subparts[0].lower()
        rest = subparts[1] if len(subparts) > 1 else ""
        if subcmd in ("system", "user", "assistant"):
            text = parse_text_arg(rest)
            messages.append({"role": subcmd, "content": text})
            print(f"Message added: {subcmd}.")
            continue
        if subcmd == "add":
            if not messages:
                print("No messages to add to.")
                continue
            text = parse_text_arg(rest)
            messages[-1]["content"] = messages[-1].get("content", "") + text
            print("Message updated.")
            continue
        if subcmd == "clear":
            messages = []
            print("Messages cleared.")
            continue
        print("Usage: msg <system|user|assistant> <text> | msg add <text>")
        continue

    if cmd == "tokens":
        current = get_current_context()
        if current == "":
            if mode == "chat":
                print("No messages available for chat mode.")
            else:
                print("No context loaded. Use `load` or `add`.")
            continue
        show_tokens(current)
        continue
    if cmd == "next":
        current = get_current_context()
        if current == "":
            if mode == "chat":
                print("No messages available for chat mode.")
            else:
                print("No context loaded. Use `load` or `add`.")
            continue
        k = args.top_k
        if arg:
            if arg.isdigit():
                k = int(arg)
            else:
                print("Usage: next [k]")
                continue
        show_next(current, k=k)
        continue
    if cmd == "attn":
        current = get_current_context()
        if current == "":
            if mode == "chat":
                print("No messages available for chat mode.")
            else:
                print("No context loaded. Use `load` or `add`.")
            continue
        if not arg:
            print("Usage: attn <idx>")
            continue
        if not arg.isdigit():
            print("Usage: attn <idx>")
            continue
        show_attn(current, int(arg))
        continue
    if cmd == "pattern":
        current = get_current_context()
        if current == "":
            if mode == "chat":
                print("No messages available for chat mode.")
            else:
                print("No context loaded. Use `load` or `add`.")
            continue
        if not arg:
            print("Usage: pattern <layer>")
            continue
        if not arg.isdigit():
            print("Usage: pattern <layer>")
            continue
        show_pattern(current, int(arg))
        continue
    if cmd == "gen":
        current = get_current_context()
        if current == "":
            if mode == "chat":
                print("No messages available for chat mode.")
            else:
                print("No context loaded. Use `load` or `add`.")
            continue
        if not arg:
            show_gen(current, None)
            continue
        if not arg.isdigit():
            print("Usage: gen [count]")
            continue
        show_gen(current, int(arg))
        continue
    if cmd == "variations":
        current = get_current_context()
        if current == "":
            if mode == "chat":
                print("No messages available for chat mode.")
            else:
                print("No context loaded. Use `load` or `add`.")
            continue
        if not arg:
            print("Usage: variations <n>")
            continue
        if not arg.isdigit():
            print("Usage: variations <n>")
            continue
        count = int(arg)
        show_variations(current, count, tokens_per=10)
        continue

    print("Unknown command. Type `help` for commands.")
