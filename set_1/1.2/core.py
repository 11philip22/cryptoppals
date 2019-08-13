def xor_two_str(input_1, input_2):
    xord_bytes = b""
    for b1, b2 in zip(input_1, input_2):
        xord_bytes += (bytes([b1 ^ b2]))
        print(xord_bytes)
    return xord_bytes


key = bytes.fromhex("686974207468652062756c6c277320657965")
string = bytes.fromhex("1c0111001f010100061a024b53535009181c")

print(xor_two_str(key, string).hex())
