# WhitePages

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

I stopped using YellowPages and moved onto WhitePages... but [the page they gave me](https://jupiter.challenges.picoctf.org/static/95be9526e162185c741259a75dffa0ab/whitepages.txt) is all blank!

## Approach

Upon opening `whitepages.txt` in a hex editor, I noticed there were only 2 different kinds of value, `.` and ` `, which corresponds to `b'\xe2\x80\x83` and `b'\x20'`.

Thinking about how a flag can be hidden using only 2 different kinds of value, I thought the flag could possible be represented in binary. So, I tried to replace `.` with `0` and ` ` with `1` using `script.py` and obtained the flag.

## Flag

`picoCTF{not_all_spaces_are_created_equal_7100860b0fa779a5bd8ce29f24f586dc}`