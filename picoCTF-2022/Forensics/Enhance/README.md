# Enhance!

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Download this image file and find the flag.
- [Download image file](https://artifacts.picoctf.net/c/102/drawing.flag.svg)

## Approach

Using `exiftool`, there doesn't seem to be anything interesting.

```
$ exiftool drawing.flag.svg
ExifTool Version Number         : 13.00
File Name                       : drawing.flag.svg
Directory                       : .
File Size                       : 4.1 kB
File Modification Date/Time     : 2023:03:16 11:16:47+08:00
File Access Date/Time           : 2024:12:04 16:07:16+08:00
File Inode Change Date/Time     : 2024:12:04 16:07:16+08:00
File Permissions                : -rwxrwxrwx
File Type                       : SVG
File Type Extension             : svg
MIME Type                       : image/svg+xml
Xmlns                           : http://www.w3.org/2000/svg
Image Width                     : 210mm
Image Height                    : 297mm
View Box                        : 0 0 210 297
SVG Version                     : 1.1
ID                              : svg8
Version                         : 0.92.5 (2060ec1f9f, 2020-04-08)
Docname                         : drawing.svg
Metadata ID                     : metadata5
Work Format                     : image/svg+xml
Work Type                       : http://purl.org/dc/dcmitype/StillImage
Work Title                      :
```

I decided to try `strings` to look for the flag. It apears that the flag is being spread out throughout the last `<text></text>` tags.

Example:
```
<tspan
sodipodi:role="line"
x="107.43014"
y="132.11588"
style="font-size:0.00352781px;line-height:1.25;fill:#ffffff;stroke-width:0.26458332;"
id="tspan3752">c 3 d _ d 0 a 7 5 7 b f }</tspan>
```

Putting the texts together, I obtained the flag.

## Flag

`picoCTF{3nh4nc3d_d0a757bf}`