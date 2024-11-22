# flag_shop

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

There's a flag shop selling stuff, can you buy a flag? [Source](https://jupiter.challenges.picoctf.org/static/253c4651d852ac6342752ff222cf2a83/store.c). Connect with nc jupiter.challenges.picoctf.org 9745.

## Approach

In this challenge, we need to purchase the actual flag for 100000 dollars, but we only have 1100 dollars. Looking through the source code, I noticed `total_cost` and `number_flags` are initialised as signed integers and

```c
total_cost = 900*number_flags;
```

There could be a integer overflow, resulting in total_cost being negative, which would allow me to earn money and obtain 100000 dollars to purchase the flag.

```
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
222222222

The final cost is: -1863463112

Your current balance after transaction: 1863464212
```

## Flag

`picoCTF{m0n3y_bag5_65d67a74}`