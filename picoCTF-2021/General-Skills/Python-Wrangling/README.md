# Python Wrangling

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py) using [this password](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/pw.txt) to get [the flag](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/flag.txt.en)?

## Approach

Upon running the python file, it appears I need a `-d` or `-e` flag to choose between decryption and encryption. I would also have to provide a password to decrypt/encrypt files.

Hence, I used the `-d` flag and the password from `pw.txt` to decrypt the flag. `<` is used to take the data from `pw.txt` and redirect it to the password input required by `python ende.py -d flag.txt.en`.

```
$ python ende.py -d flag.txt.en < pw.txt
Please enter the password:picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}
```

## Flag

`picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}`