# Wave a flag

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/f95b1ee9f29d631d99073e34703a2826/warm) has extraordinarily helpful information...

## Approach

The file provided is an ELF file.

```
$ file warm
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=01b148cdedfc38125cac0d87e0537466d47927b1, with debug_info, not stripped
```

Upon trying to execute the file, I was asked to add the `-h` flag to know what the program does.

```
$ ./warm
Hello user! Pass me a -h to learn what I can do!
```

After which, I added the flag and obtained the flag.

```
$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}
```

## Flag

`picoCTF{b1scu1ts_4nd_gr4vy_f0668f62}`