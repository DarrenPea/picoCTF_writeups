# Disk, disk, sleuth! II

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

All we know is the file with the flag is named `down-at-the-bottom.txt`... Disk image: [dds2-alpine.flag.img.gz](https://mercury.picoctf.net/static/626abf12c976b994999f77eec3138a22/dds2-alpine.flag.img.gz)

## Approach

After unzipping the image with `gunzip`, I used `mmls` to display its partition layout.

```
$ mmls dds2-alpine.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)
```

Then, i used `fls` to view the files and directories on the Linux partition with offset `2048`. Since we know that the flag is in `down-at-the-bottom.txt`, we can use grep to search all file names in the partition.

```
$ fls -o 2048 dds2-alpine.flag.img -r | grep down
++ d/d 2177:    if-down.d
++ d/d 2178:    if-post-down.d
++ d/d 2180:    if-pre-down.d
++ d/d 2204:    shutdown
+ r/r 18291:    down-at-the-bottom.txt
+ l/l 18311:    ifdown
+ r/r 18344:    openrc-shutdown
+++++ r/r 12472:        down.sh
```

After obtaining the inode number of `down-at-the-bottom.txt`, I proceeded to read the file using `icat`.

```
$ icat -o 2048 dds2-alpine.flag.img 18291
   _     _     _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
   _     _     _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
   _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( 3 ) ( _ ) ( 0 ) ( d ) ( 9 ) ( d ) ( 9 ) ( e ) ( c ) ( b ) ( } )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
```

## Flag

`picoCTF{f0r3ns1c4t0r_n0v1c3_0d9d9ecb}`