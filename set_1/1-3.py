'''
a wordt tegen ascii tabel gexored. 
de output daarvan wordt bekeken hoeveel letters ervan er voorkomen in  "ETAOIN SHRDLU".
iedere keer dat een "ETAOIN SHRDLU" letter voorkomt is een punt. 
de output strings met hun punten aantal worden in een dictonary gezet. 
dan is de string met het hoogste puntenaantal waarschijnlijk het antwoord.
'''

import codecs

'''input string vanuit hex decoden'''
a = codecs.decode("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736", "hex")
b = 


c = b""
for count in range(0,34):
	c += bytes([a[count] ^ b[count]])


''' a xor tegen b'''
#c = b""
#for count in range(0,34):
#	c += bytes([a[count] ^ b[count]])

'''lijst met meest voorkomende letters'''
d = [E, T, A, O, I, S, H, R, D, L, U]