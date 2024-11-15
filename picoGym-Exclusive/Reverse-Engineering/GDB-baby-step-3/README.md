# GDB baby step 3

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Now for something a little different. `0x2262c96b` is loaded into memory in the `main` function. Examine byte-wise the memory that the constant is loaded in by using the GDB command `x/4xb addr`. The flag is the four bytes as they are stored in memory. If you find the bytes `0x11 0x22 0x33 0x44` in the memory location, your flag would be: `picoCTF{0x11223344}`.
Debug [this](https://artifacts.picoctf.net/c/531/debugger0_c).

## Approach

```asm
gef➤  b main
gef➤  r
gef➤  disassemble
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
=> 0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x2262c96b
   0x000000000040111c <+22>:    mov    eax,DWORD PTR [rbp-0x4]
   0x000000000040111f <+25>:    pop    rbp
   0x0000000000401120 <+26>:    ret
End of assembler dump.
```

As seen, `<main+15>` is the instruction where `0x2262c96b` is loaded to the `[rbp-0x4]` memory address. So, i set another breakpoint at `<main+15>`, and carry out 1 instruction after reaching that breakpoint. Then, viewed the memory at location `[rbp-0x4]` using `x/4xb`.

```asm
gef➤  b *main+15
gef➤  c
gef➤  ni
gef➤  x/4xb $rbp-0x4
0x7fffffffd8ac: 0x6b    0xc9    0x62    0x22
```


## Flag

`picoCTF{0x6bc96222}`