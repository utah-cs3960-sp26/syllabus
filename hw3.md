CS 3960 Homework 3
------------------

Status: final \
Due: 6 Mar

In this assignment you will make your text editor fast.

# Requirements

First make sure your text editor has a find-and-replace feature. Most
students implemented one at some point, but if not, the actual UI can
be simple; you only need single-file string find-replace. To be
specific, you only need "replace all". Make sure it's accessible with
Ctrl-F and make it sure it shows the number of matches / replacements.

## Week 8

Add a frame timer to your text editor; it should show the last,
average, and max frame timings, and it should subtract idle time.
Make Ctrl-P show/hide it. Make sure it does not time while it is
hidden, and that the frame timings reset when you hide the widget.
We'll need that to time different editor actions.

Frame timers measure how long it takes the editor to respond to a user
action. Verify that yours works: open your editor with an empty file
and open the frame timer. It should show timings far below 16ms,
probably a few milliseconds; if you see timings of about 500ms on an
empty file, your frame timer probably isn't handling idle frames
correctly. (In this case, your editor is probably redrawing every
500ms in order to blink the cursor, but it *could* redraw much faster
if it wanted to, like if the user was interacting with it.)

Most GUI applications target frame timings of 16ms or 60Hz; newer
displays even target 8ms or 120Hz. Our goal in this assignment will be
to get as close as possible to this target for all user actions in our
editor, but we'll specifically test file opening, scrolling, and
find-replace. How hard this is will depend on what other features
you've implemented in your editor. If you've implemented, say, rich
text editing, then you might need to add fast-paths when that is not
in use.

We will be testing your editor's performance on three files:

 - [`small.txt`][small] is a few hundred lines long
 - [`medium.txt`][medium] is ten thousand lines long
 - [`large.txt`][large] is over a million lines long, and some of
   those lines are thousands of characters long.
 
[small]: https://pavpanchekha.com/cs3960/small.txt
[medium]: https://pavpanchekha.com/cs3960/medium.txt
[large]: https://pavpanchekha.com/cs3960/large.txt

Don't check these files into your Git repository, they are too large.
Github will reject them.

All of the files use a lot of Python keywords, though they're not
really Python code per se. Files like `large.txt` are rare, but they
do happen: log files, disk dumps, packed files, hex dumps, and similar
all occur every now and then.

Open each of the three files. For each file, record:

- The maximum frame time when you open the file.
- The maximum frame time as you scroll up and down. Try
  to scroll a few hundred lines quickly using your touchpad or mouse.
- The maximum and average frame times when you click far away from the
  current location in the scroll bar.
- The maximum frame time if you try to replace "while" with "for".
  There should be 19 matches in `small.txt`, 1 186 in `medium.txt`,
  and 668 753 in `large.txt`
- The total memory used by your text editor process, which you can
  measure using "Task Manager" or "Activity Monitor" or your system's
  equivalent. Specifically look for a "Physical" or "Real" memory
  measure, not "Virtual". For the largest file it should be 1-3GiB.

Make sure to confirm that the number of matches when finding and
replacing is correct.

If your text editor can't load `large.txt` after a few minutes, you
don't have to time scrolling and find-replacing for it. If you think
you got an outlier measurement you can try again and take the lowest.

Record your results in a file called `TIMING.md` in the root of your
repository, and clearly label them as your initial timings.

Once done, make it possible to open, scroll, and find-replace
`large.txt` in under a minute. This could require a substantial amount
of work; feel free to discuss with your AI. If memory usage grows past
3GiB for the largest file, that's one place to start.

By the due date (5pm on Friday Feb 27), re-record the timings in
`TIMING.md`. Keep the initial timings in the document as well. Clearly
label which is which. Write a paragraph (clearly labeling it Week 8)
describing what changes you had to make and your current editor
architecture.

## Week 9

Do the same as above, but now we want to hit good frame times, not a
minute. The ideal times are 16ms for each action on each file. Any
frame that takes more than 16ms is a "dropped" frame and we want as
few of those as possible.

In some cases, that might not be possible---opening a file, for
example, probably uses your system file picker. You need to account
for every dropped frame: what's the code that drops the frame, why
does it take so long, and why can't you fix it. Make sure your answers
are consistent across file sizes. For example, if you think the system
file picker drops two frames, you'd expect that to happen the same way
with all three sizes.

You may need to use additional libraries and further change your
architecture to minimize dropped frames, but list every library used
and describe why you use it. Be wary of multi-threading, which makes
tricky mistakes easy to make. If you must use multi-threading, like
for indexing, use it in limited ways with a simple lock discipline.
Make sure you are still getting the correct number of matches after
any optimizations you perform.

By the due date (5pm on Friday Mar 6), add your Week 9 timings to
`TIMING.md`, keeping existing timings and labeling everything clearly.
Write a paragraph (clearly labeling it Week 9) describing what changes
you had to make and your current editor architecture. Then list every
dropped frame across the experiments above (you can group them if you
think it's best) and explain why those frames are dropped and why you
can't fix it.

# Submission

See instructions in the individual weeks.

# Demo Day

TBD
