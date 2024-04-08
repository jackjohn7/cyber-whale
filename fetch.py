from ftplib import FTP

def extact_permissions(listings: list[str]) -> list[str]:
    permissions = []
    for file in listings:
        temp = file.split()
        permissions.append(temp[0])
    return permissions






##### MAIN #####

IP = "138.47.165.156"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/"
USE_PASSIVE = True 
METHOD = True

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

permissions = extact_permissions(files)
for i in permissions:
    print(i)

	
