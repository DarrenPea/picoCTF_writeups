# 1_wanna_b3_a_r0ck5tar

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

I wrote you another [song](https://jupiter.challenges.picoctf.org/static/96904d361d61fada5bd2d13536706f9a/lyrics.txt). Put the flag in the picoCTF{} flag format

>The Rockstar language has changed since this problem was released! Use this Wayback Machine URL to use an older version of Rockstar, [here](https://web.archive.org/web/20190522020843/https://codewithrockstar.com/online).

## Approach

Pasting the lyrics into the website, it prompts for an input when running the code.

### Analysis of code

`Listen to the music` and `Listen to the rhythm` are reading inputs from `STDIN` and storing it in `music` and `rhythm` respectively.

`A guitar is a six-string` can be read as initialising `a guitar` with `136`. <br>
`Music is a billboard-burning razzmatazz!` can be read as initialising `Music` with `1970`.

`If the music is a guitar` is an if-statement that checks if `music` is `136`. <br>
`If the rhythm without Music is nothing` is an if-statement that checks if `Music` is subtracted from `rhythm` is equivalent to 0.

Inputting `136` and `1970`, the output is obtained.

```
Keep on rocking!
66
79
78
74
79
86
73
```

Converting the numbers from decimal to ASCII, `BONJOVI` is obtained.

## Flag

`picoCTF{BONJOVI}`