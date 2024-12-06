# Packets Primer

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Download the packet capture file and use packet analysis software to find the flag.
- [Download packet capture](https://artifacts.picoctf.net/c/195/network-dump.flag.pcap)

## Approach

Following TCP stream 0 in `network-dump.flag.pcap`, the flag is obtained.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Forensics/Packet-Primer/img/flag.png" />
</p>

## Flag

`picoCTF{p4ck37_5h4rk_b9d53765}`