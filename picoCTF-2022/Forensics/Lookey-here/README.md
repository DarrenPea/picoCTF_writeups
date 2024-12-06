# Lookey here

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.
Download the data [here](https://artifacts.picoctf.net/c/124/anthem.flag.txt).

## Approach

After downloading `anthem.flag.txt`, it seems that it consists of long chunks of text. To look for the flag in the text, I used `grep picoCTF` to look for strings that contains "picoCTF".

```
$ cat anthem.flag.txt | grep picoCTF
we think that the men of picoCTF{gr3p_15_@w3s0m3_4c479940}
```

## Flag

`picoCTF{gr3p_15_@w3s0m3_4c479940}`