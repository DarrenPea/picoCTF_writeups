# Safe Opener 2

- [Description](#description)
- [Alternate solution](#alternate-solution)
- [Approach](#approach)
- [Flag](#flag)

## Description

What can you do with this file? <br>
I forgot the key to my safe but this [file](https://artifacts.picoctf.net/c/286/SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

## Alternate solution

Looking at the possible strings present in the file using `strings`, I obtained the flag.

```
$ strings SafeOpener.class | grep picoCTF
,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_3dae8463}
```

## Approach

Using Ghidra to decompile the file, 

## Flag

`picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_3dae8463}`