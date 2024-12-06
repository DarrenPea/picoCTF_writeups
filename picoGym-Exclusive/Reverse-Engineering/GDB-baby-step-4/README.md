# GDB baby step 4

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

main calls a function that multiplies `eax` by a constant. The flag for this challenge is that constant in decimal base. If the constant you find is `0x1000`, the flag will be `picoCTF{4096}`.
Debug [this](https://artifacts.picoctf.net/c/532/debugger0_d).

## Approach

`main` function:
```asm
gef➤  disassemble
Dump of assembler code for function main:
   0x000000000040111c <+0>:     endbr64
   0x0000000000401120 <+4>:     push   rbp
   0x0000000000401121 <+5>:     mov    rbp,rsp
=> 0x0000000000401124 <+8>:     sub    rsp,0x20
   0x0000000000401128 <+12>:    mov    DWORD PTR [rbp-0x14],edi
   0x000000000040112b <+15>:    mov    QWORD PTR [rbp-0x20],rsi
   0x000000000040112f <+19>:    mov    DWORD PTR [rbp-0x4],0x28e
   0x0000000000401136 <+26>:    mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040113d <+33>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401140 <+36>:    mov    edi,eax
   0x0000000000401142 <+38>:    call   0x401106 <func1>
   0x0000000000401147 <+43>:    mov    DWORD PTR [rbp-0x8],eax
   0x000000000040114a <+46>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040114d <+49>:    leave
   0x000000000040114e <+50>:    ret
End of assembler dump.
```

`func1` function:
```asm
gef➤  disassemble
Dump of assembler code for function func1:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
=> 0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000000000401111 <+11>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401114 <+14>:    imul   eax,eax,0x3269
   0x000000000040111a <+20>:    pop    rbp
   0x000000000040111b <+21>:    ret
End of assembler dump.
```

The `main` function stores the value in memory location `[rbp-0x4]` in the `eax` register, with value `0x28e`. At `<main+38>`, `func1` is called.

Taking a look at `func1`, `<func1+14>` multiplies the value in `eax` register with `0x3269` and the value at `eax` is derived from `edi`, which can be traced back to the `main` function, which has value `0x28e`.

Basically, the value returned will be `0x28e x 0x3269 = 8439870`

So, the constant that is being multiplied with `eax` is `0x3269`

## Flag

`picoCTF{12905}`