# Obedient Cat

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag).

## Approach

Since the flag is in plain sight, I used `strings` to look for readable strings in the file and managed to obtain the flag.

```
$ strings flag
picoCTF{s4n1ty_v3r1f13d_2aa22101}
```

## Flag

`picoCTF{s4n1ty_v3r1f13d_2aa22101}`