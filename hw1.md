CS 3960 Homework 1
------------------

Status: final \
Due: 23 Jan

In this homework assignment you will build a text editor. The exact
architecture, UI, implementation, and features are up to you, but
remember to execute with taste and aim for quality and polish.

# Requirements

You must build a native, cross-platform text editor using the Qt
framework in Python. Use pytest for testing. Do *not* use other libraries
to provide the features below. Besides core features (like editing,
selection, opening and saving files, keyboard shortcuts, and so on)
you must select and implement at least two of the following:

- Automatic indentation and bracket and quote matching
- Multiple cursors and rectangular selection
- Custom fonts, colors, and keyboard shortcuts
- Multi-language syntax highlighting using static language definitions
- Find and replace, including multi-file find and replace
- Multi-file support, tabs, and split views
- A file tree explorer with collapsible folders
- Jump to definition with an indexing system

The assignment description is purposefully high-level. Draw
inspiration from other text editors or other students' prior releases
and iterate on your vision before implementing.

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
