from datetime import datetime
import hashlib
from pytz import tz
import glob

# set current time to .now() if not DEBUG
# epoch must be set via file input
epoch = ''
current = datetime.now()
#current = datetime.strptime(current, "%Y %m %d %H %M %S")
DEBUG = True

# given hash_str --> formulates four-character code with
# first two letters from left-to-right 
# first two numbers from right-to-left
def retrive_code(hash_str):
    code = ''
    char_count = 2

    # retrive letters
    for i in hash_str:
        if i.isalpha():
            code += i
            char_count -= 1
        if char_count == 0:
            break
    # retrieve numbers
    num_count = 2
    i = 1
    while(i <= len(hash_str)):
        if hash_str[-i].isalpha() == False:
            code += hash_str[-i]
            num_count -= 1
        if num_count == 0:
            break
        i += 1
    return code

if __name__ == '__main__':

    # take in file input
    files = glob.glob('*.txt')
    for f in files:

        file = open(f, 'r')
        epoch += file.read()

    
    
    # if DEBUG allow current time to be set manually via the command line
    if DEBUG:
        try:
            print("Epoch time: " + epoch + '\n')
            current = input("current time: ")
            print('\n')
        except EOFError:
            print("Eoferror")
        current =  datetime.strptime(current, "%Y %m %d %H %M %S")
        
    # handle DST by converting datetime objects to datetime onjects in local timezone
    epoch = datetime.strptime(epoch, "%Y %m %d %H %M %S")
    epoch = epoch.replace(tzinfo = tz.tzlocal())
    current = current.replace(tzinfo = tz.tzlocal())

    # calculate time elapsed (in seconds)
    difference = int(abs(epoch - current).total_seconds())
    difference -= difference%60 # top of the minute

    # generate hash_str using md5
    hash_str = hashlib.md5(hashlib.md5(str(difference).encode()).hexdigest().encode()).hexdigest()

    # if DEBUG print total seconds and the generated hash string
    if DEBUG:
        print("Total_seconds: " + str(difference) + '\n')
        print("hash_str: " + hash_str + '\n')

    # retrieve the code from hash_str
    code = retrive_code(hash_str)

    print(code + '\n')
    
       
            

    
    