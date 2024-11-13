## PW Crack 1

This challenge provided 2 files:
- `level1.flag.txt.enc` - encrypted flag
- `level1.py` - password checker

Running `level1.py`, it asks for a password to retrieve the flag so I went to analyse the python file.

```python
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "8713"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```
From this function, the password for the flag is checked if its `8713`. Then, I got the flag by entering the correct password.

### Flag

`picoCTF{545h_r1ng1ng_1b2fd683}`