# GDB baby step 2

- [Description](#description)
- [Approach](#approach)
- [Alternative Approach](#alternative-approach)
- [Flag](#flag)

## Description

Can you figure out what is in the `eax` register at the end of the `main` function? Put your answer in the picoCTF flag format: `picoCTF{n}` where n is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`.
Debug [this](https://artifacts.picoctf.net/c/520/debugger0_b).

## Approach

```asm
gef➤  disassemble
Dump of assembler code for function main:
   0x0000000000401106 <+0>:     endbr64
   0x000000000040110a <+4>:     push   rbp
   0x000000000040110b <+5>:     mov    rbp,rsp
=> 0x000000000040110e <+8>:     mov    DWORD PTR [rbp-0x14],edi
   0x0000000000401111 <+11>:    mov    QWORD PTR [rbp-0x20],rsi
   0x0000000000401115 <+15>:    mov    DWORD PTR [rbp-0x4],0x1e0da
   0x000000000040111c <+22>:    mov    DWORD PTR [rbp-0xc],0x25f
   0x0000000000401123 <+29>:    mov    DWORD PTR [rbp-0x8],0x0
   0x000000000040112a <+36>:    jmp    0x401136 <main+48>
   0x000000000040112c <+38>:    mov    eax,DWORD PTR [rbp-0x8]
   0x000000000040112f <+41>:    add    DWORD PTR [rbp-0x4],eax
   0x0000000000401132 <+44>:    add    DWORD PTR [rbp-0x8],0x1
   0x0000000000401136 <+48>:    mov    eax,DWORD PTR [rbp-0x8]
   0x0000000000401139 <+51>:    cmp    eax,DWORD PTR [rbp-0xc]
   0x000000000040113c <+54>:    jl     0x40112c <main+38>
   0x000000000040113e <+56>:    mov    eax,DWORD PTR [rbp-0x4]
   0x0000000000401141 <+59>:    pop    rbp
   0x0000000000401142 <+60>:    ret
End of assembler dump.
```

Looking at the disassembled `main()` function, I set a breakpoint at `<main+59>` to view the content of `eax` right before it returns.

```asm
gef➤  b *main+59
Breakpoint 1 at 0x401141
```

Then, I read the value of `eax` after running the program up till the breakpoint.

```asm
gef➤  p $eax
$1 = 0x4af4b
```

Converting the number from hex to decimal, `307019` is obtained.

## Alternative Approach

Using GDB to disassemble the `main()` function:

From `<main+15>`, `<main+22>` and `<main+29>`, we know the values at these 3 memory location below.
- `[rbp-0x4]` : `0x1e0da`
- `[rbp-0xc]` : `0x25f`
- `[rbp-0x8]` : `0x0`

Then the program jumps to `<main+48>`, which sets the `eax` register to the values in `[rbp-0x8]`(`0x0`), which is less than the value in `[rbp-0xc]`(`0x25f`), so it jumps again to `<main+38>`.

### 1st loop

After which, `eax` is set to `[rbp-0x8]`'s value (`0x0`). `eax`'s value will be added to the value at `[rbp-0x4]` and `[rbp-0x8]` will be incremented by 1. Then, `[rbp-0x8]`'s value is moved to `eax` and compared with the value at `[rbp-0xc]`(`0x25f`). If it is lesser than `0x25f`, it will loop again.

### Exit loop

Once `eax` is equivalent to `0x25f`, the value at `[rbp-0x4]` will be moved to `eax` and that is the answer

### Calculations

```
0x1e0da + (0x1 + 0x2 + 0x3 + ... + 0x25e) = 307019
```

## Flag

`picoCTF{307019}`