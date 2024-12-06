# file-run2

- [Description](#description)
- [Approach](#approach)
- [Flag](#flag)

## Description

Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"? <br>
Download the program [here](https://artifacts.picoctf.net/c/156/run).

## Approach

Executing the file with a single argument, `"Hello!"`, the flag is obtained.

```
$ ./run Hello!
The flag is: picoCTF{F1r57_4rgum3n7_96f2195f}
```

## Flag

`picoCTF{F1r57_4rgum3n7_96f2195f}`