import string


frequency = {}
text = ""
with open("cipher.txt", mode="r") as t:
	text = t.read()
	for char in string.printable:
		frequency[char] = 0
	for char in text:
		frequency[char] += 1

	sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
	to_remove = []
	for tuple in sorted_frequency:
		if tuple[0] in {" ", ",", ".", "-", "\n"}:
			to_remove.append(tuple)
	for tuple in to_remove:
		sorted_frequency.remove(tuple)

	print(sorted_frequency)
	
	## [('o', 79), ('h', 77), ('c', 76), ('r', 63), ('l', 59), ('q', 52), ('m', 48), 
	## ('j', 46), ('v', 42), ('u', 32), ('y', 32), ('x', 29), ('i', 24), ('e', 23), 
	## ('a', 22), ('b', 19), ('f', 14), ('k', 13), ('g', 12), ('t', 12), ('z', 11), 
	## ('w', 8), ('_', 5), (';', 3), ('p', 2), ('d', 1), ('n', 1), ('s', 1), ('0', 0),
	## ('1', 0), ('2', 0), ('3', 0), ('4', 0), ('5', 0), ('6', 0), ('7', 0), ('8', 0),
	## ('9', 0), ('A', 0), ('B', 0), ('C', 0), ('D', 0), ('E', 0), ('F', 0), ('G', 0),
	## ('H', 0), ('I', 0), ('J', 0), ('K', 0), ('L', 0), ('M', 0), ('N', 0), ('O', 0),
	## ('P', 0), ('Q', 0), ('R', 0), ('S', 0), ('T', 0), ('U', 0), ('V', 0), ('W', 0),
	## ('X', 0), ('Y', 0), ('Z', 0), ('!', 0), ('"', 0), ('#', 0), ('$', 0), ('%', 0),
	## ('&', 0), ("'", 0), ('(', 0), (')', 0), ('*', 0), ('+', 0), ('/', 0), (':', 0),
	## ('<', 0), ('=', 0), ('>', 0), ('?', 0), ('@', 0), ('[', 0), ('\\', 0), (']', 0),
	## ('^', 0), ('`', 0), ('{', 0), ('|', 0), ('}', 0), ('~', 0), ('\t', 0), ('\r', 0),
	## ('\x0b', 0), ('\x0c', 0)]

	## original cipher frequency list
	## cipher_frequency_list = ['o', 'h', 'c', 'r', 'l', 'q', 'm', 'j', 'v', 'u', 'y', 'x', 'i', 'e', 'a', 'b', 'f', 'k', 'g', 't', 'z', 'w', 'p', 'd', 'n', 's']

	## manually adjusted frequency list
	cipher_frequency_list = ["o", "c", "h", "r", "q", "l", "j", "m", "v", "y", "x", "e", "a", "u", "b", "g", "k", "f", "i", "z", "t", "w", "p", "n", "d", "s"]

	## list sorted based on frequency of letters in an English Corpus
	usual_frequency_list = ["E", "T", "A", "O", "I", "N", "S", "R", "H", "L", "D", "C", "U", "M", "F", "P", "G", "W", "Y", "B", "V", "K", "X", "J", "Q", "Z"]
	
	for i in range(len(usual_frequency_list)):
		text = text.replace(cipher_frequency_list[i], usual_frequency_list[i])
	
file_path = "solution.txt"
with open(file_path, mode="w") as f:
		f.write(text)

print(text)