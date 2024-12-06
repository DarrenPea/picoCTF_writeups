# Operation Orchid

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Download this disk image and find the flag.
Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
- [Download compressed disk image](https://artifacts.picoctf.net/c/214/disk.flag.img.gz)

## Approach

After unzipping the gzip file, I used `mmls` to look at the partition layout of the volume system.

```
$ mmls disk.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000411647   0000204800   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000411648   0000819199   0000407552   Linux (0x83)
```

It appears that there is 3 partitions, as shown in rows `002`, `003`, and `004`. 

Looking at the first 2 partitions, it doesn't seem promising.

When checking the third partition's `/root/` folder, I noticed something interesting.

```
$ fls -o 411648 disk.flag.img
d/d 460:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 81: proc
d/d 82: dev
d/d 83: tmp
d/d 84: lib
d/d 87: var
d/d 96: usr
d/d 106:        bin
d/d 120:        sbin
d/d 466:        media
d/d 470:        mnt
d/d 471:        opt
d/d 472:        root
d/d 473:        run
d/d 475:        srv
d/d 476:        sys
d/d 2041:       swap
V/V 51001:      $OrphanFiles

$ fls -o 411648 disk.flag.img 472
r/r 1875:       .ash_history
r/r * 1876(realloc):    flag.txt
r/r 1782:       flag.txt.enc
```

The flag could be in `flag.txt` or `flag.txt.enc` so i used `icat` to read the contents of the file.

```
$ icat -o 411648 disk.flag.img 1876
           -0.881573            34.311733

$ icat -o 411648 disk.flag.img 1782
Salted__S�+%���+�O��k�ђ(A����c��
                                @]ԣ
L�ޢȤ7� ���؎$�'%
```

It looks like the flag is encrypted in `flag.txt.enc`. So, I looked at `.ash_history`.

```
$ icat -o 411648 disk.flag.img 1875
touch flag.txt
nano flag.txt
apk get nano
apk --help
apk add nano
nano flag.txt
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
```

It seems that the flag has been encrypted using AES256 encryption, with the key `"unbreakablepassword1234567"`. Let's extract the encrypted flag from the image first.

```
$ icat -o 411648 disk.flag.img 1782 > flag.txt.enc
```

Using `openssl aes256` to decrypt the salted and encrypted flag with the key `"unbreakablepassword1234567"`, the flag is obtained.

```
$ openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567

$ cat flag.txt
picoCTF{h4un71ng_p457_1d02081e}
```

## Flag

`picoCTF{h4un71ng_p457_1d02081e}`