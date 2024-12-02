message = ''
with open('message.txt', 'r') as f:
	message = f.read()

decrypted_text = ''

for i in range(0,len(message),3):
	decrypted_text += message[i+2]
	decrypted_text += message[i]
	decrypted_text += message[i+1]

print(decrypted_text)