# Transformation

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

[crackme.py](https://mercury.picoctf.net/static/8fc4e878bd6708031d67cb846f03c140/crackme.py)

## Approach

Looking through `crackme.py`, it seems that the flag used ROT47 cipher to hide the flag, while the file only calls the `choose_greatest` function.

Hence, I replaced the `choose_greatest` function with `decode_secret` function, and passed the secret into it to obtain the flag.

## Flag

`picoCTF{1|\/|_4_p34|\|ut_a79b6c2d}`