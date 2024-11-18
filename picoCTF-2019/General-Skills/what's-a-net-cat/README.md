# what's a net cat?
- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Using netcat (nc) is going to be pretty important. Can you connect to `jupiter.challenges.picoctf.org` at port `25103` to get the flag?

## Approach

As the challenge suggests, I used netcat to obtain the flag.

```
└─$ nc jupiter.challenges.picoctf.org 25103
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_d0c64587}
```

## Flag

`picoCTF{nEtCat_Mast3ry_d0c64587}`