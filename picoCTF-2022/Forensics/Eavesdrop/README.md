# Eavesdrop

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Download this packet capture and find the flag.
- [Download packet capture](https://artifacts.picoctf.net/c/133/capture.flag.pcap)

## Approach

Upon analysing the PCAP file, I noticed that there is a conversation going on for TCP stream 0. 

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Forensics/Eavesdrop/img/conversation.png" />
</p>

It appears that the file is decrypted using the following command:
```
openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
```

So, I need to obtain `file.des3`. After analysing the other 2 TCP streams, I noticed that TCP stream 2 seems like an openssl file. So, I saved the packets in raw form as `file.des3`.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Forensics/Eavesdrop/img/openssl.png" />
</p>

Now, I run the command that was mentioned in TCP stream 0 and I obtained the flag.

```
$ openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123

$ cat file.txt
picoCTF{nc_73115_411_5786acc3}
```

## Flag

`picoCTF{nc_73115_411_5786acc3}`