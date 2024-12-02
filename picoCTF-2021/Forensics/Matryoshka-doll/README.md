# Matryoshka doll

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/f6cc2560a70b1ea811c151accba5390f/dolls.jpg)

## Approach

Using `binwalk`, I found that there are more images hidden inside the original `dolls.jpg`, so I believe that I need to recursively perform binwalk on the doll images to obtain the flag.

```
$ binwalk dolls.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378955, uncompressed size: 383936, name: base_images/2_c.jpg
651613        0x9F15D         End of Zip archive, footer length: 22

$ tree
.
├── dolls.jpg
├── _dolls.jpg.extracted
│   ├── 4286C.zip
│   └── base_images
│       └── 2_c.jpg
```

Repeatedly perform `binwalk -e` on every image inside the base_images folders to obtain the flag.
```
$ tree
.
├── dolls.jpg
├── _dolls.jpg.extracted
│   ├── 4286C.zip
│   └── base_images
│       ├── 2_c.jpg
│       └── _2_c.jpg.extracted
│           ├── 2DD3B.zip
│           └── base_images
│               ├── 3_c.jpg
│               └── _3_c.jpg.extracted
│                   ├── 1E2D6.zip
│                   └── base_images
│                       ├── 4_c.jpg
│                       └── _4_c.jpg.extracted
│                           ├── 136DA.zip
│                           └── flag.txt
```

We finally found the flag inside the 4th image in `flag.txt`.

## Flag

`picoCTF{ac0072c423ee13bfc0b166af72e25b61}`