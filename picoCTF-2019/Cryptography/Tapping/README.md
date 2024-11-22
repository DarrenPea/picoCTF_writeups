# Tapping

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Theres tapping coming in from the wires. What's it saying `nc jupiter.challenges.picoctf.org 9422`.

## Approach

```
$ nc jupiter.challenges.picoctf.org 9422
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ....- -.... .---- ----- }
```

The flag appears to be represented in morse code. Decoding the flag, I obtained `picoCTF{m0rs3c0d31sfun2683824610}`

## Flag

`picoCTF{m0rs3c0d31sfun2683824610}`