import sys

# take in the message and key. xor_message is a bytearray 
def xor(message, key):
    xor_message = bytearray()
    # xor each bit in message to corresponding bit in key.
    # if the key is shorter than the message, it is repeated
    for i in range(len(message)):
        xor_message.append(message[i] ^ key[i % len(key)])
    return xor_message

###### MAIN #######
# Read key file and adjust "key" or "key2"
with open("key", "rb") as key_file:
    key = bytearray(key_file.read())

# Read message from stdin and pass through xor function with key
text = sys.stdin.buffer.read()
final = xor(text, key)

# output the final message
sys.stdout.buffer.write(final)
