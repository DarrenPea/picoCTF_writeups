# Specialer

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.
Additional details will be available after launching your challenge instance.

`ssh -p 54475 ctf-player@saturn.picoctf.net`. The password is `fd7746b4`

## Approach

After connecting using `ssh`, I tried to do `ls`, but it says that the command is not found. So, I used `help` to list out the available commands.

After looking through, the relatively more helpful commands now are `cd` and `pwd`. But I do not know where to `cd` to. However, `cd` has a feature, such that I can use the `Tab` key to list out the directories/files. It also applies to other commands in general.

```
Specialer$ cd
.hushlogin  .profile    abra/       ala/        sim/
```

After looking into the directories, it seems that there are `.txt` files stored in them, but `cat` command is not found too. But, `echo` is still available, so I can do `echo $(< path/.txt file)` to print the contents of the file.

After looking through the various `.txt` files, I managed to obtain the flag.

```
Specialer$ echo $(< ala/kazam.txt)
return 0 picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_38f5cc78}
```

## Flag

`picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_38f5cc78}`