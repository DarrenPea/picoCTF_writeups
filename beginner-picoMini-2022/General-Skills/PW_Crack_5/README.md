## PW Crack 5

This challenge seemed to provide multiple files to simulate cracking of passwords through brute force.

```python
def level_5_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```

I edited the script such that it would iterate through every possible password in dictionary.txt and check if its hash is equivalent to the actual password's hash, and eventually obtained the flag.

### Flag

`picoCTF{h45h_sl1ng1ng_fffcda23}`