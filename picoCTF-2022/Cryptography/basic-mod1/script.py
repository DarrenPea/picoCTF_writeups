with open('message.txt', 'r') as f:
	message = f.read().strip().split(" ")

flag = ""
char_map = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

for num in message:
	num = int(num)
	mod_37 = num % 37
	flag += char_map[mod_37]

print(flag)