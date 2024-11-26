# Static ain't always noise

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/e9dd71b5d11023873b8abe99cdb45551/static)? This [BASH script](https://mercury.picoctf.net/static/e9dd71b5d11023873b8abe99cdb45551/ltdis.sh) might help!

## Approach

Upon running the BASH script, it appears to require a program file.

```
─$ ./ltdis.sh
Attempting disassembly of  ...
objdump: 'a.out': No such file
objdump: section '.text' mentioned in a -j option, but not found in any input file
Disassembly failed!
Usage: ltdis.sh <program-file>
Bye!
```

After running the script on `static`, the disassembly can be found in `static.ltdis.x86_64.txt`, while the strings are found in `static.ltdis.strings.txt`.

```
$ ./ltdis.sh static
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```

Then, I used grep to obtain the flag from the strings file.

```
$ cat static.ltdis.strings.txt | grep pico
1020 picoCTF{d15a5m_t34s3r_ae0b3ef2}
```

## Flag

`picoCTF{d15a5m_t34s3r_ae0b3ef2}`