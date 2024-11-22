# extensions

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

This is a really weird text file [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)? Can you find the flag?

## Approach

Checking the file type of this .txt file, it claims that it is a PNG instead.

```
└─$ file flag.txt
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```

Also, looking at the magic bytes of the file,

```
└─$ xxd flag.txt
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```

Hence, I changed the file extension, from `flag.txt` to `flag.png` and obtained the flag.

## Flag

`picoCTF{now_you_know_about_extensions}`