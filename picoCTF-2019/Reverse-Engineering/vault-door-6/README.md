# vault-door-6

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](https://jupiter.challenges.picoctf.org/static/86e94cc555b2ca7375424c884ef581a6/VaultDoor6.java)

## Approach

Analysing the Java code, the password is checked after each character is `XOR`-ed with `0x55`.

```java
byte[] passBytes = password.getBytes();
byte[] myBytes = {
	0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
	0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
	0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
	0xa , 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36,
};
for (int i=0; i<32; i++) {
	if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
		return false;
	}
}
return true;
```

Due to `XOR` property below, I can reverse engineer the password bytes to satisfy `(passbytes[i] ^ 0x55) = myBytes[i]`:

A &oplus; B = C is equivalent to C &oplus; B = A

For example, <br>
passBytes[0] = 0x3b &oplus; 0x55

After computing all bytes,

```java
byte[] passBytes = {
	0x6e, 0x30, 0x74, 0x5f, 0x6d, 0x55, 0x63, 0x48,
	0x5f, 0x68, 0x34, 0x72, 0x44, 0x33, 0x72, 0x5f,
	0x74, 0x48, 0x34, 0x6e, 0x5f, 0x78, 0x30, 0x72,
	0x5f, 0x39, 0x35, 0x62, 0x65, 0x35, 0x64, 0x63
}
```

Converting these from hex to ASCII, `n0t_mUcH_h4rD3r_tH4n_x0r_95be5dc` is obtained.

## Flag

`picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_95be5dc}`