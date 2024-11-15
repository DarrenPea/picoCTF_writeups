# Big Zip

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Unzip this archive and find the flag.
- [Download zip file](https://artifacts.picoctf.net/c/503/big-zip-files.zip)

## Approach

To retrieve the contents in the zip, i ran the following command

```bash
unzip -p big-zip-files.zip | grep "picoCTF"
```

The `-p` flag for `unzip` redirects the file to stdout, then i piped it through `grep` to look for strings that contain `"picoCTF"` to obtain the flag.

## Flag

`picoCTF{gr3p_15_m4g1c_ef8790dc}`