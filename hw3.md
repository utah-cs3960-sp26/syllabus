CS 3960 Homework 3
------------------

Status: draft \
Due: 13 Mar

In this assignment you will make your text editor fast.

# Requirements

First make sure your text editor has a find-and-replace feature. Most
students implemented one at some point, but if not, the actual UI can
be simple; we only need single-file find-replace for strings. Make
sure it's accessible with Ctrl-F and make it sure it shows the number
of matches / replacements.

## Week 8

Add a frame timer to your text editor; there's a built-in Qt widget.
Make Ctrl-P show/hide it. Make sure it does not time while it is
hidden, and that the frame timings reset when you hide the widget.
We'll need that to time different editor actions.

Frame timers measure how long it takes the editor to respond to a user
action. Most GUI applications target frame timings of 16ms or 60Hz;
newer displays even target 8ms or 120Hz. In this class we'll target a
16ms or 60Hz.

We will be testing your editor's performance on three files:

 - `small.txt` is a few hundred lines long
 - `medium.txt` is ten thousand lines long
 - `large.txt` is over a million lines long, and some of those
   lines are thousands of characters long.

All of the files use a lot of Python keywords, though they're not
really Python code per se. Files like `large.txt` are rare, but they
do happen: log files, disk dumps, packed files, hex dumps, and similar
all occur every now and then.

You can download these files from [this repository](../data/) but
don't check them into your Git repository, they are too large.

Open each of the three files. For each file, record:

- The time it takes to open the file, specifically the time between
  pressing the "Select" or similar button on the file picker and the
  time that the editor is usable again.
- The maximum and average frame times as you scroll up and down. Try
  to scroll a few hundred lines quickly using your touchpad or mouse.
- The maximum and average frame times when you click far away from the
  current location in the scroll bar.
- The maximum and average frame times if you try to replace "while"
  with "for". There should be 19 matches in `small.txt`, 1 186 in
  `medium.txt`, and 2 720 995 in `large.txt`
- The total memory used by your text editor process, which you can
  measure using "Task Manager" or "Activity Monitor" or your system's
  equivalent. Specifically look for a "Physical" or "Real" memory
  measure, not "Virtual". For the largest file it should be 1-3GiB.

If your text editor can't load `large.txt` after a few minutes, you
don't have to time scrolling and find-replacing for it. Make sure to
confirm that the number of matches is correct.

Record your results in a file called `TIMING.md` in the root of your
repository, and clearly label them as your initial timings.

Once done, make it possible to open, scroll, and find-replace
`large.txt` in under a minute. This could require a substantial amount
of work; feel free to discuss with your AI. Consider subclassing Qt's
`QAbstractScrollArea`. If you see memory usage grow past 3GiB for the
largest file, that's one place to start.

By the due date (5pm on Friday Feb 27), re-record the timings in
`TIMING.md`. Keep the initial timings in the document as well. Clearly
label which is which. Write a paragraph (clearly labeling it Week 8)
describing what changes you had to make and your current editor
architecture.

## Week 9

Do the same as above, but now bring your frame timings below 1 second,
except for find-replace on `large.txt`, which should be under a minute
but can be longer than 1 second. You may need to use the `mmap`
library. Be wary of multi-threading, which makes tricky mistakes easy
to make. If you must use multi-threading, like for indexing, use it in
limited ways with a simple lock discipline.

By the due date (5pm on Friday Mar 6), add your Week 9 timings to
`TIMING.md`, keeping existing timings and labeling everything clearly.
Write a paragraph (clearly labeling it Week 9) describing what changes
you had to make and your current editor architecture.

## Week 10

Do the same as above, but now bring your frame timings below 16ms,
including for find-replace on `large.txt`. You may need to learn more
about the Qt event loop and perform expensive operations like
find-replace in multiple smaller chunks. Make sure you are still
getting the correct number of matches.

By the due date (5pm on Friday Mar 13), add your Week 10 timings to
`TIMING.md`, keeping existing timings and labeling everything clearly.
Write a paragraph (clearly labeling it Week 10) describing what
changes you had to make and your current editor architecture.

# Submission

See instructions in the individual weeks.

# Demo Day

TBD
