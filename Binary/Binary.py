import sys

# reads file and removes new lines that unnecessarily disrupt bit stream
def read_file():
    input_data = sys.stdin.read().replace('\n', '')
    return input_data

# checks stream length to determine which approach to take (7 or 8)
# if both or neither (i.e.; 56 then returns None)
def numBits(text):
    if len(text) % 8 == 0:
        return 8
    elif len(text) % 7 == 0:
        return 7
    elif len(text) % 8 & len(text) % 7:
        return None
    else:
        return None

# breaks the stream into segments placed into a list. Segment size is taken as an argument
# and used in range.
def segments(stream, size):
    lis = []
    for i in range(0, len(stream), size):
        segment = stream[i:i + size]
        lis.append(segment)
    return lis

# converts each segemnt from binary to ACSII then concats each ASCII value to a new string
def toASCII(segments):
    lis = []
    for i in segments:
        ascii = int(i,2)
        lis.append(ascii)

    text = ''.join(chr(ascii) for ascii in lis)
        
    return text


### MAIN ###
if __name__ == "__main__":
    contents = read_file()
    num = numBits(contents)
    if num != None:
        segment_list = segments(contents, num)
        print(toASCII(segment_list))
    else:
        print("Warning: Check Bit Stream")
