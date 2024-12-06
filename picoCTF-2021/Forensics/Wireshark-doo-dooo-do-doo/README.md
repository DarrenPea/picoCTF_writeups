# Wireshark doo dooo do doo...

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/b44842413a0834f4a3619e5f5e629d05/shark1.pcapng).

## Approach

Upon analysing the file, I noticed there is something suspicious in TCP stream 5.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2021/Forensics/Wireshark-doo-dooo-do-doo/img/stream_5.png" />
</p>

It seems like the flag could be encrypted using a shift cipher so I used [dCode](https://www.dcode.fr/caesar-cipher) to decrypt the text.

## Flag

`picoCTF{p33kab00_1_s33_u_deadbeef}`