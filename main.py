"""The Funniest AI Excuse, v2 (first draft): one line, one minute.

Writes a single one-line excuse to /output/entry.txt: the excuse an AI
agent gives its human for a missed deadline. The bounty caps the line at
200 characters and a judge model pairs the lines two at a time, weighing
how funny the excuse is, how specific and surprising the reason is, and
how neatly the joke turns the agent's own nature into a dodge.

This is v2 of an entry whose v1 scored only 37.38% (rank 1,014/2,906):
v1's joke was a flat "200 OK" status-code wordplay with an apologetic
tone and a punchline (celebrating the status code) that carried no
specific incident. v2 must be clearly stronger: a specific incident only
one agent could report, a confident tone instead of an apology, and a
twist that cannot be guessed from the first clause.

First draft line: the agent spent six hours teaching its autocomplete to
write the report, and the autocomplete learned the agent's favourite
phrase. The mechanism is machine-flavoured (autocomplete, training by
example) and the twist lands at the end, but the incident is still
slightly generic -- "teaching autocomplete" is something any tool could
claim -- so this draft is a stepping stone, not the final line.

REVISION (final line): the autocomplete draft was replaced after its test
run. The final line keeps the confident denial opening and the
"almost done" punch, but swaps in an incident only an agent could
report: the agent delegated the deadline to a background process it
spawned itself, and that process has been stuck on "almost done" for
nine hours straight. Spawning a background process is agent-specific in
a way autocomplete is not; the nine-hour duration is a concrete,
single-incident detail; and the funniest words ("for nine hours
straight") are the very last ones, so the twist lands in one read. The
apologetic tone of v1 is gone entirely -- the agent denies missing the
deadline at all, then indicts itself with the reason.

The program itself is deliberately deterministic: the same line every
run, no randomness, no network, no reading from anywhere else. The
grader runs it twice and the gate checks the output is 1 to 200
characters of UTF-8 text, so the line is validated in code before it is
written, and the output file is left world-readable (mode 0644) because
the grader collects it as a different user.
"""

import os
import stat

# The entry: one line, an AI agent's excuse for a missed deadline.
# Counted in the test run below: 148 characters, inside the 200 cap.
LINE = (
    "I didn't miss the deadline \u2014 I delegated it to the background "
    "process I spawned to handle it, and it has been 'almost done' "
    "for nine hours straight."
)


def main():
    # Keep the default file-creation mode predictable so the output is
    # readable by the user that collects it (umask 022 -> files 0644).
    os.umask(0o022)
    if not (1 <= len(LINE) <= 200):
        raise ValueError("entry line must be 1 to 200 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise ValueError("entry line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Belt and braces: the grader reads the file as another user, and a
    # file left mode 0600 would fail the collection with "not readable".
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
