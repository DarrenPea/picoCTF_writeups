# ASCII FTW

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

This program has constructed the flag using hex ascii values. Identify the flag text by disassembling the program.
You can download the file from [here](https://artifacts.picoctf.net/c/507/asciiftw).

## Approach

```asm
gef➤  disass main
Dump of assembler code for function main:
   0x0000555555555169 <+0>:     endbr64
   0x000055555555516d <+4>:     push   rbp
   0x000055555555516e <+5>:     mov    rbp,rsp
=> 0x0000555555555171 <+8>:     sub    rsp,0x30
   0x0000555555555175 <+12>:    mov    rax,QWORD PTR fs:0x28
   0x000055555555517e <+21>:    mov    QWORD PTR [rbp-0x8],rax
   0x0000555555555182 <+25>:    xor    eax,eax
   0x0000555555555184 <+27>:    mov    BYTE PTR [rbp-0x30],0x70
   0x0000555555555188 <+31>:    mov    BYTE PTR [rbp-0x2f],0x69
   0x000055555555518c <+35>:    mov    BYTE PTR [rbp-0x2e],0x63
   0x0000555555555190 <+39>:    mov    BYTE PTR [rbp-0x2d],0x6f
   0x0000555555555194 <+43>:    mov    BYTE PTR [rbp-0x2c],0x43
   0x0000555555555198 <+47>:    mov    BYTE PTR [rbp-0x2b],0x54
   0x000055555555519c <+51>:    mov    BYTE PTR [rbp-0x2a],0x46
   0x00005555555551a0 <+55>:    mov    BYTE PTR [rbp-0x29],0x7b
   0x00005555555551a4 <+59>:    mov    BYTE PTR [rbp-0x28],0x41
   0x00005555555551a8 <+63>:    mov    BYTE PTR [rbp-0x27],0x53
   0x00005555555551ac <+67>:    mov    BYTE PTR [rbp-0x26],0x43
   0x00005555555551b0 <+71>:    mov    BYTE PTR [rbp-0x25],0x49
   0x00005555555551b4 <+75>:    mov    BYTE PTR [rbp-0x24],0x49
   0x00005555555551b8 <+79>:    mov    BYTE PTR [rbp-0x23],0x5f
   0x00005555555551bc <+83>:    mov    BYTE PTR [rbp-0x22],0x49
   0x00005555555551c0 <+87>:    mov    BYTE PTR [rbp-0x21],0x53
   0x00005555555551c4 <+91>:    mov    BYTE PTR [rbp-0x20],0x5f
   0x00005555555551c8 <+95>:    mov    BYTE PTR [rbp-0x1f],0x45
   0x00005555555551cc <+99>:    mov    BYTE PTR [rbp-0x1e],0x41
   0x00005555555551d0 <+103>:   mov    BYTE PTR [rbp-0x1d],0x53
   0x00005555555551d4 <+107>:   mov    BYTE PTR [rbp-0x1c],0x59
   0x00005555555551d8 <+111>:   mov    BYTE PTR [rbp-0x1b],0x5f
   0x00005555555551dc <+115>:   mov    BYTE PTR [rbp-0x1a],0x37
   0x00005555555551e0 <+119>:   mov    BYTE PTR [rbp-0x19],0x42
   0x00005555555551e4 <+123>:   mov    BYTE PTR [rbp-0x18],0x43
   0x00005555555551e8 <+127>:   mov    BYTE PTR [rbp-0x17],0x44
   0x00005555555551ec <+131>:   mov    BYTE PTR [rbp-0x16],0x39
   0x00005555555551f0 <+135>:   mov    BYTE PTR [rbp-0x15],0x37
   0x00005555555551f4 <+139>:   mov    BYTE PTR [rbp-0x14],0x31
   0x00005555555551f8 <+143>:   mov    BYTE PTR [rbp-0x13],0x44
   0x00005555555551fc <+147>:   mov    BYTE PTR [rbp-0x12],0x7d
   0x0000555555555200 <+151>:   movzx  eax,BYTE PTR [rbp-0x30]
   0x0000555555555204 <+155>:   movsx  eax,al
   0x0000555555555207 <+158>:   mov    esi,eax
   0x0000555555555209 <+160>:   lea    rdi,[rip+0xdf4]        # 0x555555556004
   0x0000555555555210 <+167>:   mov    eax,0x0
   0x0000555555555215 <+172>:   call   0x555555555070 <printf@plt>
   0x000055555555521a <+177>:   nop
   0x000055555555521b <+178>:   mov    rax,QWORD PTR [rbp-0x8]
   0x000055555555521f <+182>:   xor    rax,QWORD PTR fs:0x28
   0x0000555555555228 <+191>:   je     0x55555555522f <main+198>
   0x000055555555522a <+193>:   call   0x555555555060 <__stack_chk_fail@plt>
   0x000055555555522f <+198>:   leave
   0x0000555555555230 <+199>:   ret
End of assembler dump.
```

Looking at the assembly code, i notice the flag is being stored from `<main+27>` to `<main+147>`, so i set a breakpoint after `<main+147>` and analysed the stack to obtain the flag.

```asm
0x00007fffffffd8a0│+0x0000: "picoCTF{ASCII_IS_EASY_7BCD971D}"    ← $rsp
0x00007fffffffd8a8│+0x0008: "ASCII_IS_EASY_7BCD971D}"
0x00007fffffffd8b0│+0x0010: "_EASY_7BCD971D}"
0x00007fffffffd8b8│+0x0018: 0x007d443137394443 ("CD971D}"?)
0x00007fffffffd8c0│+0x0020: 0x00007fffffffd9a0  →  0x0000000000000000
0x00007fffffffd8c8│+0x0028: 0x86b9bd70ffdc1f00
0x00007fffffffd8d0│+0x0030: 0x0000000000000001   ← $rbp
0x00007fffffffd8d8│+0x0038: 0x00007ffff7de7dba  →  <__libc_start_call_main+007a> mov edi, eax
```

## Flag

`picoCTF{ASCII_IS_EASY_7BCD971D}`