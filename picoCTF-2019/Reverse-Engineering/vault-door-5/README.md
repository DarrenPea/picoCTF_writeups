# vault-door-5

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](https://jupiter.challenges.picoctf.org/static/9505cca05dc00fecead41106370ee619/VaultDoor5.java)

## Approach

Analysing the Java code, the password is checked after URL encoding, followed by base-64 encoding.

```java
public boolean checkPassword(String password) {
	String urlEncoded = urlEncode(password.getBytes());
	String base64Encoded = base64Encode(urlEncoded.getBytes());
	String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
					+ "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
					+ "JTM0JTVmJTMwJTYyJTM5JTM1JTM3JTYzJTM0JTY2";
	return base64Encoded.equals(expected);
}
```

Using Cyberchef to base64-decode the `expected` string, then URL decode it, I obtained the flag.

<p align="center">
  <img src="https://raw.githubusercontent.com/DarrenPea/picoCTF_writeups/refs/heads/main/picoCTF-2019/Reverse-Engineering/vault-door-5/img/decoding.png" />
</p>

## Flag

`picoCTF{c0nv3rt1ng_fr0m_ba5e_64_0b957c4f}`