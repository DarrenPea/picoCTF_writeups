# Shop

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](https://mercury.picoctf.net/static/db20ea321ce780e69e29fd4b60e60fe0/source). The shop is open for business at `nc mercury.picoctf.net 3952`.

## Approach

It seems that we need to purchase the Fruitful Flag which costs 100 coins, but we only have 40 coins.

```
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
```

After trying to purchase a negative quantity of Quiet Quiches and Average Apple, it allowed me to gain money. This is due to the lack of checking whether the quantity purchased is negative, and subtracting a negative value from the total coins will increase the number of coins.

After purchasing -100 Quiet Quiches, I bought the Fruitful Flag.

```
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 57 99 49 49 56 98 98 102 125]
```

Using [Cyberchef](https://cyberchef.org/#recipe=From_Decimal('Space',false)&input=MTEyIDEwNSA5OSAxMTEgNjcgODQgNzAgMTIzIDk4IDUyIDEwMCA5NSA5OCAxMTQgMTExIDEwMyAxMTQgOTcgMTA5IDEwOSAxMDEgMTE0IDk1IDU3IDk5IDQ5IDQ5IDU2IDk4IDk4IDEwMiAxMjU) to convert these decimals to ASCII, I obtained the flag.

## Flag

`picoCTF{b4d_brogrammer_9c118bbf}`