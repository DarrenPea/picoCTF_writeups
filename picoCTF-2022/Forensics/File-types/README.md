# File types

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can. <br>
You can download the file from [here](https://artifacts.picoctf.net/c/81/Flag.pdf).

## Approach

Upon reading `Flag.pdf`, it mentions that to extract the files in it, I should use `sh`.

```
$ file Flag.pdf
Flag.pdf: shell archive text

$ sh Flag.pdf
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046.
```

Upon looking at the file type of `flag`, it seems that it is an ar archive so i can try to extract files from this archive.

```
$ file flag
flag: current ar archive

$ ar x flag

$ ls
flag  Flag.pdf  README.md
```

After extracting the file in the ar archive, I have a cpio archive, `flag`, which I can extract using `cpio`.

```
$ file flag
flag: cpio archive; device 234, inode 37426, mode 100644, uid 0, gid 0, modified Thu Mar 16 01:40:17 2023, 510 bytes "flag"

$ mv flag flag.cpio

$ cpio -iv < flag.cpio
flag
2 blocks

$ ls
flag  flag.cpio  Flag.pdf  README.md
```

Now, `flag` is a bzip2 compressed file so I can use `bunzip2` to decompress the data.

```
$ mv flag flag.bz2

$ file flag.bz2
flag.bz2: bzip2 compressed data, block size = 900k

$ bunzip2 -k flag.bz2

$ ls
flag  flag.bz2  flag.cpio  Flag.pdf  README.md
```

With this, I get `flag` file, which is a gzip compressed file so I can use `gunzip` to decompress the file.

```
$ file flag
flag: gzip compressed data, was "flag", last modified: Thu Mar 16 01:40:17 2023, from Unix, original size modulo 2^32 327

$ mv flag flag.gz

$ gunzip -k flag.gz

$ ls
flag  flag.bz2  flag.cpio  flag.gz  Flag.pdf  README.md
```

Now, the `flag` file is a lzip compressed file so I used `lzip` to decompress the file.

```
$ file flag
flag: lzip compressed data, version: 1

$ mv flag flag.lz

$ lzip -dk flag.lz

$ ls
flag  flag.bz2  flag.cpio  flag.gz  flag.lz  Flag.pdf  README.md
```

After decompressing with `lzip`, `flag` is now compressed with `lz4` so I used `lz4` to decompress the data.

```
$ file flag
flag: LZ4 compressed data (v1.4+)

$ mv flag flag.lz4

$ lz4 -dk flag.lz4
Decoding file flag
flag.lz4             : decoded 265 bytes

$ ls
flag  flag.bz2  flag.cpio  flag.gz  flag.lz  flag.lz4  Flag.pdf  README.md
```

Now, `flag` is a LZMA compressed file, so I used `xz` to decompress the file.

```
$ file flag
flag: LZMA compressed data, non-streamed, size 254

$ mv flag flag.lzma

$ xz -dk flag.lzma

$ ls
flag  flag.bz2  flag.cpio  flag.gz  flag.lz  flag.lz4  flag.lzma  Flag.pdf  README.md
```

Now, `flag` is `lzop` compressed, so I used `lzop` to decompress it.

```
$ file flag
flag: lzop compressed data - version 1.040, LZO1X-1, os: Unix

$ mv flag flag.lzop

$ lzop -d flag.lzop

$ ls
flag  flag.bz2  flag.cpio  flag.gz  flag.lz  flag.lz4  flag.lzma  flag.lzop  Flag.pdf  README.md
```

Now, `flag` is a `lzip` compressed file so I used `lzip` again to decompress the file.

```
$ file flag
flag: lzip compressed data, version: 1

$ mv flag flag_2.lz

$ lzip -dk flag_2.lz

$ mv flag_2 flag

$ ls
flag  flag_2.lz  flag.bz2  flag.cpio  flag.gz  flag.lz  flag.lz4  flag.lzma  flag.lzop  Flag.pdf  README.md
```

Now, `flag` is `xz` compressed, so I used `xz` to decompress the data.

```
$ file flag
flag: XZ compressed data, checksum CRC64

$ mv flag flag.xz

$ xz -dk flag.xz

$ ls
flag  flag_2.lz  flag.bz2  flag.cpio  flag.gz  flag.lz  flag.lz4  flag.lzma  flag.lzop  Flag.pdf  flag.xz  README.md
```

Finally, `flag` is an ASCII text, which contains the flag.

```
$ cat flag
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f37396230316332367d0a
```

This seems to be in hexadecimals, so converting it to ASCII using [Cyberchef](https://cyberchef.net/#recipe=From_Hex('Auto')&input=NzA2OTYzNmY0MzU0NDY3YjY2MzE2YzY1NmU0MDZkMzM1ZjZkNDA2ZTMxNzA3NTZjNDA3NDMxMzA2ZTVmDQo2NjMwNzI1ZjMwNjIzMjYzNzU3MjMxMzc3OTVmMzczOTYyMzAzMTYzMzIzNjdkMGE&ieol=CRLF), this is obtained:
```
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}
```

## Flag

`picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}`