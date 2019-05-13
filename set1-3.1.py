import codecs
import string

ct = codecs.decode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", "hex")


for key in range(0, 256):
	output = ''
	for b in ct:
		output += chr(b ^ key)
		for letter in output:
			if letter in string.printable:
				print(output)
	
	# print(output)
	# Bevat output unprintable chars? laat hem dan niet zien anders wel