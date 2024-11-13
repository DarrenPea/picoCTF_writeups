from pwn import *

io = remote("saturn.picoctf.net", 64703)

while True:
	try:
		question = io.recvline_contains(b'md5 hash').decode()
		question_ls = question.split("'")
		word = question_ls[1]
		io.recvuntil(b'Answer:')
		print(word)
		hashed = md5sumhex(word.encode())
		print(hashed)
		io.sendline(hashed.encode())

		io.recvuntil(b'Correct.')
	except EOFError:
		print(io.recvline_contains(b'picoCTF').decode())
		break

