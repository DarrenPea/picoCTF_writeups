# credstuff

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it? <br>
Download the leak [here](https://artifacts.picoctf.net/c/151/leak.tar). <br>
The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.

## Approach

Using `tar -xvf`, I extracted `usernames.txt` and `passwords.txt` in the `leak/` folder.

I first found the entry of `cultris` in `usernames.txt`, which I will then link it with the index in `passwords.txt` to obtain the password that corresponds to `cultris`.

```
$ cat -n usernames.txt | grep cultiris
   378  cultiris

$ cat -n passwords.txt | grep 378
   378  cvpbPGS{P7e1S_54I35_71Z3}
```

It appears that the flag could be encrypted with a shift cipher. Using [dCode](https://www.dcode.fr/caesar-cipher), I decrypted the ciphertext and obtained the flag. It was a shift by 13 letters, which is equivalent to a ROT13.

## Flag

`picoCTF{C7r1F_54V35_71M3}`