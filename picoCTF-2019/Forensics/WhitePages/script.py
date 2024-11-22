with open('whitepages.txt', 'rb') as f:
	data = f.read()
	data = data.replace(b'\xe2\x80\x83', b'0')
	data = data.replace(b'\x20', b'1')
	data_int = int(data, 2)
	data_str = data_int.to_bytes((data_int.bit_length() + 7) // 8, 'big').decode()

print(data_str)