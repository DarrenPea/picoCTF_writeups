# Special

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)
Start your instance to see connection details.
Additional details will be available after launching your challenge instance.

`ssh -p 61160 ctf-player@saturn.picoctf.net` <br>
The password is `fd7746b4`

## Approach

Upon trying a few alphabets, it seems that it always replaces the alphabets with something else and says its not found. What if I could call the command directly through `/usr/bin/` since it contains the executable files? It works!

```
Special$ '/usr/bin/ls'
'/usr/bin/ls'
blargh
```

With this, I read the flag in the `blargh/` directory.

```
Special$ '/usr/bin/ls' 'blargh'
'/usr/bin/ls' 'blargh'
flag.txt

Special$ '/usr/bin/cat' 'blargh/flag.txt'
'/usr/bin/cat' 'blargh/flag.txt'
picoCTF{5p311ch3ck_15_7h3_w0r57_f578af59}
```

## Flag

`picoCTF{5p311ch3ck_15_7h3_w0r57_f578af59}`