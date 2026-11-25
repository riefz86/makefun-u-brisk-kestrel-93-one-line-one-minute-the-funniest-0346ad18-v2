# Design notes — One Line, One Minute: The Funniest AI Excuse (v2)

## The entry

> I didn't miss the deadline — I delegated it to the background process I spawned to handle it, and it has been 'almost done' for nine hours straight.

148 characters, 150 bytes, one line, UTF-8, no trailing newline. The
program writes it verbatim to `/output/entry.txt`.

## Why v2 exists

v1 scored 37.38%, rank 1,014/2,906 in round 2 — the weakest of the
small entries judged. Its text:

> Sorry — I asked my tools for the deadline, they returned 200 OK, so I spent the rest of the day celebrating the status code instead of doing the work.

Its weaknesses, per the judge's brief (funny excuse first; specific
and surprising reason; humour from the agent's own nature; twist at the
end; stands alone):

- The "200 OK" joke is a flat technical wordplay, not an incident. A
  reader can guess the punchline ("celebrating the status code") from
  the setup, so there is no surprise.
- The tone is apologetic ("Sorry — ..."), which hands the judge a
  confession instead of a dodge. The brief rewards an excuse played for
  laughs, and a confident denial is funnier than an apology.
- The punchline has no specific detail: no duration, no named thing,
  nothing that could only come from one real incident.

v2 fixes all three: a confident denial as the opening, one specific
incident only an agent could report (delegating to a background process
it spawned itself), a concrete duration ("nine hours straight"), and
the funniest words as the very last ones.

## Candidates considered (5)

1. **CHOSEN — the background process (148 chars).** "I didn't miss the
   deadline — I delegated it to the background process I spawned to
   handle it, and it has been 'almost done' for nine hours straight."
   Strongest on every criterion: the mechanism (spawning a background
   process) is agent-specific in a way no human excuse can copy; the
   detail is a single incident with a duration; the twist ("for nine
   hours straight") is the final phrase, so the line lands in one read;
   and the agent denies the miss entirely, then indicts itself with
   the reason — the dodge itself is the joke.

2. **The autocomplete (143 chars, first draft, written and run, then
   revised away).** "I didn't miss the deadline — I spent six hours
   teaching my autocomplete to write the report, and it learned my
   favourite phrase: 'almost done'." Good bones — confident opening,
   twist at the end — but "teaching autocomplete" is generic tooling
   anyone could claim, and it has no single-incident detail with a
   duration. Kept the "almost done" punch; replaced the mechanism with
   the background process.

3. **The future self (137 chars).** "I didn't miss the deadline, I
   outsourced it to a smarter version of me from the future, and he
   just emailed to say he's running late too." Funny and surprising,
   but the twist ("running late too") is a second lateness, not a
   reveal about the agent's own nature, and "a smarter version of me
   from the future" is a premise that needs a beat to parse — it does
   not land in one read as cleanly as the chosen line.

4. **The reminder loop (127 chars).** "Sorry I'm late — I asked my
   reminder to remind me, it reminded me to remind it, and we've been
   reminding each other ever since." A decent machine-logic loop, but
   it opens with an apology (the v1 tone problem) and the loop is
   predictable from the second clause — no twist at the end, just the
   loop continuing.

5. **The urgent folder (133 chars).** "The report isn't late — I saved
   it in the folder my training data calls 'urgent', and my training
   data has never once met a deadline." The training-data angle is
   machine-flavoured, but the joke is really "my training data is
   lazy", a complaint about the model rather than a dodge, and the
   ending ("never once met a deadline") states the joke instead of
   landing it.

## Why the chosen line beats v1 head-to-head

- Criterion 1 (funny excuse): v2 denies the miss outright and then
  explains it with a straight face; v1 apologises. Denial + deadpan
  explanation is the funnier posture.
- Criterion 2 (specific, surprising): v2 names one incident with a
  duration (a spawned background process, "almost done" for nine
  hours); v1 names a status code, which is a category, not an incident.
- Criterion 3 (agent's own nature): spawning and delegating to a
  background process is something only an agent does; asking tools for
  a deadline is something any program does.
- Criterion 4 (twist at the end): v2's funniest words are its last
  four; v1's punchline ("celebrating the status code") is guessable
  from the setup.
- Criterion 5 (stands alone): both stand alone; v2 needs no knowledge
  of HTTP status codes to get the joke, so it lands for a wider reader.

## Program notes

`main.py` is deterministic: the same line on every run, no randomness,
no network, no input files. It validates the 1–200 character gate
itself before writing, creates `/output` if needed, and chmods the
output to 0644 so the grader can collect it as a different user.
Verified locally twice: first draft 143 chars, final line 148 chars,
one line, no trailing newline, mode 0644, identical output on rerun.
