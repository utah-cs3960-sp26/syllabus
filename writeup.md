Lessons Learned from a Course on Vibe Coding
============================================

From January to April 2026 we taught "Vibe Coding" to 60 University of
Utah Computer Science undergraduates, mostly in their 3rd or 4th
year. They were excited about LLM coding agents but at the same time
wary about the new technology, and also visibly nervous about the
highly uncertain job market that they are about to be facing.

# Course Vision

Going into this, we had a lot of questions. Perhaps the most important
of these were:

1. What relationship with code are we trying to promote?
2. What relationship with the agent are we trying to promote?

We started with negative examples. One relationship with code could be
"fire and forget" where the students write prompts and run code, but
never actually edit, optimize, debug, profile, or even read the code.
One relationship with the agent could be "magic genie" where the
student assumes the agent can do a good job of any task. As computer
science professors who love code, this is not what we were after.

But it turned out to be surprisingly difficult to do better!

One vision is "manager", where the student is responsible for code
existing and working, but delegates actually writing to code to
subordinate agents. The manager's main skills are dividing large
projects into small tasks that are within their workers' capabilities
and then tracking completion. This was our initial preferred vision
for the course, but we found it quite difficult to *teach* the
relevant skills. We had a number of lectures on how software
engineering works in industry and on the capabilities of models, but
they may not have connected with students.

Another vision is "architect", where the student writes a good
specification (which may include tests, standards, formal
specifications, or other things) and the agent is charged with
implementing. We felt comfortable lecturing on this, since both of us
are programming languages researchers. While this could probably make
a coherent course, the projects students wanted to do were often
music, interfaces, or games, for which it's difficult to write
specifications to begin with. The domains of computer science where
specifications matter a lot---systems software, for example---were
less exciting to students.

Of course, part of the challenge in answering these questions was that
it is genuinely unclear what the role of programmers will be in the
future. As that gets clearer maybe the course vision will resolve.

# Curriculum

For a curriculum, one place we turned was software engineering. Most
traditional CS courses effectively focus on solo programmers. If every
programmer is a manager (or, later, an architect), then we instead
needed material that focuses on teams working in concert, which means
software engineering. Of course, the true bottlenecks in software
engineering have always been determining what software should actually
be written, and then reliably creating software that is fit for some
particular purpose, which will often include requirements such as
usability, accessibility, platform constraints, security-critical use
cases, and safety-critical use cases. What role, if any, does AI play
in meeting these diverse requirements? More importantly, could we get
the students on the path towards being able to sign off, as a software
professional, on the fitness of a piece of code for its intended
purpose? Even when some or most of the software was written by a
coding agent?

We didn't want to teach anything that would obsolete with improving
model capabilities. We didn't teach prompt engineering tricks or
recommend specific models for specific tasks. We wanted "time-tested"
wisdom more than from AI-specific content. When we did cover AI we
avoided math, so we didn't cover gradient descent or the attention
mechanism itself (besides some vague hand-waving).

We spent many lectures on testing, paying particular attention to
automated test oracles, which of course combine well with randomized
testing methods. We lectured on code review, specifications, software
architecture, modularity, security, and formal verification. In all
cases, our priority was to give the currently-accepted fundamentals in
the topic, and then secondarily to tie the topic in to LLM-based
software development. Many students seemed to be seeing some of the
more advanced content for the first time. Our observation is that
skill in these areas is likely to be significantly more important much
earlier a software engineer's career than was previously the case.

The other half of the curriculum attempted to explain the agents'
capabilities and what the manager should do to make them successful.
There were a few lectures on LLM basics, like what tokens are, how
text is generated token by token, and how tool calls allow an LLM to
code. Then there was a series of lectures on context management,
memory, and version control. We figured that AI capabilities would
continue improving, so exact capabilities or prompting tricks weren't
worth teaching, but that any LLM-based system would be limited by what
would make it into the LLM's context. We also hoped that describing
how LLMs worked would allow students to see limitations and weaknesses
instead of just assuming the LLM is good at everything.

In surveys we ran, students seemed to think both halves of the
curriculum were quite valuable and interesting. Many students were
especially appreciative to be taught how software development works in
practice. It helped that both of us have industry experience to refer
to, and it also helped that many students had had jobs and could
relate their own experiences.

That said, like lectures in any class, they weren't entirely
successful. A memorable example was an assignment where students were
supposed to write a prompt file with a specification, and the agent
would then implement that specification using a prompt loop. We
discovered that basically all students had actually generated their
prompt files using ChatGPT or similar tools. When questioned, they
said they did this because ChatGPT's prompt was "more detailed". Few
seemed to realize the contradiction.

We also made mistakes. The most notable is teaching "prompt loops" /
"Ralph loops". While these are effective, we don't think any of our
students reached the level of effectiveness with agents where prompt
loops produces good software, and they are extraordinarily costly.
Some students accidentally left their prompt loop running for too
long, costing hundreds of dollars in tokens. It would be worth it if
there was pedagogical value, but we didn't see much of one.

# Course Structure

Our course used [Amp](https://ampcode.com/) as its coding agent. Amp
is a coding agent, available in VSCode or the CLI, which during the
class used Claude Opus as its LLM. Virtually all of the students
preferred to use the VS Code plugin. Many students had already used
Codex, Claude, Copilot, or Gemini at jobs or internships, and they
gave Amp high marks.

A key question for future AI coding courses is cost. The Amp folks
were generous enough to give us many thousand dollars worth of
credits. We couldn't have run the course without that. Our total cost
ended up being about $13,000, or a bit over $200 per student. We
consciously tried not to rate limit students (which in a few cases
lead to run-away spending where we had to intervene manually), but we
don't think the course would have been the same if we'd tried to limit
students, to, say, the bounds of a $20/month subscription. Tens of
thousands of dollars is hard to come up with, so without corporate
support we're not sure how to run the class.

We structured Vibe Coding traditionally: during most class sessions,
one of us would lecture for about an hour, leaving the final 20
minutes for an in-class exercise. The in-class exercise was graded,
but mostly to enforce attendance. We gave 1-2 reading assignments each
week, these were usually blog posts or other web-based articles, and
were occasionally a section from some paper; students had to answer a
few questions about the assigned material. Readings were graded to
ensure that students read the material, but (after experimenting) we
found that Claude Opus did a perfectly fine job grading readings. This
made readings very easy to assign and made them effective at
delivering additional content.

The bulk of the coursework for Vibe Coding, however, fit into three
programming projects: a text editor, a physics simulation, and a
self-directed final project. The text editor stretched over three
separate assignments (feature implementation; code review and testing;
and performance optimization), while the physics simulator and final
projects were shorter. At the end of each assignment, we had a "demo
day" where each student had to show off their text editor to one of
the three of us (John, Pavel, and our TA Yumeng), answer some
questions about their implementation, talk us through their design
choices, etc.

The point was for students to demonstrate ownership of the code.
Reviews were mixed but, we think, for the right reasons. One student
wrote, for example, "it was challenging to express my knowledge [...]
because I didn't have it." That said, these "demo days" were not
scalable (they needed a whole course period and we still only had a
few minutes per student) and we never came up with a better way to
enforce ownership and responsibility. Probably a good fraction of the
class never engaged seriously with any of the code they "wrote". This
was very apparent during the testing assignment, where students had to
achieve 100% code coverage for their text editor. We'd ask students
to, say, show us the find-replace tests, and those tests would often
"cheat", for example, triggering a find-replace (to achieve coverage)
but not actually checking that the find-replace was done correctly.
Testing correspondingly didn't make the editors much less buggy.

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

Our hope with these projects was that *visual* software would provide
room for creativity but also have challenging specification,
correctness, and performance constraints where students would need to
guide the LLM. To some extent this was correct. But a challenge we
didn't anticipate was student skill level. We made basically no
attempt to teach students how text editors or physics simulators
worked. Pre-AI, that would have resulted in all but a few students
failing to write one. AI agents substantially raised the
floor---basically all students produced working editors and
simulators---but also increased dispersion across skill levels
significantly. The strongest students could come up with and enforce
an architecture for their agent to follow. The weakest students,
though, quickly felt like there was nothing they could contribute at
all.

Visual software is also quite flexible: there are many different text
editors that work in quite different ways. Ideally, students would
make bold design choices, but they mostly didn't, leaving design
decisions to the AI. The AI's choices were largely tasteless. This had
the funny side effect that almost all students' text editors were
terrible (buggy, unintuitive, lacking features, etc) and so were
widely hated. The physics simulator was better---there was less room
for choice---though it had the weakness that students who could
imagine how a text editor works often had no idea how a physics
simulator would.

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

We *had* hoped that a long-running assignment would force students to
"dig their way out" of their own mistakes. Software engineering
courses often attempt this, and AI agents are great at "digging
holes", so to speak. Unfortunately, students were quite limited in
their willingness or ability to "dig their way out" via refactorings,
tests, and specifications. It's possible that better assignment design
would help (perhaps we could have an assignment to refactor their text
editor into model-view-controller form, or into modular plugins, or
something) but I think the long-running project was a mistake how we
ran it. More shorter projects would have been more effective,
especially since students could build complex software very quickly.

For the final project, we let students propose a project of their own.
Naturally, there were many video games, and a surprising number of
audio-focused projects, but also a diverse array of surprising
personal projects. The projects were generally more impressive than in
prior non-AI classes we've taught---one student wrote a billiards
simulator that hooked up to a real physics engine and could use
computer vision to read a real pool table---but in general the
distribution of quality seemed similar to prior years.

In any case, we promised (and held to) A grades for essentially all
students who put effort into the class. This lifted the burden of
developing fair assessments, which would be a big challenge with how
we ran the class. An essential challenge is that *detailed* homework
assignments can be completed autonomously by AI agents, while *vague*
homework assignments are hard to grade with a high bar, and AI agents
are extremely effective at meeting vague, low bars. AI code is often
tasteless, but grading taste is difficult.

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

---------------

lessons learned

**** A lot of the material feels reusable even if the tech improves (who knows, of course)
*** The success: software engineering
**** Most students in the class are hearing about specifications, tests, CI for the first time
**** But they largely enjoyed learning about it!
**** This stuff is all *way* more valuable now, so we should focus on it
** Assessment
*** Our plan
**** We were gonna basically give all As and grade on effort
**** Readings + attendance + assignments
*** A success: readings
**** Students answer some short questions
**** I think students in fact do them
**** And we grade them with AI, takes very little time
*** Assignments: the triple-bind
**** If your assignments are detailed enough, the AI can grind to victory
**** If they're too vague, the AI can one-shot something plausible
**** If they're hard enough that the AI gets stuck, the students do too
*** Some things we tried
**** We tried doing a long-ish project to force students to maintain state
***** They mostly didn't, I think this was a failure
**** We tried doing assignments to help them understand code
***** I don't know that this worked that well
**** We tried pushing students with harder projects
***** The weaker ~50% of students just couldn't do it
** What skills are students lacking?
*** Reading: a bottleneck
**** Students are bad at reading code
**** They mostly don't review what the AI writes, or if they do, not effectively
**** If the AI can't do it they barely understand how to help
*** Architecture: they don't know how
**** Students struggle to think of detail at multiple levels
**** They can't synthesize architecture from code or vice versa
**** Lacking this they delegate it to the AI
**** The AI is bad at this
*** Taste: A real failure
**** I was hoping we could grade to and enforce "taste" of some kind
**** For this reason we made a UI-heavy application
**** We basically failed at that. We couldn't grade for that efficiently and students couldn't do it
**** But also for this reason this application was universally hated, for sucking
** A future challenge: costs
*** Running this class will end up costing us $15k, which is $250/student, and I think you'd want to go bigger
*** We got most of this donated but that's not going to be workable going forward
*** It might get cheaper one day but we might have a while before that happens
*** Maybe local models catch up, and we self-host? Maybe costs come down?
*** Teaching something like this is critical but gonna set fire to the budget~

- when the students have a good LLM coding agent, it's very difficult
  to force them to personally engage with their code base
  - our response was to ask about their code during demo days
    - some fraction of the class never actually engaged with their code
- it's hard to come up with assignments that a modern LLM can't one-shot
  - our response was multi-stage project where we meaningfully changed the
    requirements with respect to the previous stage
    - including submitting patches to another repo
    - and reviewing patches to their own repo
- forcing students to achieve 100% test coverage was a mixed bag
  - many of them just let the LLM do what it wanted, rather than taking this as
    an opportunity to get to know the code base better
- students want to know this stuff, and want to understand real-world
  software engineering
- our overall premise and plan were sound, and seemed to work out overall
- we can come up with learning outcomes, but I'm not sure we yet have the right ones
- this kind of course is expensive to run!

what relationship with the code do we want the students to have?
make a list of these relationships
- understand the code in broad strokes
- understand the code in detail
- be responsible for the code
- be able to write down the desiderata
- 

are the coding agents a leveling or anti-leveling force?

couldn't have done this earlier

ground rules for agent loop:
  completely autonomous or start over
    but there have to be better tests/spec
  it's one shot!!!


---------------------------

learning outcomes

Have a basic understanding of text prediction in general, and LLM-based text prediction in particular
What are tokens?
How do we predict the next one?
How does training work?

Be able to use AI to construct large applications to a high degree of reliability
LLM-assisted testing & specification
LLM-assisted refactoring
LLM-assisted algorithm development and optimization

Be able to develop context, including tools, specifications, tests, and documentation, for use with AI coding agents
Basic testing
Advanced testing– property-based, exhaustive, randomized
Design for testing
Assertions, invariants
Code review
Documentation – for humans and also for the LLM
Logging – super important since the LLM is great at reading

---------------------------
