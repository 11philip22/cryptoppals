import codecs

inputa = "1c0111001f010100061a024b53535009181c"
inputb = "686974207468652062756c6c277320657965"

a = codecs.decode(inputa, "hex")
b = codecs.decode(inputb, "hex")

c = b""

for count in range(0,18):
	c += bytes([a[count] ^ b[count]])

print(codecs.encode(c, "hex"))
