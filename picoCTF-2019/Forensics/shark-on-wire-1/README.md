# shark on wire 1

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap). Recover the flag.


## Approach

Using `Wireshark` to analyse the file, I decided to filter by UDP and look into it. Following the UDP stream, I got 2 different flags, one of which was a fake flag and the other was real.

1. `picoCTF{N0t_a_fLag}`
2. `picoCTF{StaT31355_636f6e6e}`

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2019/Forensics/shark-on-wire-1/img/fake.png" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2019/Forensics/shark-on-wire-1/img/flag.png" />
</p>



## Flag

`picoCTF{StaT31355_636f6e6e}`