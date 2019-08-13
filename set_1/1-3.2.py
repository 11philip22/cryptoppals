import codecs
import string

ct = codecs.decode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", "hex")


# for key in range(0, 256):
# 	output = ''
# 	ascii = True
# 	for b in ct:
# 		output += chr(b ^ key)
# 		for letter in output:
# 			if letter not in string.printable:
# 				ascii = False
# 	if ascii == True:
# 			print(repr(output))
# 	# print(output)
	# Bevat output unprintable chars? laat hem dan niet zien anders wel




# for key in range(0, 256):
# 	output = ''
# 	ascii = True
# 	for b in ct:
# 		c = chr(b ^ key)
# 		if c not in string.printable:
# 			ascii =False
# 			break
# 		output += c
# 	if ascii == True:
# 			print(repr(output))
# 	# print(output)

# mydict = {}
# with open("/home/philip/boek.txt", "rb") as fd:
# 	for line in fd:
# 		for c in line:
# 			c = chr(c)
# 			c = c.lower()
# 			if c not in mydict.keys():
# 				mydict[c] = 1
# 			else:
# 				mydict[c] += 1

def xor(message, key='a'):
	output = ''
	for b in message:
		output += chr(b ^ key)
	return output

def checkascii(message):
	for b in message:
		if b not in string.printable:
			return False
	return True

for key in range(0, 256):
	output = xor(ct, key)
	if checkascii(output):
		print(output)