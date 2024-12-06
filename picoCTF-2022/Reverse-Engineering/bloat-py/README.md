# bloat.py

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you get the flag?
Run this [Python program](https://artifacts.picoctf.net/c/103/bloat.flag.py) in the same directory as this [encrypted flag](https://artifacts.picoctf.net/c/103/flag.txt.enc).

## Approach

When running `bloat.flag.py`, it asks for a password to retrieve the flag. Looking at the code, it seems that every character is being retrieved by using indexes based on the variable `a`. 

We can see that the function `arg232()` returns an `input()` function, so it is responsible for retrieving our password input.

```py
def arg232():
  return input(a[47]+a[75]+a[68]+a[64]+a[82]+a[68]+a[94]+a[68]+a[77]+a[83]+\
a[68]+a[81]+a[94]+a[66]+a[78]+a[81]+a[81]+a[68]+a[66]+a[83]+\
a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+a[81]+a[67]+a[94]+\
a[69]+a[78]+a[81]+a[94]+a[69]+a[75]+a[64]+a[70]+a[25]+a[94])
```

Let's see where this function is called below. It stores our input in `arg432` and passes it through `arg133()`.

```py
arg432 = arg232()
arg133(arg432)
```

Looking at `arg113()` function, it is evident that it is reponsible for checking whether we have written the correct password. Since we have the program, I can print out the value of the correct password.

```py
def arg133(arg432):
  print(a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68])
  if arg432 == a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]:
    return True
```

Upon running the program, I see that "happychance" is printed out, so I provided it as my input and obtained the flag.

## Flag

`picoCTF{d30bfu5c4710n_f7w_b8062eec}`