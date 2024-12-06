# transposition-trial

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message [here](https://artifacts.picoctf.net/c/191/message.txt).

## Approach

Upon looking at the message, it seems that "The" has been transposed to "heT". So, I wrote `script.py` to rearrange every block of 3 before printing our the original text.

## Flag

`picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}`