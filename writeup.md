# Lessons Learned from a Course on Vibe Coding

From January to April 2026 we taught "Vibe Coding" to 60 University of
Utah Computer Science undergraduates, mostly in their 3rd or 4th
year. They were excited about LLM coding agents but at the same time
wary about the new technology, and also visibly nervous about the
highly uncertain job market that they are about to be facing.

Going into this, we had a lot of questions. Perhaps the most important
of these were:
1. What is the actual curriculum here?
2. What relationship with code are we trying to promote, and how are
   we going to do that?

For example, one relationship with code could be "fire and forget"
where the students write prompts and run code, but never actually
edit, optimize, debug, profile, or even read the code. As computer
science professors who love code, this is not the relationship that we
were after---but it turned out to be surprisingly difficult to do
better.

For a curriculum, one place we turned was software engineering. Here,
our belief was that only a small proportion of the courses required
for a traditional CS degree is providing preparation for a world where
every software developer is effectively a low-level manager,
overseeing multiple AI agents. Of course, the true bottlenecks in
software engineering have always been determining what software should
actually be written, and then reliably creating software that is fit
for some particular purpose, which will often include requirements
such as usability, accessibility, platform constraints,
security-critical use cases, and safety-critical use cases. What role,
if any, does AI play in meeting these diverse requirements? More
importantly, could we get the students on the path towards being able
to sign off, as a software professional, on the fitness of a piece of
code for its intended purpose? Even when some or most of the software
was written by a coding agent?

We spent several lectures on testing, paying particular attention to
automated test oracles, which of course combine well with randomized
testing methods. We lectured on code review, specifications, software
architecture, modularity, security, and formal verification. In all
cases, our priority was to give the currently-accepted fundamentals in
the topic, and then secondarily to tie the topic in to LLM-based
software development. Our observation is that skill in these areas is
likely to be significantly more important much earlier a software
engineer's career than was previously the case.

The other half of our curriculum was less traditionally structured: it
was an answer to the question "What do developers need to know about
how modern LLMs and coding agents work, in order to use these tools
effectively?"

[Pavel elaborates here-- what were the topics? why were these the
topics? etc.]

For a coding agent, the students in our course used
[Amp](https://ampcode.com/), which provides an LLM-backed CLI tool and
also a VSCode plugin. Virtually all of the students preferred to use
the plugin. The Amp folks were generous enough to give us several
thousand dollars worth of credits, which was a key enabler for us to
run this course. (Pavel say more about money?)

We structured Vibe Coding traditionally: during most class sessions,
one of us would lecture for about an hour, leaving the final 20
minutes for an in-class exercise. We gave 1-2 reading assignments each
week, these were usually blog posts or other web-based articles, and
were occasionally a section from some paper; students had to answer a
few questions about the assigned material.

The bulk of the coursework for Vibe Coding fit into three programming
projets: a text editor, a physics simulation, and a self-directed
final project.

The text editor stretched over nine weeks. Initially,
they were to just bring up a text editor built using PyQt, implementing
two features from a list that we provided, including:
- automatic indentation and bracket/quote matching
- multiple cursors and rectangular selection
- custom fonts, colors, and keyboard shortcuts
- multi-language syntax highlighting
- find and repalce, including multi-find-and-replace
During the third week of class we had a "demo day" where each student
had to show off their text editor to one of the three of us (John, Pavel,
and our TA), answer some questions about their implementation,
talk us through their design choices, etc.

For the second part of the text editor project, we assigned each
student to take a different student's code base and implement a
feature that that student had not implemented yet. This was to be
boxed up as a pull request that they had to convince the code owner to
merge. The following week, each student had create tests that achieved
100% line coverage of their editor (with another student's feature
merged), or else document any code that could not be covered. We had a
second demo day where students had to demonstrate their testing
strategy: how did they achieve coverage of the various features of
their code? What code could not be covered and why?

For the final 

- 3 programming projects
  - a many-part assignment on building a text editor
  - a shorter 2-week assignment building a physics simulator
  - a 3-week self-directed final project
- 4 "demo days" where the 3 instructors spend approx 4 minutes per
  student interviewing them about their project and its design and implementation

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
