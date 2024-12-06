# basic-mod2

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

A new modular challenge! <br>
Download the message [here](https://artifacts.picoctf.net/c/178/message.txt). <br>
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. <br>
Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)


## Approach

To find the modular inverse of `x`, let the modular inverse be `y`. The following must be satisfied:

```py
(x * y) % mod == 1		## in this case, mod = 41 and x, y < mod
```

I have written `script.py` to solve this problem.

## Flag

`picoCTF{1nv3r53ly_h4rd_c680bdc1}`