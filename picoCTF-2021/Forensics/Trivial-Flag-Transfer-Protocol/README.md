# Trivial Flag Transfer Protocol

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Figure out how they moved the [flag](https://mercury.picoctf.net/static/cc6074838ede2edf9f805fd2b58bdc58/tftp.pcapng).


## Approach

Analysing the file using Wireshark, I noticed that there are a few files being transmitted, like `picture3.bmp`, so I decided to export the objects using the `TFTP` protocol. 

Upon inspecting `instructions.txt` and `plan`, it appears that it is encrypted with some sort of cipher. Using ROT13, I managed to decrypt the text in both files.

`instructions.txt`: [Cyberchef](https://cyberchef.net/#recipe=ROT13(true,true,false,13)&input=R1NHQ1FCUkZBR1JBUEVMQ0dCSEVHRU5TU1ZQRkJKUlpIRkdRVkZUSFZGUkJIRVNZTlRHRU5BRlNSRS5TVlRIRVJCSEdOSk5MR0JVVlFSR1VSU1lOVE5BUVZKVllZUFVSUFhPTlBYU0JFR1VSQ1lOQQ0K&ieol=CRLF&oeol=CRLF)
```
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
```

`plan`: [Cyberchef](https://cyberchef.net/#recipe=ROT13(true,true,false,13)&input=VkhGUlFHVVJDRUJURU5aTkFRVVZRVkdKVkdVLVFIUlFWWVZUUkFQUi5QVVJQWEJIR0dVUkNVQkdCRg0K&ieol=CRLF&oeol=CRLF)
```
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
```

It seems that the flag is being hidden in the photos using `program.deb`. Upon inspecting `program.deb`, it appears to be `steghide`.

```
$ dpkg --info program.deb
 new Debian package, version 2.0.
 size 138310 bytes: control archive=1250 bytes.
     826 bytes,    18 lines      control
    1184 bytes,    17 lines      md5sums
 Package: steghide
 Source: steghide (0.5.1-9.1)
 Version: 0.5.1-9.1+b1
 Architecture: amd64
 Maintainer: Ola Lundqvist <opal@debian.org>
 Installed-Size: 426
 Depends: libc6 (>= 2.2.5), libgcc1 (>= 1:4.1.1), libjpeg62-turbo (>= 1:1.3.1), libmcrypt4, libmhash2, libstdc++6 (>= 4.9), zlib1g (>= 1:1.1.4)
 Section: misc
 Priority: optional
 Description: A steganography hiding tool
  Steghide is steganography program which hides bits of a data file
  in some of the least significant bits of another file in such a way
  that the existence of the data file is not visible and cannot be proven.
  .
  Steghide is designed to be portable and configurable and features hiding
  data in bmp, wav and au files, blowfish encryption, MD5 hashing of
  passphrases to blowfish keys, and pseudo-random distribution of hidden bits
  in the container data.
```

To obtain the information hidden in the pictures, I used `steghide extract -sf`, but it appears that a passphrase is needed. Revisiting the decrypted text from `instructions.txt` and `plan`, `DUEDILIGENCE` could be the possible passphrase. 

I was unable to extract data from `picture1.bmp` and `picture2.bmp` using the passphraes `DUEDILIGENCE`, but i was able to obtain `flag.txt` from `picture3.bmp`. 

## Flag

`picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`