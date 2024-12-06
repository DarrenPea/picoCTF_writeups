# plumbing

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 4427.

## Approach

I used netcat to connect to the challenge and realised it generated large amounts of data. As such, I decided to save them in a `.txt` file and perform `grep` to obtain the flag.

```bash
$ nc jupiter.challenges.picoctf.org 4427 > output.txt
$ cat output.txt | grep "picoCTF"
picoCTF{digital_plumb3r_5ea1fbd7}
```

## Flag

`picoCTF{digital_plumb3r_5ea1fbd7}`