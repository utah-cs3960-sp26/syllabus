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
one in lexical order, among the students enrolled in the
class. We'll post a list of uNIDs to Piazza to make this easy to find.
If you're the last student in this list, do the obvious
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
asks you questions about your editor, you must answer them clearly
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
this. However, the code review belongs to you. If it is unreasonable or
makes no sense, this is your fault. An AI is not a person and it
cannot take responsibility for something.

In Canvas, hand in links to your two code reviews by the due date.

## Week 6

This week your code base should include the feature that you merged
from another student in the class. Your assignment is to get close to
100% code coverage on your editor (including the new feature).

You have three main tools at your disposal here. You may add new test
cases to cover uncovered lines of code. Second, you may remove lines
of code that you're certain are dead. Third, if there are chunks of
code that you can't cover but you don't think are dead, you must
explain each of them to us using a couple of sentences of English
text. If there are more than 10 of these, then you don't need to
write about all of them, just the first 10. **You are to write these
yourself, don't use the AI.** We want to know that you understand
why this code can't be covered.

By the due day (5pm on Friday Feb 13), produce a document in the
root directory of your repo, called COVERAGE.md, which mentions:
- what command we should run to measure the coverage of your tests
- what total percent coverage you have achieved
- a list of exceptions that you could not cover. each of them should
  link to a block (a range of lines) of code in your repo, and then
  include the description mentioned above, explaining why this
  code is not covered. Again, you don't need to do more than 10
  of these, and you can do zero of them if you have achieved
  100% coverage of your editor.

# Submission

See instructions in the individual weeks.

# Demo Day

TBA
