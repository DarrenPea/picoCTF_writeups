# Transformation

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

I wonder what this really is... [enc](https://mercury.picoctf.net/static/77a2b202236aa741e988581e78d277a6/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

## Approach

The encryption script is provided to us. 

It can be seen that it looks at every pair of characters in the flag. Since each character falls within `chr(256)`, which is equivalent to 8 bits, the left shift of `ord(flag[i])` by 8 bits will preserve `ord(flag[i])` in the first 8 bits of each new character while `ord(flag[i + 1])` will be preserved in the last 8 bits of each new character, so I extracted out `flag[i]` and `flag[i + 1]` from each character and obtained the flag.

## Flag

`picoCTF{16_bits_inst34d_of_8_75d4898b}`