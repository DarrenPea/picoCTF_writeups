# substitution1

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

A second message has come in the mail, and it seems almost identical to the first one. Maybe the same thing will work again.
Download the message [here](https://artifacts.picoctf.net/c/181/message.txt).

## Approach

Using a [frequency analysis tool](https://www.101computing.net/frequency-analysis/), I tried to form the word 'The flag is: picoCTF'.

I then tried piecing out the rest of the text using common English words.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Cryptography/substitution1/plaintext.png" />
</p>

## Flag

`picoCTF{FR3QU3NCY_4774CK5_4R3_C001_4871E6FB}`