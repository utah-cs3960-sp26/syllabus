CS 3960 Homework 2
------------------

Status: draft \
Due: 13 Feb

In this assignment you will continue to work on text editors.

# Requirements

## Week 4

BEFORE YOU START: Make sure your README.md includes the necessary
instructions telling people how to run your text editor. Someone else
will need to run it now.

This week, you will not be working on your own text editor, but rather
on the editor belonging to the student with the uNID that is the next
higher one in lexical order, among the students enrolled in the
class. We'll post a list of uNIDs to Piazza to make this easy to find.
If you're the last or first student in this list, do the obvious
wraparound.

The first thing you should do is to familiarize yourself with the text
editor belonging to the other student. Make sure you can run it, play
around with its features, run its test suite, etc.

Your assignment is to implement a significant new feature in this text
editor that is not yours. The feature that you choose should be one of
those we listed for Assignment 1, that the code owner did not choose
to implement. If the code owner implemented all of the features in the
list, then you should propose a significant new feature (and it is
fine to ask John and Pavel for ideas).

You are free to ask questions, directed towards the author of the text
editor that you're working with. But you don't need to. If someone
asks you questoions about your editor, you must answer them clearly
and promptly.

Sometime before the due date for this assignment (Friday Jan 30 at
5pm), you will have submitted a pull request to the repository
containing the editor that you added your feature to. The pull request
should include a reasonable collection of tests for the new
feature. Also, you must not break any of the existing tests that are
in the repository when you started.

In Canvas, hand in a link to your pull request by the due date: Jan 30 @5pm.

## Week 5

During this week, each of you will provide a code review for two
different pull requests. First, you will review the pull request that
a different student in the class has made to your repository. Second,
you will review the pull request submitted to the repository belonging
to the person with the uNID that is one before you in the list. Thus,
every pull request should receive two code reviews.

What goes into a code review? Basically, you should comment on
specific things that are good and bad about the pull request. Does it
fit into the software architecture? Does it basically make sense?  Can
you find any bugs in it? Does it include enough tests? Etc.  We'll
also discuss code reviews in class.

Can you get help from AI for code review? Sure! In fact we encourage
this. However, the code review belongs to you. If it is unreaonable or
makes no sense, this is your fault. An AI is not a person and it
cannot take responsibility for something.

In Canvas, hand in links to your two code reviews by the due date.

## Week 6

This week your code base should include the feature that you merged
from another student in the class. The first thing you should do is
run your editor's test suite, with the Python code coverage tool
enabled:

https://github.com/coveragepy/coveragepy

But you should be able to easily get coverage like this:

```
pytest --cov=pyedit
```

Report the total coverage achieved by your unit tests. 

# Submission

See instructions in the individual weeks.

# Demo Day

TBA
