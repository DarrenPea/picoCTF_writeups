## Serpentine

When executing `serpentine.py`, I was presented with 3 options:
```
a) Print encouragement
b) Print flag
c) Quit
```

After choosing `b`, it says that the function `print_flag()` was misplaced, so I looked at the Python file. There was indeed a function `print_flag()` that has been implemented, but it was not called. This function does a `XOR` operation with the key `'enkidu'` to decrypt the flag.

Hence, I added `print_flag()` to option `b`, and ran the code again to obtain the flag.

### Flag

`picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}`