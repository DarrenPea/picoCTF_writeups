# Mind your Ps and Qs

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/b9ddda080c56fb421bf30409bec3460d/values)

## Approach

Using [dCode's RSA cipher module](https://www.dcode.fr/rsa-cipher), I passed the values of `c`, `n`, and `e`, to obtain the flag in plaintext.

## Flag

`picoCTF{sma11_N_n0_g0od_73918962}`