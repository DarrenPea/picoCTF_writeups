# patchme.py

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you get the flag?
Run this [Python program](https://artifacts.picoctf.net/c/200/patchme.flag.py) in the same directory as this [encrypted flag](https://artifacts.picoctf.net/c/200/flag.txt.enc).

## Approach

When running `patchme.flag.py`, I was prompted for a password. Analysing the code in the Python file, there seems to be a check on the password value.

```py
user_pw = input("Please enter correct password for flag: ")
if( user_pw == "ak98" + \
				"-=90" + \
				"adfjhgj321" + \
				"sleuth9000"):
	print("Welcome back... your flag, user:")
	decryption = str_xor(flag_enc.decode(), "utilitarian")
	print(decryption)
	return
print("That password is incorrect")
```

`"a" + "b" = "ab"` is a string concatenation operation in Python. These lines of code in `patchme.flag.py` checks whether our input is equivalent to `ak98-=90adfjhgj321sleuth9000`, hence I provided it as the password and obtained the flag.

```
$ python patchme.flag.py
Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000
Welcome back... your flag, user:
picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}
```

## Flag

`picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}`