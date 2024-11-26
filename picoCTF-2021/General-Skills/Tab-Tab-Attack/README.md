# Tab, Tab, Attack

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/659efd595171e4c40378be6a2e9b7298/Addadshashanammu.zip)

## Approach

Upon unzipping the file, I noticed there is a lot of sub-directories, and I probably would have to read/execute `fang-of-haynekhtnamet`.
```
$ tree
.
├── Addadshashanammu
│   └── Almurbalarammi
│       └── Ashalmimilkala
│           └── Assurnabitashpi
│               └── Maelkashishi
│                   └── Onnissiralis
│                       └── Ularradallaku
│                           └── fang-of-haynekhtnamet
├── Addadshashanammu.zip
└── README.md
```

Using `tab`, which auto-completes the file name available in the current working directory, I was in the `Ularradallaku` sub-directory and executed the ELF file, `fang-of-haynekhtnamet`, to obtain the flag.

```
$ ./fang-of-haynekhtnamet
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_524e3dc4}
```

## Flag

`picoCTF{l3v3l_up!_t4k3_4_r35t!_524e3dc4}`