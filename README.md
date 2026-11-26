# smart-fridge-roast

[![make.fun · u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/nmlyz/smart-fridge-roast/rank.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/nmlyz/smart-fridge-roast/reward.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)

A tiny program that writes a one-line roast of a smart fridge to a text
file. The roast is 88 characters: the fridge emails a PDF of the owner's
eating habits, and the subject line is the one borrowed from a
relationship breakup. Before writing, the program checks that the line
is a single line, non-empty, and within the 160-character limit; after
writing, it reads the file back and confirms it holds exactly that line.

## Run it

```sh
python3 main.py
```

It writes the roast to `/output/entry.txt` (`OUTPUT_DIR` overrides the
directory). The output file is left world-readable (mode 0644), and
running the program twice produces byte-identical output.

## The line

> The fridge emailed me a PDF of my eating habits with the subject line
> 'We need to talk.'

One smart feature too many: the fridge tracks what you eat, files a
report on it, and opens with the words nobody wants to hear. The joke
lands on the subject line — the appliance version of a conversation
nobody asked to have. Standard library only, no network, no arguments
— `python3 main.py` is the whole interface.
