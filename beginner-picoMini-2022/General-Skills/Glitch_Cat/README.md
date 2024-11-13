## Glitch Cat

Connecting to the challenge instance, the following was printed:
`'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'`

By converting the provided hex values to their respective ASCII values, the flag was obtained.
- chr(0x62) = b
- chr(0x64) = d
- chr (0x61) = a
- chr(0x36) = 6
- chr(0x38) = 8
- chr(0x66) = f
- chr(0x37) = 7
- chr(0x35) = 5

### Flag

`picoCTF{gl17ch_m3_n07_bda68f75}`