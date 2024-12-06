# strings it

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you find the [flag](https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings) in file without running it?

## Approach

Usings `strings` to search for data inside the file, I found the flag.

```
└─$ strings strings | grep "picoCTF{"
picoCTF{5tRIng5_1T_827aee91}
```

## Flag

`picoCTF{5tRIng5_1T_827aee91}`