import codecs
import base64

a = codecs.decode("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d", "hex")
print(a)
b = base64.b64encode(a)
print(b)

