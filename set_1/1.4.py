from string import ascii_lowercase

# file = open("4.txt", "r")
	
for line in file:
	decoded_line = codecs.decode(line, 'hex')
	for c in ascii_lowercase:
		print(decoded_line ^ ord(c))
		

		# ding = hex(int(line,16) ^ int(c,16))
		# print(bytes.fromhex(ding).decode('utf-8'))
		# print(hex(int(line,16) ^ ord(c)))

for c in ascii_lowercase:
	print(c)