Lectures for CS 3960 Vibe Coding
================================

| Week   | Monday | Wednesday | Friday          |
|--------|--------|-----------|-----------------|
| Jan  5 | 00     | A1        | release notes 1 |
| Jan 12 | B1     | A2        | release notes 2 |
| Jan 19 | ------ | *Demo*    | HW1             |
| Jan 26 | B2     | A3        |                 |
| Feb  2 | B3     | A4        |                 |
| Feb  9 | C1     | A5        | HW2             |
| Feb 16 | ------ | *Demo*    |                 |
| Feb 23 | C2     | A6        |                 |
| Mar  2 | C3     | A7        | HW3             |
| Mar  9 | ------ | ------    | ------          |
| Mar 16 | D1     | *Demo*    |                 |
| Mar 23 | D2     | D3        | HW4             |
| Mar 30 | *Demo* | D4        |                 |
| Apr  6 | D5     | D6        |                 |
| Apr 13 | D7     | D8        | HW5             |
| Apr 20 | *Demo* | ------    | ------          |

Lecture 00, *Introduction*

+ Reading: [AI Can Write Your Code. It Can’t Do Your Job.](https://terriblesoftware.org/2025/12/11/ai-can-write-your-code-it-cant-do-your-job/)
+ Activity: [Install Amp](https://ampcode.com/);
  create a native Qt-based text editor
  
Lecture A1, *Software Engineering*
+ Reading: none
+ Activity: discussion
+ Optional reading: [The Mythical Man-Month](https://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959) \
  This classic essay collection, originally written in 1975, discusses
  the lessons learned about large-scale software engineering working
  on System/360, an old IBM mainframe computer program. At the time
  this was one of the largest software developments ever done, and a
  lot of the lessons are still valid.
+ Optional reading: [Code Complete *2e*](https://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670) \
  This classic book, written in 1994 and now a little dated, is all
  about what it takes to write large software programs, besides of
  course being able to program.
+ Optional reading: [Software Engineering at Google](https://abseil.io/resources/swe-book) \
  This more recent book, published in 2020, covers somewhat more
  modern lessons learned from building large systems at Google. Google
  was early to building "Internet-scale" software and so was building
  some of the most complex software of its time. Happily, the lessons
  really are quite similar to those in the prior two books, showing
  that for over 50 years we've been learning the same kinds of things
  about software engineering.

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

Lecture A4, *Test Coverage*

+ Activity: Code coverage activity
+ Reading: [How to Balance Speed, Quality, and Maintainability in Test Suite Management](https://katalon.com/resources-center/blog/test-suite-management)
+ Optional Reading: [How to Misuse Code
  Coverage](http://www.exampler.com/testing-com/writings/coverage.pdf) \
  This article, written in 1997, makes the point that, if you just
  blindly cover uncovered code, you’re doing it wrong, and explains
  why with a lot of examples.

Lecture C1, *Context Engineering*

+ Reading: [Context Engineering for Agents](https://rlancemartin.github.io/2025/06/23/context_engineering/)

Lecture A5, *Fuzzing*

Lecture C2, *Parallelizing Work*

- Reading: [A Successful git Branching Model](https://nvie.com/posts/a-successful-git-branching-model/)
- Optional reading: Microsoft put up a [bizarre AI
  hallucination](https://nvie.com/posts/15-years-later/) of this
  diagram on their website for some reason.

Lecture A6, *Assertions*

- Reading: [QuickCheck: a lightweight tool for random testing of Haskell programs](https://dl.acm.org/doi/pdf/10.1145/351240.351266)
- Optional reading: [How to Fuzz an ADT
  Implementation](https://blog.regehr.org/archives/896), by John
- Optional reading: [Write Fuzzable Code](https://blog.regehr.org/archives/1687), by John
- Optional reading: [Use of Assertions](https://blog.regehr.org/archives/1091), by John
- Optional reading: [The Fuzzing Book](https://www.fuzzingbook.org/) \
  This book covers both how fuzzing works and how to use it
  effectively to test a wide variety of programs.

Lecture C3, *Documentation*

- Reading: [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
- Optional reading: [Explaining Code using ASCII Art](https://blog.regehr.org/archives/1653), by John

Lecture A7, *Program Verification*

Lecture D1, *Claude C Compiler*

- Reading: [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler)
- Optional reading: [I Fuzzed, and Vibe Fixed, the Vibed C Compiler](https://john.regehr.org/writing/claude_c_compiler.html), by John

Lecture D2, *JustHTML and chardet*

- Reading: [Issue #327: No right to relicense this project](https://github.com/chardet/chardet/issues/327),
  specifically the initial issue by `a2mark` and the pinned reply by `dan-blanchard`
- Reading: [Can coding agents relicense open source through a “clean room” implementation of code?](https://simonwillison.net/2026/Mar/5/chardet/)

Lecture Cn, *Tool outputs*

- Reading: [Toyota Production System](https://global.toyota/en/company/vision-and-philosophy/production-system/)

 Consider how car manufacturing is different from AI coding. It's very very different! What justifications does Toyota give for just-in-time manufacturing. Which justifications do apply to WIP in software engineering and which ones don't? What about the sections on "automation with a human touch" / jidoka—is there any relevance of this concept to software engineering?

- Optional reading: [Manifesto for Agile Software Development](https://agilemanifesto.org/) \
  This very influential manifesto, and the associated
  [Principles](https://agilemanifesto.org/principles.html) written in
  2001, was influential in the reorganization of software around
  individual developers owning all steps from writing to debugging to
  testing and reviewing code.
