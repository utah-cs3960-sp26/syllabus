Lessons Learned from a Course on Vibe Coding
============================================

By [John Regehr](https://users.cs.utah.edu/~regehr/) &
[Pavel Panchekha](https://pavpanchekha.com/)

From January to April 2026 we taught "Vibe Coding" to 60 University of
Utah Computer Science undergraduates, mostly in their 3rd or 4th
year. They were excited about LLM coding agents but at the same time
wary about the new technology, and also visibly nervous about the
highly uncertain job market that they would soon face.

# Course Vision

Going into this, we had a lot of questions. Perhaps the most important
of these were:

1. What relationship with the code are we trying to promote?
2. What relationship with the agent are we trying to promote?

We started with negative examples. One relationship with code could be
"fire and forget" where the students write prompts and run code, but
never actually edit, optimize, debug, profile, or even read the code.
That's what "vibe coding" usually means, but we didn't want that. One
relationship with the agent could be "magic genie" where the student
assumes the agent can do a good job of any task. As computer science
professors, this is not what we were after.

But it turned out to be surprisingly difficult to do better!

One vision we tried is "manager", where the student is responsible for
code existing and working, but delegates actually writing to code to
subordinate agents. The manager's main skills are dividing large
projects into small tasks that are within their workers' capabilities
and then tracking completion. This was our initial preferred vision
for the course, but we found it quite difficult to *teach* the
relevant skills. We had a lectures on how software engineering works
in industry and on the capabilities of models, but they may not have
connected with students, and it's not clear that that's really what
students were missing, anyway. Such a focus could work with lectures
more focused on traditional management topics, but we didn't feel
comfortable teaching that subject.

Another vision is "architect", where the student writes a good
specification (which may include tests, standards, formal methods, or
other things) and the agent is charged with implementing. We felt
comfortable lecturing on this, since both of us are programming
languages researchers, and this could probably make a coherent course.
But the projects students wanted to do were often music, interfaces,
or games, for which it's difficult to write specifications. The
domains of computer science where specifications matter most---like
systems software---were less exciting to students.

Toward the end, we also toyed with a vision of "production engineer",
where the student oversees the agent's actual development process and
ensures it has access to sufficient tests, metrics, observability
tooling, and feedback to make consistent progress. We found that the
level of abstraction required to think about software development
feedback loops was difficult for most students, and we also struggled
to produce relevant lecture content besides cases studies. It's
possible that there's a coherent course here, but we didn't have the
time to find it.

Of course, part of the challenge in answering these questions was that
it is genuinely unclear what the role of programmers will be in the
future. As that gets clearer maybe the course vision will resolve.

# Curriculum

We didn't want to teach anything that would obsolete with improving
model capabilities. We didn't teach prompt engineering tricks or
recommend specific models for specific tasks. We wanted "time-tested"
wisdom more than AI-specific content. When we did cover AI we avoided
math, so we didn't cover gradient descent or the attention mechanism
itself, besides some very high-level descriptions.

We ended up with a split curriculum: half focused on AI, and half on
software engineering, with a particular emphasis on testing.

The AI half attempted to explain the agents' capabilities from the
bottom up. The hope was that describing LLMs mechanically would allow
students to see limitations and weaknesses instead of just assuming
the LLM is good at everything. So, for example, there were lectures on
basics like what tokens are, how text is generated token by token, and
how tool calls allow an LLM to code. We also had a more practical
series of lectures on context management, memory, and version control,
which we figured were the best student-controllable method of
affecting the quality of their AI-written code, and also would not be
obsoleted too quickly.

The software engineering half focused on how teams of engineers can
write good software. Traditional CS courses effectively focus on solo
programmers, but in an agentic world, even a solo student has to think
about decomposing tasks, handing off knowledge, and ensuring
maintainability. We pitched software engineering as the basics of
determining what software should actually be written and then reliably
creating software that is fit for that particular purpose. This
includes requirements such as usability, accessibility, platform
constraints, security-critical use cases, and safety-critical use
cases. What role, if any, does AI play in meeting these diverse
requirements? More importantly, could we get the students on the path
towards being able to sign off, as a software professional, on the
fitness of a piece of code for its intended purpose? Even when some or
most of the software was written by a coding agent?

We focused specifically on testing, paying particular attention to
automated test oracles, which of course combine well with randomized
testing methods. We lectured on code review, specifications, software
architecture, modularity, security, and formal verification. In all
cases, our priority was to give the currently-accepted fundamentals in
the topic, and then secondarily to tie the topic in to LLM-based
software development. Many students seemed to be seeing some of the
more advanced content for the first time. Our observation is that
skill in these areas is likely to be significantly more important much
earlier a software engineer's career than was previously the case.

In surveys we ran, students seemed to think both halves of the
curriculum were quite valuable and interesting. Many students were
especially appreciative to be taught how software development works in
practice. It helped that both of us have industry experience to refer
to, and it also helped that many students had had jobs and could
relate their own experiences.

Still, like in any class, our lectures weren't entirely successful. A
memorable example was an assignment where students were supposed to
write a specification and have the agent implement it using a prompt
loop. Basically all students generated their specification using
ChatGPT or similar tools. When questioned, they said they did this
because ChatGPT's version was "more detailed". Few seemed to realize
the contradiction.

We also made mistakes. The most notable is teaching prompt loops in
the first place. We don't think any of our students reached the level
of effectiveness with agents where prompt loops produce good software.
And they are extraordinarily costly: some students accidentally cost
us hundreds of dollars in tokens by leaving theirs running too long.
We didn't see much pedagogical value to justify the cost. A better and
possibly cheaper assignment would ask students to write a prompt that
would allow the agent to one-shot some task. That might force students
to write detailed prompts and think through necessary information.

# Course Structure

Our course used [Amp](https://ampcode.com/) as its coding agent. At
the time, Amp used Claude Opus as its model, and was available in
VSCode or the CLI. Virtually all of the students preferred the VS Code
plugin. Many students had already used Codex, Claude, Copilot, or
Gemini at jobs or internships, and they gave Amp high marks.

A key question for future AI coding courses is cost. The Amp folks
were generous enough to give us many thousand dollars worth of
credits. We couldn't have run the course without that. Our total cost
ended up being about $13,000, or a bit over $200 per student. We
consciously tried not to rate-limit students (except a few cases of
run-away spending where we did intervene), and we don't think the
course would have worked if we'd tried to limit students. If students,
say, had to stick within the bounds of a $20/month subscription, they
would try to scrimp and save, and we'd have little answer for a
student who ran out of tokens before an assignment was due. Still,
tens of thousands of dollars is hard to come up with, so without
corporate support we're not sure how to run the class.

We structured class sessions to include about an hour of lecture,
leaving the final 20 minutes for an in-class exercise. The in-class
exercise was graded, but mostly to enforce attendance. They often
involved the students vibe-coding something, like a Markov Chain,
and we found that this was quite effective at giving students
immediate experience with a lecture topic.

We gave 1-2 reading assignments each week, usually blog posts but
occasionally a section from some paper, and students had to answer a
few questions about the assigned material. Readings were graded to
ensure that students read the material, but (after experimenting) we
found that Claude Opus did a perfectly fine job grading readings.

The bulk of the coursework for Vibe Coding, however, fit into three
programming projects, which deserve a more extensive discussion. We
promised (and held to) A grades for essentially all students who put
effort into the class. This lifted the burden of developing fair
assessments, which would be a big challenge given how we ran the
class, but any future offering would need to address it.

# Code Ownership

We assigned three projects: a text editor, a physics simulation, and a
self-directed final project. The text editor stretched over three
separate assignments (feature implementation; code review and testing;
and performance optimization) and nine weeks, while the physics
simulator and final projects were shorter at three weeks each. At the
end of each assignment, we had a "demo day" where each student had to
show off their text editor to one of the three of us (John, Pavel, and
our TA Yumeng), answer some questions about their implementation, and
talk us through their design choices.

The point was for students to demonstrate ownership of the code.
Reviews were mixed but, we think, for the right reasons. One student
wrote, for example, "it was challenging to express my knowledge [...]
because I didn't have it." In effect, the demo days were oral exams.
That said, these were not scalable (with a whole course period we
could only do a few minutes per student) and we never came up with a
better way to enforce ownership and responsibility. Probably a good
fraction of the class never engaged seriously with any of the code
they "wrote". This was very apparent during the testing assignment,
where students had to achieve 100% code coverage for their text
editor. We'd ask students to, say, show us the find-replace tests, and
those tests would often "cheat", for example, triggering a
find-replace (to achieve coverage) but not actually checking that the
find-replace was done correctly. Testing correspondingly didn't make
the editors much less buggy. We're not sure what, besides punitive
grading, would have helped.

One surprise was that students would typically try to understand the
AI-written code by asking the AI. This was very clear during demo
days. We'd ask students, say, what chunk size they used for something,
and students would quite visibly have no idea where that was even
defined. Thinking it over, the traditional CS curriculum doesn't
really teach *reading* code. Students focus on *writing* code, and
reading is learned as a byproduct. Perhaps future CS education should
explicitly teach code reading, including techniques like grepping for
related abstractions, traversing callers and callees, and reasoning
about control flow.

# Flexibility

We purposefully chose *visual* software. Our hope was that that would
provide room for creativity but also have challenging specification,
correctness, and performance requirements that would require student
guidance of LLMs. To some extent this was correct, but it really
depended on student skill level. We made basically no attempt to teach
students how text editors or physics simulators worked. Pre-AI, that
would have resulted in all but a few students failing to write one. AI
agents substantially raised the floor---basically all students
produced working editors and simulators---but also increased
dispersion across skill levels significantly. The strongest students
could come up with and enforce an architecture for their agent to
follow. The weakest students, though, quickly felt like there was
nothing they could contribute at all.

This was most notable during our most difficult assignment, which
required a low-latency find-replace function in their text editor.
Without AI, implementing something like an `mmap`-based piece table
with a line index and batched find-replace jobs would be beyond all
but the very strongest students. With AI, writing and debugging the
code wasn't a problem, but many students had a foggy-enough idea of
allocation, copies, and strings---let alone virtual memory and text
encodings---that they couldn't even effectively prompt the AI. In
retrospect, we think attempts to simply "raise the bar" thanks to AI
assistance don't really work. To do that, we would need to teach many
foundational concepts (like memory management) at a more rigorous but
conceptual basis.

Visual software is also quite flexible: there are many different text
editors that work in quite different ways. Ideally, students would
make bold design choices, but they mostly didn't, leaving design
decisions to the AI. The AI's choices were tasteless. The physics
simulator was better---there was less room for choice---though it had
the weakness that, while some students could imagine how a text editor
works, almost none had any idea how a physics simulator would.

In either case, tastelessness was a problem. Almost all students' text
editors were terrible: ugly, buggy, and hard to use. This made them
widely hated, and students begged us to move on to a new project. But
it was just as much a problem with the simulator. During demo days,
we'd point out to students simple, easily-observable issues, like
objects vibrating rapidly when in contact with two walls, or just
hanging in mid-air, and students would often say they hadn't noticed
the issues. We didn't have the heart to give major point deductions
for this, and didn't know how else to force students to have better
taste. A key problem is that, if we were to give students an extensive
rubric, the agent would use that rubric to do a good job.

# Long-running Projects

We *had* hoped that a long-running assignment would force students to
"dig their way out" of their own mistakes. Software engineering
courses often attempt this, and AI agents are great at "digging
holes", so to speak. This worked great: cavernous holes were quickly
dug. Unfortunately, students were more limited in their willingness or
ability to use refactoring, tests, and specifications to fix the
problem. It's possible that better assignment design would help
(perhaps we could have an assignment to refactor their text editor
into model-view-controller form, or into modular plugins) but I think
the long-running project was a mistake the way we ran it. More,
shorter projects would have been more effective; with the long
projects, students were often just stuck with their own bad choices,
limiting their ability to do further assignments.

We also hoped that a long-running project would force students to
maintain context, and to push toward that we meaningfully changed the
requirements over the course of the project, including asking them to
make PRs to another student's project and to review the other
student's PR to their own repository. This was probably valuable for
students, but overall students didn't do a great job of engaging with
their own or others' code, and so didn't really have context that they
were maintaining for the AI. Simple things like testing frameworks the
agent could figure out on its own, and students often didn't know or
own more complex invariants and design decisions.

For the final project, we let students propose a project of their own.
Naturally, there were many video games, and a surprising number of
audio-focused projects, but also a diverse array of surprising
personal projects. The projects were generally more impressive than in
prior non-AI classes we've taught---one student wrote a billiards
simulator that hooked up to a real physics engine and could use
computer vision to read a real pool table---but in general the
distribution of quality seemed similar to prior years. Perhaps taste
and creativity had always been the bottleneck there.

# Future Offerings

It's not clear that we'll ever offer *this* course again, but surely
every Computing department will be offering classes with AI coding
soon. Our experience suggests that these classes can be valuable for
students and can cover important material. Overall, we think of our
class as a success. That said, any such offering should confront a few
questions head-on.

First, costs. Agentic coding is expensive, and tens of thousands of
dollars are scarce in academia. How will tokens be paid for?

Second, vision. What relationship is the course trying to encourage
with a student's code and agents? This should drive the curriculum.

Third, skills. What specific skills and knowledge are students
lacking? We think there are many under-developed skills that could be
at the center of such a course. Code reading, core concepts,
debugging, performance engineering, and others all stand out.
By definition, these skills must complement AI.

Fourth, assessment. Reading and grading AI-written code makes no
sense. Neither does writing detailed assignments for students to hand
off to AI. Ideally one would assess whatever skills one is teaching.
An essential challenge is that *detailed* homework assignments can be
completed autonomously by AI agents, while *vague* homework
assignments are hard to grade with a high bar, and AI agents are
extremely effective at meeting vague, low bars. AI code is often
tasteless, but grading taste is difficult.

But courses like this one will need to be taught, and we hope future
offerings, at Utah or elsewhere, can figure out how to teach them
more effectively. Many goals we had weren't achieved, at least for the
weaker students. A scoped-down but more rigorous course may be better.

Still, we think our course showed that students both need and value
learning software engineering, and also that these skills are more
important now that AI agents write the code. The course was largely
successful and conveying these skills, and clearly valuable for the
students.
