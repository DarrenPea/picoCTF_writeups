# vault-door-4

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/c695ee23309d453a3ef369c34cc1bccb/VaultDoor4.java)

## Approach

Analysing the Java code, the password is checked against `myBytes`.

```java
public boolean checkPassword(String password) {
	byte[] passBytes = password.getBytes();
	byte[] myBytes = {
		106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
		0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
		0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,
		'4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
	};
	for (int i=0; i<32; i++) {
		if (passBytes[i] != myBytes[i]) {
			return false;
		}
	}
	return true;
}
```

Using Cyberchef for the appropriate conversions of each rows to their respective characters, I obtained the flag.

myBytes: <br>
Row 1: Decimal <br>
`106, 85, 53, 116, 95, 52, 95, 98`: `jU5t_4_b` <br>
Row 2: Hexadecimal <br>
`0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f`: `UnCh_0f_` <br>
Row 3: Octal <br>
`0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,`: `bYt3s_8f`

## Flag

`picoCTF{jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b}`