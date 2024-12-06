# morse-code

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Morse code is well known. Can you decrypt this? <br>
Download the file [here](https://artifacts.picoctf.net/c/79/morse_chal.wav). <br>
Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.

## Approach

We are first provided with `morse_chal.wav`. Upon opening the `.wav` file using `audacity`, it seems that it is written in morse code.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Cryptography/morse-code/img/morse.png" />
</p>

Reading the morse code, I obtained the following:

```
.-- .... ....- --...   .... ....- --... ....   ----. ----- -..   .-- ..--- ----- ..- ----. .... --...
```

Using a [morse code translator](https://morsecode.world/international/translator.html), I obtained the words `WH47 H47H 90D W20U9H7`.

## Flag

`picoCTF{WH47_H47H_90D_W20U9H7}`