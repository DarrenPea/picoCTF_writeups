# substitution0

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?
Download the message [here](https://artifacts.picoctf.net/c/152/message.txt).

## Approach

Using a [frequency analysis tool](https://www.101computing.net/frequency-analysis/), I tried to form the word 'The flag is: picoCTF'.

I then realised that the first word of the file is supposed to correspond to the alphabet from A-Z so I replaced each character and obtained the entire plaintext.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Cryptography/substitution0/plaintext.png" />
</p>

## Flag

`picoCTF{5UB5717U710N_3V0LU710N_59533A2E}`