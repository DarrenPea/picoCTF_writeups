# GDB Test Drive

- [Description](#description)
- [Analysis](#analysis)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you get the flag? <br>
Download this [binary](https://artifacts.picoctf.net/c/87/gdbme). <br>
Here's the test drive instructions:
- `$ chmod +x gdbme`
- `$ gdb gdbme`
- `(gdb) layout asm`
- `(gdb) break *(main+99)`
- `(gdb) run`
- `(gdb) jump *(main+104)`

## Analysis

To look at the `main` function, i disassembled the function in GDB

```
gef➤  disas main
```

Looking through the assenbly instructions, I noticed that the program is put to sleep for `0x186a0` seconds at `<main+99>`, which is equivalent to `100000` seconds, before continuing the rest of the program.

```
0x0000555555555319 <+82>:    mov    QWORD PTR [rbp-0x20],rax
0x000055555555531d <+86>:    mov    QWORD PTR [rbp-0x18],rdx
0x0000555555555321 <+90>:    mov    BYTE PTR [rbp-0x10],0x0
0x0000555555555325 <+94>:    mov    edi,0x186a0
0x000055555555532a <+99>:    call   0x555555555110 <sleep@plt>
0x000055555555532f <+104>:   lea    rax,[rbp-0x30]
0x0000555555555333 <+108>:   mov    rsi,rax
0x0000555555555336 <+111>:   mov    edi,0x0
0x000055555555533b <+116>:   call   0x555555555209 <rotate_encrypt>
0x0000555555555340 <+121>:   mov    QWORD PTR [rbp-0x38],rax
0x0000555555555344 <+125>:   mov    rdx,QWORD PTR [rip+0x2cc5]        # 0x555555558010 <stdout@@GLIBC_2.2.5>
0x000055555555534b <+132>:   mov    rax,QWORD PTR [rbp-0x38]
0x000055555555534f <+136>:   mov    rsi,rdx
0x0000555555555352 <+139>:   mov    rdi,rax
0x0000555555555355 <+142>:   call   0x5555555550f0 <fputs@plt>
0x000055555555535a <+147>:   mov    edi,0xa
0x000055555555535f <+152>:   call   0x5555555550c0 <putchar@plt>
0x0000555555555364 <+157>:   mov    rax,QWORD PTR [rbp-0x38]
0x0000555555555368 <+161>:   mov    rdi,rax
0x000055555555536b <+164>:   call   0x5555555550b0 <free@plt>
```

Hence, we stop the program before it executes the `sleep` function, then jump to the instruction after `sleep`, which is at `<main+104>`.

## Approach

Following the test drive instructions:

```
$ chmod +x gdbme	// gives 'gdbme' executable permissions

$ gdb gdbme			// opens gdbme in gdb
```

Now, we are inside gdb

```
(gdb) layout asm 	// opens in the assembly layout
```

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2022/Reverse-Engineering/GDB-Test-Drive/img/asm.png" />
</p>

```
(gdb) break *(main+99)		// adding a breakpoint at <main+99>
Breakpoint 1 at 0x132a
```

```
(gdb) run		// runs the program, but stops when it arrives at the Breakpoint 1 <main+99>
```

```
(gdb) jump *(main+104)		// jump to <main+104> and continues execution
Continuing at 0x55555555532f.
picoCTF{d3bugg3r_dr1v3_7776d758}
```

## Flag

`picoCTF{d3bugg3r_dr1v3_7776d758}`