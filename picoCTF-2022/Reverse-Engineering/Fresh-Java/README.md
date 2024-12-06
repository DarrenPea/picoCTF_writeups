# Fresh Java

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you get the flag?
Reverse engineer this [Java program](https://artifacts.picoctf.net/c/199/KeygenMe.class).

## Approach

Upon trying to run the Java file, it prompts me for a key.

```
$ java KeygenMe
Enter key:
```

There were no useful information when I used `strings`, so I decided to decompile the program with Ghidra.

Looking at the main function, it seems that it is comparing each character of the key value. If any character is wrong, it returns "Invalid key".

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Reverse-Engineering/Fresh-Java/img/main.png" />
</p>

Upon piecing the characters together for a valid key, I obtained `picoCTF{700l1ng_r3qu1r3d_2bfe1a0d}`

## Flag

`picoCTF{700l1ng_r3qu1r3d_2bfe1a0d}`