# unpackme.py

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you get the flag?
Reverse engineer this [Python program](https://artifacts.picoctf.net/c/48/unpackme.flag.py).

## Approach

I added a `print` statement before the `exec` function. This allowed me to check what was being executed.

```py
pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_5274ff21}')
else:
  print('That password is incorrect.')
```

As seen, the password of the program would be `batteryhorse`, and the flag will be printed out.

## Flag

`picoCTF{175_chr157m45_5274ff21}`