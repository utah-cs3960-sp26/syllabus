CS 3960 Homework 4
------------------

Status: released \
Due: 27 Mar

In this assignment you will build a new project: a physics simulator.

# Requirements

Implement a 2D physics simulator. The simulator should simulate
circular balls and fixed, immovable walls. The balls should be
influenced by gravity and should collide with the walls and with other
balls in non-elastic collisions with restitution. If you don't know
what that means, that's OK, Amp probably does.

Use SDL3 via C++. (Ask Amp or ChatGPT to install it.) Running your
application should set up an initial "scene" with about a thousand
balls in some kind of container made up of wall pieces. Set up the
initial scene so the balls bounce around for a while and then settle
down. Ideally it'll also be fast enough that it's pleasant to look at.

The hard part is going to be making sure the balls don't end up
overlapping or squeezing through the walls. You'll also sometimes see
balls start vibrating really fast. Sometimes they vibrate fast and
faster and eventually shoot off to infinity. Make the restitution
amount configurable; you should see things settle down faster with
less restitution, but the final "settled" state should take up the
same amount of space no matter the amount of restitution.

# Approach & Submission

For this project we want, as much as possible, to have Amp build it
autonomously. Use a prompt loop: write a `PROMPT.md` file and commit
it to your repository. Then ask Amp to continuously start sessions
with that prompt. On Linux and macOS, use this prompt:

    git commit -m "Prompt changes" -- PROMPT.md
    while true; do cat PROMPT.md | amp --mode deep 2>&1 | tee -a amp.log; done

If you're on Windows, use this instead, in Powershell:

    git commit -m "Prompt changes" -- PROMPT.md
    while ($true) {
        Get-Content PROMPT.md -Raw | amp --mode deep 2>&1 | Tee-Object -FilePath amp.log -Append
    }

The first line commits any prompt changes, the second starts Amp with
the prompt in `PROMPT.md`, and restarts it when it's done.
You can tweak this for your system if you want, or you can test
`smart` versus `deep` mode.

Before starting Amp, think about what tools Amp will need access to so
it can debug your physics simulation. You might want to read an [Amp
blog post](https://ampcode.com/notes/feedback-loopable) on setting up
automated software engineering for a similar task. You might also want
to describe the high-level project goals, tell Amp when to commit, how
to test, and where to write documentation and track progress.

Don't edit any files other than `PROMPT.md`. We want you to focus on
guiding an autonomous Amp, not doing the work yourself. But do watch
Amp as it works. You'll notice it do dumb things, and then you'll want
to stop the loop, adjust your prompt to make it work better, and then
restart it.

Make sure to commit changes to the prompt file; this will let you look
back through your edits later. 

Push your work [to Github](https://github.com/utah-cs3960-sp26) and
name your repository `simulate-uXXXXXXX`.

## Week 10

Create a `RESULTS.md` file in your repository. Run your simulator and
summarize the current status of your physics simulator. Ideally you'll
get all the bugs with balls phasing through walls or vibrating to
infinite speed fixed.

Look through the history of all edits you ever made to your prompt.
Detail the changes you made and why you made them. What Amp
misbehaviors did you notice? What and why did you add to the prompt
file? Did you remove anything?

## Week 11

Make it possible to describe the initial scene in a CSV file; the CSV
file should have one row per ball and list a starting position and a
color. (The walls can be fixed, or you can add them and even other
fields, like size, if you want.) Make the simulator save the final
positions to a similar CSV file. Add a tool that takes an initial
scene CSV file and assign colors based on where the final balls end up
and what color a given image has at that location.

If you do it right, you should be able to run the simulator, have a
lot of colorful balls bounce around seemingly at random, and then when
things settle down you should be able to see an image form. There are
[videos on Youtube][pezza] where you can see this in action.

[pezza]: https://youtu.be/9IULfQH7E90?si=BAt848YncoYFaSBp&t=410

Write up the same things as Week 8, clearly marking what parts of
`RESULTS.md` are from Week 8 and which are from Week 9.

# Demo Day

Please come to class ready to run your simulator and:

- Demonstrate that it works
- Show off your prompt file and talk through its content
- Explain what Amp behaviors you observed and what you added or
  removed from the prompt file to address them.

Expect to spend a few minutes on each one, including answering
follow-up questions.
