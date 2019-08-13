from codecs import encode

def repleating_key_xor(string):
    output = []
    key = ["I", "C", "E"]
    counter = 0
    for byte in bytes(string, "utf-8"):
        if counter > 2:
            counter = 0
        for byte1 in bytes(key[counter], "utf-8"):
            byte_key = byte1
        print(byte, byte_key)
        xor = byte ^ byte_key
        output.append(xor)
        counter = counter + 1
    str_output = "".join(str(e) for e in output)
    str_output = str_output.replace("[", "").replace("]", "")
    str_output = str_output.encode("utf-8")
    str_output.hex()
    print(str_output)


if __name__ == "__main__":
    str1 = '''Burning 'em, if you ain't quick and nimble
        I go crazy when I hear a cymbal'''
    repleating_key_xor(str1)