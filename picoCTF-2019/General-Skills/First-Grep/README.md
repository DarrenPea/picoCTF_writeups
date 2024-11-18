# First Grep

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/515f19f3612bfd97cd3f0c0ba32bd864/file)? This would be really tedious to look through manually, something tells me there is a better way.

## Approach

Instead of reading the file manually, I used grep.

```
└─$ grep "picoCTF{" file
picoCTF{grep_is_good_to_find_things_5af9d829}
```

## Flag

`picoCTF{grep_is_good_to_find_things_5af9d829}`