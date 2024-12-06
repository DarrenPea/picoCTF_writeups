# Redaction gone wrong

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Now you DON’T see me.
This [report](https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?

## Approach

Upon downloading the PDF file, I used `pdftotext` to view the all texts in the file. This allowed me to obtain the flag in plaintext.

```
$ pdftotext Financial_Report_for_ABC_Labs.pdf

$ cat Financial_Report_for_ABC_Labs.txt
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
Breakdown - Just painted over in MS word.

Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document.
```

## Flag

`picoCTF{C4n_Y0u_S33_m3_fully}`