from pwn import *

CONN = remote('jupiter.challenges.picoctf.org', 29221)

for i in range(3):
	CONN.recvuntil(b'the ')
	question = CONN.recvuntil(b' as a word').decode().strip().split(' ')[:-3]
	CONN.recvuntil(b'Input:')
	ascii_str = ''
	print(question)
	if i == 0:
		for num in question:
			ascii_str += chr(int(num, 2))
	elif i == 1:
		for num in question:
			ascii_str += chr(int(num, 8))
	elif i == 2:
		for num in question:
			ascii_str = bytearray.fromhex(num).decode()
	print(ascii_str)
	CONN.sendline(ascii_str.encode())

print(CONN.recvall().decode())