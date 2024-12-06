# unpackme

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you get the flag?
Reverse engineer this [binary](https://artifacts.picoctf.net/c/205/unpackme-upx).

## Approach

After using `upx -d` to decompress the executable provided to me, I used `gdb` to analyse the `main` function. 

To perform a static analysis of `main`, I used `disas main` inside `gdb`. When running the program, it first asks "Whats your favourite number?", before requiring our input. This corresponds to the following code.
```asm
0x0000000000401ea3 <+96>:    mov    eax,0x0
0x0000000000401ea8 <+101>:   call   0x410ba0 <printf>
0x0000000000401ead <+106>:   lea    rax,Ärbp-0x3cÜ
0x0000000000401eb1 <+110>:   mov    rsi,rax
0x0000000000401eb4 <+113>:   lea    rdi,Ärip+0xb1165Ü        # 0x4b3020
0x0000000000401ebb <+120>:   mov    eax,0x0
0x0000000000401ec0 <+125>:   call   0x410d30 <__isoc99_scanf>
0x0000000000401ec5 <+130>:   mov    eax,DWORD PTR Ärbp-0x3cÜ
0x0000000000401ec8 <+133>:   cmp    eax,0xb83cb
0x0000000000401ecd <+138>:   jne    0x401f12 <main+207>
```

After reading our input, it appears to compare with `0xb83cb`, which is `754635` in decimal. If the input is not `754635`, it jumps to `<main+207>`, which ends the program.

After providing `754635` as the input, I obtained the flag.

## Flag

`picoCTF{up><_m3_f7w_5769b54e}`