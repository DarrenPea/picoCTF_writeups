# basic-mod1

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

We found this weird message being passed around on the servers, we think we have a working decryption scheme. <br>
Download the message [here](https://artifacts.picoctf.net/c/129/message.txt). <br>
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. <br>
Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Approach

I have written `script.py`, which will find every number mod 37, before mapping them to their respective characters based on their values and print out the decrypted message.

## Flag

`picoCTF{R0UND_N_R0UND_ADD17EC2}`