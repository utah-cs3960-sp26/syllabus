Lessons Learned from a Course on Vibe Coding
============================================

By [John Regehr](https://users.cs.utah.edu/~regehr/) &
[Pavel Panchekha](https://pavpanchekha.com/)

From January to April 2026 we taught "Vibe Coding" to 60 University of
Utah Computer Science undergraduates, mostly 3rd- and 4th-years. They
were excited about LLM coding agents but visibly nervous about the
highly uncertain job market that they would soon face. We figured we'd
meet the future head-on with them.

# Course Vision

We had a lot of questions going in, starting perhaps from:

1. What relationship to the code are we trying to promote?
2. What relationship to the agent are we trying to promote?

Here's what we didn't want. We didn't want a "fire and forget"
relationship to the code, where students never actually edit,
optimize, debug, profile, or even read the code. We didn't want
students to think of the agent as a "magic genie".

But it turned out to be surprisingly difficult to do better!

One vision we tried is "manager": the student is responsible for code
existing and working, but delegates actually writing to code to
subordinate agents. Students focus on dividing large projects into
small tasks that are within the agent's capabilities, testing them,
and tracking completion. This was our initial vision for the course,
but we found it quite difficult to *teach* the relevant skills. We had
a lectures on how software engineering works in industry and on the
capabilities of models, but they may not have connected with students.
It's anyway not clear that that's really what students were missing.
Maybe we needed lectures more focused on traditional management
topics, but we didn't feel comfortable teaching those topics.

Another vision is "architect", where the student writes a good
specification (including tests, standards, formal methods, and so on)
which the agent then implements. We felt comfortable lecturing on
specifications and formal methods and such. But students wanted to do
projects with music, interfaces, or games, where specifications are
hard to write. This vision works better for systems or such.

Finally, we toyed with a vision of "production engineer", where the
student oversees the agent's development process and ensures access to
the tests, metrics, tooling, and feedback needed to make progress.
This vision appeals to use, but was too abstract to students, who
struggled to sit "meta" to their own development process. We also
struggled to teach it, except via case studies.

Of course, part of the challenge is that it is genuinely unclear what
the role of programmers will be in the future. Perhaps, in time, that
will become clearer, and the course vision will resolve itself.

# Curriculum

We had a few goals for our curriculum. We promised the students no
math, so there wasn't any gradient descent. We wanted practical
skills, so students did projects, but more than anything, we didn't
want content that would go obsolete as models improve. So we didn't
teach prompting tricks or specific models or specific pitfalls. We
wanted "time-tested" wisdom more than AI-specific content.

We ended up with a split curriculum: half focused on AI, and half on
software engineering, with a particular emphasis on testing.

The AI half attempted to explain how agents work, mechanically, so
they would seem less like magic. So, for example, there were lectures
on what tokens are, how text is generated token by token, and agents
perform repeated tool calls. We then had a series of lectures on
context management, documentation, and version control. These lectures
went, we think, relatively well, and still hold up months later.

The software engineering half focused on how teams of engineers can
work together to build software fit for some purpose. This includes
requirements such as usability, accessibility, platform constraints,
security-critical use cases, and safety-critical use cases. In an
agentic world, even a solo student has to think about decomposing
tasks, handing off knowledge, and ensuring maintainability. We focused
specifically on testing, especially automated test oracles. There were
also lectures on code review, software architecture, security, and so
on, mostly traditional topics with only a bit of LLM spin. Students
were seeing some of the more advanced content for the first time, and
these topics are only getting more important with LLMs.

In surveys we ran, students seemed to think both halves of the
curriculum were valuable. Students especially appreciated being taught
how software development works in practice. It helped that both of us
have industry experience to draw on, and that many students had had
jobs or internships and could relate their own experiences.

Still, like in any class, not every lesson we intended landed. A
memorable example was an assignment where students were supposed to
write a specification for an agent to implement. Basically all
students used ChatGPT or similar to write the specification. When
questioned, they said they did this because ChatGPT's version was
"more detailed". Few seemed to realize the contradiction.

We also made mistakes. The most notable is teaching prompt loops. This
specific technique is now obsolete, and it didn't make a good
illustration of writing specs for autonomous agents. And prompt loops
are extraordinarily costly: some students accidentally cost us
hundreds of dollars in tokens by leaving theirs running too long. A
better assignment would have students write a prompt that allowed an
agent to one-shot some task. That would force students to write
a prompt with all the details they intend.

# Course Structure

Our course used [Amp](https://ampcode.com/) as its coding agent which,
at the time, used Claude Opus as its model. Virtually all of the
students used Amp through a VS Code plugin, though these days that
might change. Many students had already used Codex, Claude, Copilot,
or Gemini at jobs or internships, and they gave Amp high marks.

A key problem for us was cost: about $13,000, about $200 per student.
We chose not to rate-limit students (except a few cases of run-away
spending). If students, say, had to stick within the bounds of a
$20/month subscription, they would try to scrimp and save, which
wasn't our goal. Plus, we'd have little answer for a student who ran
out of tokens before an assignment was due. In our case, the Amp folks
were generous enough to give us many thousand dollars worth of
credits; the course would not have happened without that.

We structured class around an hour of lecture, leaving the final 20
minutes for an in-class exercise, which was graded but mostly enforced
attendance. For example, after a lecture on next token prediction, the
students vibe-coded a Markov Chain. This gave students some immediate
experience with a lecture topic.

We gave 1-2 reading assignments each week, usually blog posts but
occasionally a section from some paper, and had students answer a few
questions about it. Readings were graded to make sure students read
the material, but (after experimenting) we found that Claude Opus 4
did a perfectly fine job grading readings.

The bulk of the coursework for Vibe Coding was three programming
projects, which are discussed in the next few sections. Critically, we
promised (and held to) A grades for all students who put effort into
the class. This lifted the burden of developing fair assessments,
which would otherwise be a big challenge. Any future offering would
need to address that, and choosing assignments would be higher-stakes.

# Code Ownership

We assigned three projects: a text editor with three separate
assignments (feature implementation; code review and testing; and
performance optimization), and then a physics simulation and a
self-directed final project with one assignment each. After each
assignment, we had a "demo day" with one of us (John, Pavel, or our TA
Yumeng), where each student showed off what they'd built, answer some
questions about it, and talk us through their design choices.

The point was for students to demonstrate ownership of the code.
Reviews were mixed but, we think, for the right reasons. One student
wrote, for example, "it was challenging to express my knowledge [...]
because I didn't have it." In effect, the demo days were oral exams.
That said, these were not scalable (with a whole course period we
could only do a few minutes per student) and we never came up with a
better way to enforce ownership and responsibility.

A good fraction of the class never engaged seriously with the code
they "wrote". This was especially apparent in the testing assignment,
which asked for 100% test coverage for their text editor. We'd ask
students to, say, show us the find-replace tests, and those tests
would often "cheat" by, for example, triggering a find-replace without
checking its results. Basically, students didn't think much about test
oracles and, correspondingly, ended up with weak ones. Testing
correspondingly didn't make the editors much less buggy.

One surprise was that students would typically try to understand the
AI-written code by asking the AI. This was very clear during demo
days. We'd ask students, say, what chunk size their editor used, and
students would quite visibly have no idea where that was even defined.
Thinking it over, the traditional CS curriculum doesn't really teach
*reading* code. Students focus on *writing* code, and reading is
learned as a byproduct. Perhaps we must now explicitly teach code
reading, including techniques like grepping for related abstractions,
traversing callers and callees, and reasoning about control flow.

# Flexibility

We purposefully assigned *visual* projects. We hoped that this left
room for creativity but also have challenging specification,
correctness, and performance requirements. To some extent this was
correct, but it really depended on student skill level.

We made basically no attempt to teach students how text editors or
physics simulators normally worked. Pre-AI, that would have resulted
in all but a few students failing to write one. AI agents raised the
floor---all students produced working editors and simulators---but
quality differed enormously. The strongest students could come up with
and enforce an architecture for their agent to follow. The weakest
students quickly felt like they had nothing at all to contributed.

This was most notable in our most difficult assignment, low-latency
find-replace on large files. Without AI, implementing an `mmap`-based
piece table with a line index and chunked work would be beyond all but
the strongest students. With AI, that wasn't a problem, but students
with a foggy understanding of allocation, copies, and strings couldn't
effectively prompt the AI. In retrospect, we think attempts to simply
"raise the bar" to correct for AI assistance don't really work.
Instead, we need to teach foundational concepts like memory management
at a rigorous but more-conceptual level.

Visual software is also quite flexible: there are many different text
editors that work in quite different ways. Ideally, students would
make bold design choices, but they mostly didn't, leaving design
decisions to the AI. The AI's choices were tasteless. The physics
simulator was better---there was fewer decisions to make---though it
had the weakness that, while some students could imagine how a text
editor works, almost none could to that for a physics simulator.

In either case, tastelessness was a problem. The text editors were
ugly, buggy, and hard to use. The project was thus widely hated, but
it was just as much a problem with the simulator: objects vibrating
rapidly when in contact with walls, or hanging in mid-air. When we
pointed this out at a demo day, students would often say they hadn't
noticed the issues, and we had neither the heart to deduct many
points, nor the ability to force students to have better taste. If we
were to write an extensive rubric, the agent would just use that
rubric to do a good job.

# Long-running Projects

We assigned long-running projects to force students to make and
correct their own mistakes. This is a classic of software engineering
courses, and AI agents are, indeed, great at digging cavernous holes
Unfortunately, students were more limited in their ability or
willingness to "dig their way out" with refactoring, tests, and
specifications. Maybe the right projects and assignments would work,
but the long-running project was a mistake for us. More, shorter
projects would have been effective without sticking students in a
morass of their own making.

We also hoped that a long-running project would force students to
maintain context, and to push toward that we meaningfully changed the
requirements over the course of the project, including asking them to
make PRs to another student's project and to review the other
student's PR to their own repository. This was probably valuable for
students, but overall students didn't do a great job of engaging with
their own or others' code, and so didn't really have context to
maintain.

The final project was self selected. Naturally, that meant video
games, and also a surprising number of audio-focused projects, but
also a diverse array of cool, surprising personal projects. As with
assignments, the projects were generally more impressive than in prior
non-AI classes we've taught---one student wrote a billiards simulator
that hooked up to a real physics engine and could use computer vision
to read a real pool table---but in general the distribution of quality
seemed similar to prior years. Maybe taste and creativity were always
the bottleneck.

# Future Offerings

Overall, we think of our class as a success. It's not clear that we'll
ever offer *this* course again, but surely every Computing department
will be offering similar classes soon. Our experience suggests that
these classes are valuable and can cover important material. That
said, any such offering should confront a few questions head-on.

First, costs. Agentic coding is expensive, and tens of thousands of
dollars are scarce in academia. How will tokens be paid for? Today's
cheapest models, like OpenAI Luna, might now be good enough to address
this problem, but it's important to make sure that access to more
expensive, better models doesn't trivialize some assignments.

Second, vision. What relationship is the course trying to encourage
with the code and with the agent? This should drive the curriculum.

Third, skills. What are students lacking? Code reading, core concepts,
debugging, and performance engineering all stand out. It has to be
skills that complement AI.

Fourth, assessment. Reading and grading AI-written code makes no
sense. Neither do detailed assignments that students hand off to AI.
Nor do vague assignments where fair grading is impossible. AI code is
tasteless, but grading taste is hard.

We hope that future offerings, at Utah and elsewhere, are more
effective and impactful. The goals we had were achieved, but partially
and unevenly. A scoped-down but more-rigorous course may do better.

Still, our course showed that students both need and value software
engineering, that these skills are more important than ever before,
and that they can be taught. That's clearly valuable for students.
