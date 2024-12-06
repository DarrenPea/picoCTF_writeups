# flag_shop

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

We made a lot of substitutions to encrypt this. Can you decrypt it? Connect with nc jupiter.challenges.picoctf.org 39894.

## Approach

It appears that the text is being encrypted using substituition cipher. I have created a script, `script.py` to obtain the plaintext.

Firstly, I replaced each letter based on a frequency analysis, aligned with the frequency of each letter in the English Corpus. After that, I analysed the texts and made fine tune adjustments, for example, 1 letter words would most likely be 'i' or 'a', etc.

After running the script, the plaintext is saved in `solution.txt` and the flag is obtained.

## Flag

`picoCTF{frequency_is_c_over_lambda_agflcgtyue}`