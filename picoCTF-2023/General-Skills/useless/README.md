# useless

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

There's an interesting script in the user's home directory
Additional details will be available after launching your challenge instance.

The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.
Hostname: saturn.picoctf.net
Port:     57852
Username: picoplayer
Password: password

## Approach

To connect to the instance using ssh:

```
$ ssh -p 57852 picoplayer@saturn.picoctf.net

Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
picoplayer@saturn.picoctf.net's password: password
```

We can see that there is a file that is in the home directory.

```
picoplayer@challenge:~$ ls
useless
```

Upon reading the script, it seems to do basic mathematical operations in the following format:

```
./useless add 1 2
./useless sub 1 2 
./useless mul 1 2
./useless div 4 2
```

If I did not provide 3 arguments, it would prompt me to read the code. Meanwhile, if I did not use `add`, `sub`, `mul` or `div`, it asked me to read the manual!!

So, I looked at the manual with `man useless` and obtained the flag.

## Flag

`picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_8504}`