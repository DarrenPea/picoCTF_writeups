# Bit-O-Asm-4

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where `n` is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.
Download the assembly dump [here](https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt).

## Approach

```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
<+29>:    jle    0x55555555514e <main+37>
<+31>:    sub    DWORD PTR [rbp-0x4],0x65
<+35>:    jmp    0x555555555152 <main+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65
<+41>:    mov    eax,DWORD PTR [rbp-0x4]
<+44>:    pop    rbp
<+45>:    ret
```

Initially, `0x9fe1a` is loaded at memory location `[rbp-0x4]`. Since `0x9fe1a > 0x2710`, the program does not jump to `<main+37>`. <br>
`0x65` is then subtracted from `0x9fe1a`, before jumping to `<main+41>`, and the value is loaded in the `eax` register.

### Calculations

```
0x9fe1a - 0x65 = 654773
```

## Flag

`picoCTF{654773}`