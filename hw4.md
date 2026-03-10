CS 3960 Homework 4
------------------

Status: draft \
Due: 27 Mar

In this assignment you will build a new project: a physics simulator.

# Requirements

Implement a 2D physics simulator. The simulator should simulate
circular balls and fixed, immovable walls. The balls should be
influenced by gravity and should collide with the walls and with other
balls in non-elastic collisions with restitution. If you don't know
what that means, that's OK, Amp probably does.

Use SDL3 via C++. You can ask Amp or ChatGPT how to install it.
Running your application should set up an initial "scene" with about a
thousand balls in some kind of container made up of wall pieces. Set
up the initial scene so the balls bounce around for a while and then
settle down. Ideally it'll also be fast enough that it's pleasant to
look at.

The hard part is going to be making sure the balls don't end up
overlapping or squeezing through the walls. You'll also sometimes see
balls start vibrating really fast. Sometimes they vibrate fast and
faster and eventually shoot off to infinity. Make the restitution
amount configurable; you should see things settle down faster with
less restitution, and you should see the final "settled" state take up
the same amount of space no matter the amount of restitution.

# Approach & Submission

For this project we want, as much as possible, to have Amp build it
autonomously. Use a prompt loop: write a `PROMPT.md` file and commit
it to your repository. Then ask Amp to continuously start sessions
with that prompt by running this command:

    git commit -m "Prompt changes" -- PROMPT.md
    while true; do cat PROMPT.md | amp --mode deep 2>&1 | tee -a amp.log; done

The first line commits any prompt changes, the second starts Amp with
the prompt in `PROMPT.md`, and restarts it when it's done. Don't edit
any files other than `PROMPT.md`. You can use `smart` or `deep` or
`rush` mode by editing the command; we've found that `deep` mode seems
best for autonomous work.

Before starting Amp, think about what tools Amp will need access to so
it can debug your physics simulation. You might want to read an [Amp
blog post](https://ampcode.com/notes/feedback-loopable) on setting up
automated software engineering for a similar task. You might also want
to describe the high-level project goals, tell Amp when to commit, how
to test, and where to write documentation and track progress.

You can stop the prompt loop at any time and adjust your prompt. Make
sure to commit changes; this will let you look back through your edits
later. Watch Amp as it works. You'll notice it do dumb things, and
then you'll want to adjust your prompt to make it work better.

Push your work [to Github](https://github.com/utah-cs3960-sp26) and
name your repository `simulate-uXXXXXXX`.

## Week 8

Create a `RESULTS.md` file in your repository. Run your simulator and
summarize the current status of your physics simulator. Then look
through the history of all edits you ever made to your prompt.
Detail the changes you made and why you made them. What Amp
misbehaviors did you notice? What and why did you add to the prompt
file? Did you remove anything?

## Week 9

Do the same as Week 8, clearly marking what parts of `RESULTS.md` are
from Week 8 and which are from Week 9.

# Demo Day

Please come to class ready to run your simulator and:

- Demonstrate that it works
- Show off your prompt file and talk through its content
- Explain what Amp behaviors you observed and what you added or
  removed from the prompt file to address them.

Expect to spend a few minutes on each one, including answering
follow-up questions.
