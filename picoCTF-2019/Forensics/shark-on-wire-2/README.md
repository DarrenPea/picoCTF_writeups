# shark on wire 2

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap). Recover the flag that was pilfered from the network.

## Approach

Upon analysing `capture.pcap` I filtered by UDP and realised there were traffic that seemed suspicious. This caught my attention.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2019/Forensics/shark-on-wire-2/img/start.png" />
</p>

Upon deeper looking, the UDP packets that were sent to port 22 seemed suspicious, in particular their source ports, in between both ports 5000, which appears to say "start" and "end".

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2019/Forensics/shark-on-wire-2/img/end.png" />
</p>

Then, I wrote a script that extracts these source ports, and subtract 5000 from them. After, I converted the decimal numbers to their respective ASCII values at got the flag.

## Flag

`picoCTF{p1LLf3r3d_data_v1a_st3g0}`