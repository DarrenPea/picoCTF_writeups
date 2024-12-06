def calc_mod_inv(x):
	for y in range(1, 41):
		if (x * y) % 41 == 1:
			return y
	return None

with open("message.txt", "r") as f:
	message = f.read().strip().split(" ")

flag = ""
char_map = "abcdefghijklmnopqrstuvwxyz0123456789_"

for num in message:
	num = int(num)
	mod_41 = num % 41
	mod_inv = calc_mod_inv(mod_41)
	flag += char_map[mod_inv - 1]

print(flag)