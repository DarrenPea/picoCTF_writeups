# Nice netcat...

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 35652`, but it doesn't speak English...

## Approach

First, I saved the response from netcat into `file.txt`.

```bash
$ nc mercury.picoctf.net 35652 > file.txt
```

I realised that it was made up of decimals that were seperated by ` \n` so I removed all `\n` for formatting purposes.

```bash
$ tr -d '\n' < file.txt > file1.txt

$ cat file1.txt
112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 57 98 51 98 55 51 57 50 125 10
```

Using CyberChef, I decoded the flag that was encoded in decimal to obtain the flag in plaintext.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2021/General-Skills/Nice-netcat/img/flag.png" />
</p>

## Flag

`picoCTF{g00d_k1tty!_n1c3_k1tty!_9b3b7392}`