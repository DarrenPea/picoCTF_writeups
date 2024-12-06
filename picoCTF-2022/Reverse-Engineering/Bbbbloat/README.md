# Bbbbloat

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you get the flag? <br>
Reverse engineer this [binary](https://artifacts.picoctf.net/c/47/bbbbloat).

## Approach

Using Ghidra to decompile the binary, there seems to be a comparison operation after it retrieves my input for a favorite number. This can be seen from `__isoc99_scanf(&DAT_00102020, &local_48)`, which is located 2 lines after the `printf` statement.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Reverse-Engineering/Bbbbloat/img/key.png" />
</p>

After storing our input in `&local_48`, it comprares it with `0x86187`, which is `549255`. If it is not equivalent, then it will return us "Sorry, that\'s not it!". Hence, the favorite number is `549255`.

## Flag

`picoCTF{cu7_7h3_bl047_44f74a60}`