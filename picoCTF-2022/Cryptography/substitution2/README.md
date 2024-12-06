# substitution2

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

It seems that another encrypted message has been intercepted. The encryptor seems to have learned their lesson though and now there isn't any punctuation! Can you still crack the cipher?
Download the message [here](https://artifacts.picoctf.net/c/112/message.txt).

## Approach

Using a [frequency analysis tool](https://www.101computing.net/frequency-analysis/), I tried to form the word 'The flag is: picoCTF'.

I then tried piecing out the rest of the text using common English words.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Cryptography/substitution2/plaintext.png" />
</p>

## Flag

`picoCTF{N6R4M_4N41Y515_15_73D10U5_8E1BF808}`