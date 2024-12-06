with open('enc', 'r') as f:
	enc = f.read()

flag = ''

for letter in enc:
	pair_value = ord(letter)
	first_value = pair_value >> 8
	second_value = pair_value & 0xff
	flag += chr(first_value)
	flag += chr(second_value)

print(flag)