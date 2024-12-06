## PW Crack 2

This challenge provided 2 files:
- `level2.flag.txt.enc` - encrypted flag
- `level2.py` - password checker

Running `level2.py`, it asks for a password to retrieve the flag so I went to analyse the python file.

```python
def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```
From this function, the password for the flag is compared to `chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)`, which is equivalent to `4ec9`. Then, I got the flag by entering the correct password.

### Flag

`picoCTF{tr45h_51ng1ng_9701e681}`