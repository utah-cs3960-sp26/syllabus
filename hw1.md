CS 3960 Homework 1
------------------

Status: *draft* \
Due: 23 Jan

In this homework assignment you will build a text editor. The exact
architecture, UI, implementation, and features are up to you, but
remember to execute with taste and aim for quality and polish.

# Requirements

You must build a native, cross-platform text editor using the Qt
framework in Python. Do *not* use libraries outside Qt that already
provide these features. Besides core features (like editing,
selection, opening and saving files, and so on) you must select and
implement at least two of the following:

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
name your repository `textedit-uXXXXXXX`. You will make three
releases:

- By 9 Jan, push `v1.md` describing your first release
- By 16 Jan, push `v2.md` describing your second release
- On 21 Jan, demo your text editor in class
- By 23 Jan, push `v3.md` describing your third release

Each release's notes should be one or two paragraphs long and include
screenshots to demonstrate new features.

# Writing Release Notes

Your release notes should be organized around features. For this
assignment, the required features are those in the bulleted list
above.

For each feature, you should write about:

- What about the feature works and doesn't work
- Brag about the feature a little bit -- tell us something about how you approached it, how you solved it, or some interesting bit of your software architecture
- How does this feature fit into the modular structure of your editor?
- For the parts that work, explain how you know that they work. In other words, explain what kind of tests

Write up your release notes as English text, using full sentences, and
push it to the root directory of your repository using the appropriate
file name.


