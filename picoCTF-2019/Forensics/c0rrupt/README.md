# extensions

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

We found this [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery). Recover the flag.


## Approach

The file is unable to be opened, neither `strings` returned a flag. So, I went to use a hex editor.

```
$ xxd mystery | head -n 1
00000000: 8965 4e34 0d0a b0aa 0000 000d 4322 4452  .eN4........C"DR
```

I know that eN4 is not a valid extension, and I realised `8965 4e34 0d0a b0aa` looks similar to the magic bytes for `PNG`, so i changed it.

```
$ xxd mystery | head -n 2
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4322 4452  .PNG........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
```

Apart from its magic bytes, there are a few critical chunks that will contain information about the image. In particular, `IHDR` must be first, alongside `PLTE`, which is a list of colours, then `IDAT`, which is the image that can be split into multiplt `IDAT` and finally `IEND` to mark the image end ([Reference](https://en.wikipedia.org/wiki/PNG)).

```
$ xxd mystery | head -n 2
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
```

After change `C"DR` to `IHDR`, I used `pngcheck` to check if the file works.

```
$ pngcheck -v mystery
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERRORS DETECTED in mystery
```

A CRC error suggest that there is an error with the chunk type/data. Since pHYs is a valid chunk type, there is an issue with its data.

```
pHYs data:
	Pixels per unit, X axis: 4 bytes (unsigned integer)
	Pixels per unit, Y axis: 4 bytes (unsigned integer)
	Unit specifier:          1 byte
```

Based on `pngcheck`, the pixels per unit in the X axis is very large (`2852132389`) in comparison to the Y axis (`5669`), so I looked at into the hex editor.

```
$ xxd mystery | head -n 6
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 0000 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
```

As seen, the X axis has value `aa00 1625`, while the Y axis has value `0000 1625`, so I changed the X axis value to `0000 1625`.

```
$ pngcheck mystery
mystery  invalid chunk length (too large)
ERROR: mystery
```

I looked after the `pHYs` chunk and noted that there is an unusual chunk `DET` so I looked for the closest chunk type and changed it to `IDAT`. However, the data length is declared `aa aaff a5`, which is very large, which may have resulted in the `pngcheck` error.

Since `IDAT` chunks are consecutive, I calculated the data length from the first `IDAT` to the second `IDAT`. <br>
The first `IDAT` has offset `0x57`, while the second `IDAT` has offset `0x10008`. <br>
Due to file structure, I have to account for the extra bytes that is between these offset, the first `IDAT`'s chunk type and CRC, and the second `IDAT`'s length, which sums up to 12 bytes.

```
0x10008 - 0x57 - 0xC = 0xFFA5
```

So, I changed the data length of the first `IDAT` to `00 00ff a5` and the image was finally fixed.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2019/Forensics/c0rrupt/img/mystery.png" />
</p>

## Flag

`picoCTF{c0rrupt10n_1847995}`