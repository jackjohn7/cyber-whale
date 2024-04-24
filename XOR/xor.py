import sys

def read_files(key):
    with open(key, 'rb') as key_fp:
        key_data = bytearray(key_fp.read())
    
    cypher_data = bytearray(sys.stdin.buffer.read())
    return key_data, cypher_data

def decrypt(key, cypher):
    # Convert hexadecimal key to binary for both key and cyphertext
    key_binary = ""
    for byte in key:
        key_binary += format(byte, '08b')

    cypher_binary = ""
    for byte in cypher:
        cypher_binary += format(byte, '08b')

    # Perform XOR decryption
    xored = ""
    for bit1, bit2 in zip(key_binary, cypher_binary):
        if bit1 != bit2:
            xored += "1"
        else:
            xored += "0"

    # Convert binary string to ASCII text
    segments = [xored[i:i+8] for i in range(0, len(xored), 8)]
    ascii_characters = [int(segment, 2) for segment in segments]
    decrypted_text = ''.join(chr(ascii) for ascii in ascii_characters)
    
    return decrypted_text

##### MAIN ####
key = "key"
key_bytes, cypher_bytes = read_files(key)

final = decrypt(key_bytes, cypher_bytes)
print(final)
