# timer

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

You will find the flag after analysing this apk
Download [here](https://artifacts.picoctf.net/c/449/timer.apk).

## Approach

With the `.apk` file provided, I proceeded to use `apktool` to decompile the APK file.

```
$ apktool d timer.apk
```

This creates a `timer/` folder with lots of files. Hence, I tried to search for the flag using `grep` and successfully found it.

```
$ grep -r picoCTF timer/
timer/apktool.yml:  versionName: picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}
```

## Flag

`picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}`