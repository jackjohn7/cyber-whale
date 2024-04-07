import ftplib
from ftplib import FTP

# MODE can be Timo_Server or one we make ourself
MODE = 'Timo_Server'

# Server adress (default = Timo_Server address)
ip_address = '138.47.165.156'
f_d_list = []

# Method can be either '7' or '10' for 7-bit method and 10-bit method
METHOD = '7'

# adds the permissions of each file in the cwd to a list
def add_file(file):

    # only interest in last 7 bits of permissions
    if METHOD == '7':
        f_d_list.append(file[3:10])

    # only interested in the permissions of each file/directory
    elif METHOD == '10':
        f_d_list.append(file[:10])

# takes in the permissions list and converts into binary then to acsii value
def convert_binary(perm_list):
    binary_list = []

    # parse list if 10-bit method (each permission is not a stand alone char)
    if len(perm_list[0]) == 10:
        perm_list = convert_10_bit(perm_list)

    # convert each permission to binary
    for perm in perm_list:
        bin = ''
        for p in perm:
            if p == '-':
                bin += '0'
            else:
                bin += '1'
        # convert to ascii value
        binary_list.append(int(bin,2))

    return binary_list

# given a list of ascii values, converts to corresponding chars
def convert_ascii(bin_list):
    ascii_list = []
    for bin in bin_list:
        ascii_list.append(chr(bin))
    return ascii_list

# used for 10-bit method
# places all permission values into a list and then separates into 
# 7-bit chunks in prep for convert_binary()
def convert_10_bit(perm_list):
    length = 7
    full_message=''.join(str(perm) for perm in perm_list)

    parsed_string = (full_message[0+i:length+i] for i in range(0, len(full_message), length))   
    
    return(parsed_string)


def main():

    # connect to ftp server
    # password not needed for anonymous connection
    ftp = FTP(ip_address)
    ftp.login()

    # change directory: 7 for 7-bit method, 10 for 10-bit method (Timo's Server)
    ftp.cwd(METHOD) 

    ftp.dir(add_file)
    #ftp.dir()
    ftp.close()
    
    perm_list = convert_binary(f_d_list)
    ascii_list = convert_ascii(perm_list)

    message= ''.join(str(char) for char in ascii_list)

    # print the generated string (only output)
    print(message)
main()