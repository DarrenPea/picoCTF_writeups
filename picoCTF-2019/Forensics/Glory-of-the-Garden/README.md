# 13

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

This [garden](https://jupiter.challenges.picoctf.org/static/4153422e18d40363e7ffc7e15a108683/garden.jpg) contains more than it seems.

## Approach

Using `strings`, I found that the flag is hidden in the data of the image.

```
└─$ strings garden.jpg | grep "picoCTF{"
Here is a flag "picoCTF{more_than_m33ts_the_3y3657BaB2C}"
```

## Flag

`picoCTF{more_than_m33ts_the_3y3657BaB2C}`