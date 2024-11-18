# like1000

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

This [.tar file](https://jupiter.challenges.picoctf.org/static/52084b5ad360b25f9af83933114324e0/1000.tar) got tarred a lot.


## Approach

I first tried extracting the file, and realised it never ends, 1000.tar, 999.tar, 998.tar...

So, I decided to write a script, `script.py`, to automate the recursive extraction of the tar files, to finally obtain the flag.

## Flag

`picoCTF{l0t5_0f_TAR5}`