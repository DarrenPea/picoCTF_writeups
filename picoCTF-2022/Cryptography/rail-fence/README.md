# rail-fence

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it? <br>
Download the message [here](https://artifacts.picoctf.net/c/188/message.txt). <br>
Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}.

## Approach

From the challenge description, the ciphertext should be encoded using the rail fence cipher with 4 rails.

Using [Cyberchef](https://cyberchef.net/#recipe=Rail_Fence_Cipher_Decode(4,0)&input=VGEgXzdONkQ0OWhsZzpXM0RfSDNDMzFOX19BOTdlZiBzSFIwNTNGMzhONDNEN0IgaTMzX19fTjY), I decoded the rail fence cipher with key length 4 and offset 0, and obtained the flag.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Cryptography/rail-fence/img/flag.png" />
</p>

## Flag

`picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997}`