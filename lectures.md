Lectures for CS 3960 Vibe Coding
================================

| Week   | Monday | Wednesday | Friday          |
|--------|--------|-----------|-----------------|
| Jan  5 | 00     | A1        | release notes 1 |
| Jan 12 | B1     | A2        | release notes 2 |
| Jan 19 | ------ | *Demo*    | HW1             |
| Jan 26 | B2     | A3        |                 |
| Feb  2 | B3     | A4        |                 |
| Feb  9 | *Demo* | C1        | HW2             |
| Feb 16 | ------ | D1        |                 |
| Feb 23 | C2     | D2        |                 |
| Mar  2 | *Demo* | D3        | HW3             |
| Mar  9 | C3     | D4        |                 |
| Mar 16 | ------ | ------    | ------          |
| Mar 23 | C4     | D5        |                 |
| Mar 30 | C5     | *Demo*    | HW4             |
| Apr  6 | E1     | E2        |                 |
| Apr 13 | E3     | E4        | HW5             |
| Apr 20 | *Demo* | ------    | ------          |

Lecture 00, *Introduction*

+ Reading: [AI Can Write Your Code. It Can’t Do Your Job.](https://terriblesoftware.org/2025/12/11/ai-can-write-your-code-it-cant-do-your-job/)
+ Activity: [Install Amp](https://ampcode.com/);
  create a native Qt-based text editor
  
Lecture A1, *Software Engineering*
+ Reading: none
+ Activity: discussion

Lecture B1, *Next-token Prediction*

+ Reading: [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)
+ Demo: [llm-repl.py](llm-repl.py) \
  If you [install `uv`](https://docs.astral.sh/uv/getting-started/installation/)
  you can download this script and run it with `uv run llm-repl.py`.
  It'll take a long time to start (it needs to download a large model)
  but once it does you'll see `>>` and you can type `help` to see
  the list of available commands. We used this in class to show how
  next-token prediction is used to generate text.
+ Activity: train a 2-word Markov chain on [Alice's Adventures in
  Wonderland](https://www.gutenberg.org/cache/epub/11/pg11.txt).
  Implement a next-word predictor similar to the professor's. Try
  completing various (in-genre) sentences.
+ Optional reading: [A Mathematical Theory of
  Communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf) \
  This 1948 monograph by Claude Shannon invented information theory,
  and notably focused on language modeling as its example. Page 5
  introduces the basic idea of language modeling from tokens, and
  pages 6-7 introduce Markov chain models (as in our activity; Shannon
  spells it Markoff) for English. Most of the rest is math.
+ Optional reading: [Attention is All You
  Need](https://arxiv.org/pdf/1706.03762) \
  This 2017 paper (known by its title) introduced the "attention"
  mechanism and used it to do language modeling (specifically for
  translation). It might be the most important AI paper ever written.
  Section 3.2.1 gives the math behind attention. Section 5.1 (short)
  describes their (tiny by modern standards) training corpus.
+ Optional reading: [Training Compute-Optimal
  LLMs](https://arxiv.org/pdf/2203.15556) \
  This 2022 paper (known as "Chinchilla") identifies "scaling laws"
  whereby larger models trained on more tokens have better quality

Lecture A2, *Testing*

+ Reading: [Your job is to deliver code you have proven to work](https://simonwillison.net/2025/Dec/18/code-proven-to-work/)
+ Activity: 

Lecture B2, *Fine-tuning*

+ Reading: Section 1.1 of [Scaling Laws for Neural Language
  Models](https://arxiv.org/pdf/2001.08361) \
  This 2020 paper from OpenAI shows that LLMs get consistently better
  as you scale them up; this idea is sometimes called the "Scaling
  Hypothesis". Four of the authors (Dario, Sam, Tom B., and Jared)
  would go on to found Anthropic.
+ Optional reading: [Will scaling
  work?](https://www.dwarkesh.com/p/will-scaling-work) \
  This 2023 blog post asks whether LLMs can be scaled to human-level
  results, answering "yes". It's a good summary of the state of the
  discourse at the end of 2024, right before we started seeing clear
  human-level performance from LLMs.
+ Optional reading: [Dolma: An Open Corpus of 3 Trillion Tokens
for Language Model Pretraining
Research](https://allenai.github.io/dolma/docs/assets/dolma-v0_1-20230819.pdf)
\
  This 2024 technical report describes Dolma dataset, including where
  the data was gathered, how it was deduplicated and preprocessed, and
  how it can be used for neural network training.
+ Optional reading: [Prediction and Entropy of Printed
  English](https://www.princeton.edu/~wbialek/rome/refs/shannon_51.pdf) \
  This 1950 manuscript by Claude Shannon described his experiments
  measuring how well humans do at language modeling. Modern LLMs are
  trained using strikingly similar methods (and do as well or better
  than humans).
+ Optional reading: [The Scaling
  Hypothesis](https://gwern.net/scaling-hypothesis#scaling) \
  This 2020 blog post, written right after the release of GPT-3,
  points out that scaling LLMs and training them on more data
  consistently produces new capabilities, and argues that nothing
  besides scale is actually needed to achieve human-level capability.

Lecture A3

+ Activity: [Calculator, Week 4](https://github.com/utah-cs3960-sp26/calculator?tab=readme-ov-file#week-4)

Lecture B3, *Tool use*

+ Activity: [Calculator, Week 5](https://github.com/utah-cs3960-sp26/calculator?tab=readme-ov-file#week-5)
+ Reading: [How to Build an Agent](https://ampcode.com/how-to-build-an-agent)

Lecture A4

Lecture C1, *Context Engineering*

Lecture D1

Lecture C2, *Context Capacity*

Lecture D2

Lecture C3, *Prompts*

Lecture D3

Lecture C4, *Tool outputs*

Lecture D4

Lecture C5, *Sub-agents*

Lecture D5

Lecture E1

Lecture E2

Lecture E3

Lecture E4
