# Disk, disk, sleuth!

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/920731987787c93839776ce457d5ecd6/dds1-alpine.flag.img.gz)

## Approach

From the description, it seems that the flag is a string within the image. As such, I used `srch_strings` to display the printable strings inside the image and used `grep` to obtain the strings I want.

```
$ srch_strings dds1-alpine.flag.img | grep picoCTF
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0}
```

## Flag

`picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0}`