## fixme2.py

This challenge provided `fixme2.py`, which contained a syntax error shown below:

```python
# Check that flag is not empty
if flag = "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
```

From the code, the if statement should be using `==` for comparison instead of `=`. After replacing `=` with `==`, I obtained the flag.

### Flag

`picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}`