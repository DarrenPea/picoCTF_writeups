# Operation Oni

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Download this disk image, find the key and log into the remote machine.
Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory. <br>
Additional details will be available after launching your challenge instance.

[Download disk image](https://artifacts.picoctf.net/c/69/disk.img.gz) <br>
Remote machine: `ssh -i key_file -p 52870 ctf-player@saturn.picoctf.net`

## Approach

After unzipping the folder, I first used `mmls` to view the partition layout of the image.

```
$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)
```

It seems that there are 2 Linux partitions. Using `fls`, I realised the first partition didn't seem too interesting so I looked into the second partition.

Within the `/root/` folder in the second partition, I noticed something interesting.

```
$ fls -o 206848 disk.img
d/d 458:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 79: proc
d/d 80: dev
d/d 81: tmp
d/d 82: lib
d/d 85: var
d/d 94: usr
d/d 104:        bin
d/d 118:        sbin
d/d 464:        media
d/d 468:        mnt
d/d 469:        opt
d/d 470:        root
d/d 471:        run
d/d 473:        srv
d/d 474:        sys
V/V 33049:      $OrphanFiles

$ fls -o 206848 disk.img 470
r/r 2344:       .ash_history
d/d 3916:       .ssh
```

Let's see what is in `.ash_history`.

```
$ icat -o 206848 disk.img 2344
ssh-keygen -t ed25519
ls .ssh/
halt
```

It appears that an ssh key is generated with the key type, `ed25519`, and the public and private keys are saved in the `.ssh/` folder.

```
$ fls -o 206848 disk.img 3916
r/r 2345:       id_ed25519
r/r 2346:       id_ed25519.pub
```

I then proceeded to extract the private and public key files into my folder.

```
$ icat -o 206848 disk.img 2345 > openssh_priv

$ icat -o 206848 disk.img 2346 > openssh_pub
```

To connect to `ctf-player@saturn.picoctf.net` port `52870`, we need to provide the private key file as our input key file.

```
$ ssh -i openssh_priv -p 52870 ctf-player@saturn.picoctf.net
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 6.5.0-1023-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$
```

With this, we have succesfully connected using `ssh`. Upon looking for the flag, it appears to be in the home directory.

```
ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat flag.txt
picoCTF{k3y_5l3u7h_339601ed}
```

## Flag

`picoCTF{k3y_5l3u7h_339601ed}`