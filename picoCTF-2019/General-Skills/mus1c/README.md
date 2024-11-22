# mus1c

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

I wrote you a [song](https://jupiter.challenges.picoctf.org/static/c0863a3b0170d6dd176be3a595b4b75e/lyrics.txt). Put it in the picoCTF{} flag format.


## Approach

The file provided, `lyrics.txt`, appears to be programmed in the rockstar programming language. Running the lyrics [here](https://web.archive.org/web/20190522020843/https://codewithrockstar.com/online), I obtained:

```
114 114 114 111 99 107 110 114 110 48 49 49 51 114
```

This appears to be in decimal, so I decoded it to ASCII and obtained `rrrocknrn0113r`

## Flag

`picoCTF{rrrocknrn0113r}`