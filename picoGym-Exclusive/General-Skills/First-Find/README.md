# First Find

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Unzip this archive and find the file named 'uber-secret.txt'
- [Download zip file](https://artifacts.picoctf.net/c/502/files.zip)

## Approach

To retrieve the contents in the zip, i ran the following command

```bash
unzip -p files.zip | grep "picoCTF"
```

The `-p` flag for `unzip` redirects the file to stdout, then i piped it through `grep` to look for strings that contain `"picoCTF"` to obtain the flag.

## Flag

`picoCTF{f1nd_15_f457_ab443fd1}`