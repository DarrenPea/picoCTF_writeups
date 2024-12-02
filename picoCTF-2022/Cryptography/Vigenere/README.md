# Vigenere

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you decrypt this message?
Decrypt this [message](https://artifacts.picoctf.net/c/159/cipher.txt) using this key "CYLAB".

## Approach

From the challenge name and description, this cipher appears to be encrypted using the Vigenere cipher with key 'CYLAB'.

Using [Cyberchef](https://cyberchef.net/#recipe=Vigen%C3%A8re_Decode('CYLAB')&input=cmdub0RWRHtPME5VX1dRM19HMUczTzNUM19BMUFIM1NfZjg1NzI5ZTd9&ieol=CRLF&oeol=CRLF), I obtained the flag in plaintext.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Cryptography/Vigenere/img/flag.png" />
</p>

## Flag

`picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_d85729g7}`