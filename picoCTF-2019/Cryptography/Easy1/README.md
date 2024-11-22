# Easy1

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this [table](https://jupiter.challenges.picoctf.org/static/1fd21547c154c678d2dab145c29f1d79/table.txt) to solve it?.

## Approach

Using the table, to find the intersections between each character of the flag and `SOLVECRYPTO`, which should correspond to `UFJKXQZQUNB`, I obtained `CRYPTOISFUN`.

## Flag

`picoCTF{CRYPTOISFUN}`