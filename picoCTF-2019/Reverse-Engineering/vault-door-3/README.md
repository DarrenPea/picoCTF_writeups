# vault-door-3

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/a4018cec1446761cb2e8cce05db925fa/VaultDoor3.java)

## Approach

Analysing the Java code:

```java
public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);		// [0:8] - jU5t_a_s
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);	// [8:16] - 1mpl3_an
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);	// [16:32:2] - [4, r, m, 4, u, c, 9, 2]
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);		// [31:16:-2] - [1, a, 7, _, _, _, 4, g]
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm12g94c_u_4_m7ra41");
    }
```

The password is checked by checking the characters based on their indexes. Putting them together, `jU5t_a_s1mpl3_an4gr4m_4_u_c79a21` is obtained.

## Flag

`picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}`