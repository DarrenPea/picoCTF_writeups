# Mod 26

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}`

## Approach

As the description suggest, the flag could be encrypted using the ROT13 cipher, where each letter is shifted by 13 places.

Using [dCode](https://www.dcode.fr/rot-13-cipher), I managed to obtain the flag.

## Flag

`picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag}`