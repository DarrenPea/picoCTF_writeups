# Flags

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

What do the [flags](https://jupiter.challenges.picoctf.org/static/fbeb5f9040d62b18878d199cdda2d253/flag.png) mean?

## Approach

After viewing the picture, it appears that each flag represents a letter. Upon searching, I came across nautical flags, which seem to match the flags in the image.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2019/Cryptography/Flags/img/flag.png" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2019/Cryptography/Flags/img/Nautical-Flag-Alphabet.png" />
</p>

Hence, I obtained `picoCTF{f-ag-and-tuff}`

Performing a reverse image search on the remaining flags that are not decoded, I found it corresponded to `1` and `5`, so the final flag is `picoCTF{f1ag5and5tuff}`

## Flag

`picoCTF{f1ag5and5tuff}`