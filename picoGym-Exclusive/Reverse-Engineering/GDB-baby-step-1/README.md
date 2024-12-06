# GDB baby step 1

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where n is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.
Disassemble [this](https://artifacts.picoctf.net/c/512/debugger0_a).

## Approach

Using GDB to disassemble the `main()` function:

```asm
gef➤  disassemble
Dump of assembler code for function main:
   0x0000555555555129 <+0>:     endbr64
   0x000055555555512d <+4>:     push   rbp
   0x000055555555512e <+5>:     mov    rbp,rsp
=> 0x0000555555555131 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x0000555555555134 <+11>:    mov    QWORD PTR [rbp-0x10],rsi
   0x0000555555555138 <+15>:    mov    eax,0x86342
   0x000055555555513d <+20>:    pop    rbp
   0x000055555555513e <+21>:    ret
End of assembler dump.
```

Observing `<main+15>`, `0x86342` has been moved into the `eax` register. The decimal representation of `0x86342` is `549698`.

## Flag

`picoCTF{549698}`