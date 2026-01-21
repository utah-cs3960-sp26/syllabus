CS 3960 Homework 1
------------------

Status: draft
Due: 13 Feb

In this assignment you will continue to work on text editors.

# Requirements

## Week 1

During this week, you will not be working on your own text editor, but
rather on the editor belonging to the student with the uNID that is
the next higher one in lexical order, among the students enrolled in
the class. Your assignment is to implement a significant new feature
in this text editor. The feature that you choose should be one of
those we listed for Assignment 1, that the code owner did not choose
to implement. If the code owner implemented all of the features in the
list, then you should propose a significant new feature (and it is
fine to ask John and Pavel for ideas).

By the end of this week, you will have submitted a pull request to the
repository containing the editor that you added your feature to. The
pull request should include a reasonable collection of tests for the
new feature. Also, you must not break any of the existing tests that
are in the repository.

## Week 2

During this week, each of you will provide a code review for two
different pull requests. First, you will review the pull request
that a different student in the class has made to your repository.
Second, you will review 

## Week 3

# Submission

Push your work [to Github](https://github.com/utah-cs3960-sp26) and
name your repository `textedit-uXXXXXXX`. You must create a
`README.md` file in this repository with release notes. You will make
three releases:

- By 9 Jan, describe your first release under the "R1" heading in `README.md`
- By 16 Jan, describe your second release under the "R2" heading in `README.md`
- On 21 Jan, demo your text editor in class
- By 23 Jan, describe your third / final release under a "R3" heading in `README.md`

You will be graded based on the in-class demo, the release notes, and
based on the final product.

# Writing Release Notes

Organize your release notes by feature, using the features we
mentioned above. For example, "opening and saving files" is a feature.
Things that you should talk about include:

1. What about the feature works and doesn't work
2. Brag about the feature a little bit -- tell us something about how
   you approached it, how you solved it, or some interesting bit of
   your software architecture
3. How does this feature fit into the modular structure of your editor?
4. For the parts that work, explain how you know that they work as intended.
   other words, explain what kind of tests you are using to validate
   the functionality of your editor.

You don't need to write a ton; one or two paragraphs is enough. These
should be English text, using complete sentences. Include screenshots
to brag about what you've done. All the releases go in one document;
use headings "R1", "R2", and "R3" to separate them.

# Demo Day

Show up ready to run your text editor. The instructors will walk
between the tables and ask you to do various things like:

- Doing some sequence of operations to see what happens (say, what
  happens if you open a different file and then press undo)
- Answer questions about your implementation decisions (for multi-file
  support, what data structure stores the set of open files)
- Show off particular features (what format do you use for describing
  syntax highlighting definitions)
- Talk through design choices (what features does your file tree
  explorer support and which did you discard?)

Expect to spend a few minutes demoing your text editor. This will
count toward your grade.
