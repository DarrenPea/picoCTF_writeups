# Magikarp Ground Mission

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `ee388b88`
Additional details will be available after launching your challenge instance.

Challenge Endpoints: <br>
`ssh ctf-player@venus.picoctf.net -p 57195`

## Approach

After connecting to the challenge endpoint, I tried to look for `flag.txt`.

```
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
```

I seemed to obtain the first part of the flag.

```
ctf-player@pico-chall$ cat 1of3.flag.txt
picoCTF{xxsh_
```

It seems that the second flag is located at the root directory.

```
ctf-player@pico-chall$ cat instructions-to-2of3.txt
Next, go to the root of all things, more succinctly `/`

ctf-player@pico-chall$ cd /

ctf-player@pico-chall$ ls
2of3.flag.txt  boot  etc   instructions-to-3of3.txt  lib64  mnt  proc  run   srv  tmp  var
bin            dev   home  lib                       media  opt  root  sbin  sys  usr
```

Here, I obtained the second part of the flag.

```
ctf-player@pico-chall$ cat 2of3.flag.txt
0ut_0f_\/\/4t3r_
```

It seems that the last part of the flag is located in the home directory.

```
ctf-player@pico-chall$ cat instructions-to-3of3.txt
Lastly, ctf-player, go home... more succinctly `~`
```

Here, I obtained the last part of the flag.

```
ctf-player@pico-chall$ cd ~

ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in

ctf-player@pico-chall$ cat 3of3.flag.txt
3ca613a1}
```

## Flag

`picoCTF{xxsh_0ut_0f_\/\/4t3r_3ca613a1}`