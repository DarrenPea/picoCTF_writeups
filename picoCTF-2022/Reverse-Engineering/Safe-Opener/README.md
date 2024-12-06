# Safe Opener

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you open this safe?
I forgot the key to my safe but this [program](https://artifacts.picoctf.net/c/83/SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe? <br>
Put the password you recover into the picoCTF flag format like: <br>
`picoCTF{password}`

## Approach

Analysing the Java program, it seems that the password is Base-64 encoded, before comparing if it is equivalent to `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`.

Using [Cyberchef](https://cyberchef.net/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Y0d3ellYTXpYMnd6ZEY5dE0xOHhiblF3WDNSb00xOXpZV1l6), I Base-64 decoded the string and obtained `pl3as3_l3t_m3_1nt0_th3_saf3`.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Reverse-Engineering/Safe-Opener/img/flag.png" />
</p>

## Flag

`picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`