# speeds and feeds

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

There is something on my shop network running at `nc mercury.picoctf.net 20301`, but I can't tell what it is. Can you?

## Approach

First, I saved the output of `nc mercury.picoctf.net 20301` to `output.txt`. Each line in `output.txt` seemed to look something like `G1X1.6552Y3.5862`.

Upon some research, it appears to be G-code, a language for CNC machines and 3D printers. I found a [website](https://ncviewer.com/) that allows me to execute G-code and obtained the flag.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2021/Reverse-Engineering/speeds-and-feeds/img/flag.png" />
</p>

## Flag

`picoCTF{num3r1cal_c0ntr0l_68a8fe29}`