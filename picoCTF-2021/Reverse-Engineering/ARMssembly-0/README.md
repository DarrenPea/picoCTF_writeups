# ARMssembly 0

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

What integer does this program print with arguments `4004594377` and `4110761777`? File: [chall.S](https://mercury.picoctf.net/static/006961dc756fc3f418b0dbe0a42dcee8/chall.S) Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

## Approach

TLDR: After adding the 2nd argument by 24, the function prints out the larger of both numbers, which is `4110761777`. (Analysis can be found below)

Initially, the program name and both the arguments are stored in the pointer stored in `[x29, 32]`. This pointer points to the address of `argv`.

`argv[0]` stores the program name itself, followed `argv[1]`, stored at `[x0+8]` and `argv[2]` stored at `[x0+16]`.
```
str     x1, [x29, 32]
ldr     x0, [x29, 32]
add     x0, x0, 8		// 4004594377
ldr     x0, [x0]
...
ldr     x0, [x29, 32]
add     x0, x0, 16		// 4110761777
ldr     x0, [x0]
```

After both variables are stored in `x0`, they are converted from str to int using `atoi`. Then, `4004594377` is stored at `w0`, while `4110761777` is stored at `w1`, before executing `func1`.

This function will return the larger of both numbers and store it in `w0`. Basically, it compares if `w1 <= w0` and if true, branch to `.L2`, else it proceeds without branching.
```
func1:
	sub     sp, sp, #16
	str     w0, [sp, 12]
	str     w1, [sp, 8]
	ldr     w1, [sp, 12]
	ldr     w0, [sp, 8]
	cmp     w1, w0
	bls     .L2
	ldr     w0, [sp, 12]
	b       .L3
.L2:
	ldr     w0, [sp, 8]
.L3:
	add     sp, sp, 16
	ret
```

After that, the value at `w0` is printed out.
```
mov     w1, w0
adrp    x0, .LC0
add     x0, x0, :lo12:.LC0
bl      printf
```

## Flag

`picoCTF{f5053f31}`