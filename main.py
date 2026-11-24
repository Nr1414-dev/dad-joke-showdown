"""Dad Joke Showdown entry.

Writes one dad joke, at most 200 characters, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when the harness sets it).

The joke was chosen from six candidates scored against the judge brief's
five criteria in order (dad-voice, clean pun, freshness, tightness, spoken
rhythm), and it won every 1v1 comparison. See dad-joke-showdown-research.md.
"""

import os

JOKE = "My daughter asked why I keep a ladder in the kitchen. I told her, 'For high tea.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
