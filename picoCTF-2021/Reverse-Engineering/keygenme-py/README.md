# keygenme-py

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

[keygenme-trial.py](https://mercury.picoctf.net/static/b016c61bd2cc0be05a59da1dde67a2ac/keygenme-trial.py)

## Approach

Analysing the code provided, it seems that the license key is the flag, and the `check_key` function verifies the content of our flag. We know that the flag begins with `picoCTF{1n_7h3_|<3y_of_>` and ends with `}`.

In the `check_key` function, it hashes the trial username, `GOUGH` using SHA256, and obtain the missing 8 characters of the flag through indexing.

SHA256 sum of `GOUGH`: `e8a1f9146d32473b9605568ca66f7b5c2db9f271f57a8c8e9e121e48accddf2f`

After matching the indexes from the SHA256 sum to the license key, I obtained `f911a486`.

## Flag

`picoCTF{1n_7h3_|<3y_of_f911a486}`