import os
import socket

def parse():
    print("IP address :",socket.gethostbyname(socket.gethostname())+":8000")
    cwd = os.getcwd()  # used by static file server
    print("Current Working directory :" + cwd)

    ipaddress = ""
    if (os.name == "nt"):
        ipaddress = socket.gethostbyname(socket.gethostname())
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ipaddress = s.getsockname()[0]
        s.close()

    onlyfiles = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    for htmlFile in onlyfiles:
        if htmlFile.endswith(".html"):
            # print("------"+os.path.join(cwd,htmlFile))
            file = open(os.path.join(cwd, htmlFile), "r+")
            fileread = file.readlines()
            filewrite = ""
            for line in fileread:
                if line.strip().__contains__(":8000"):
                    arr = line.split(":")
                    str = arr[0]
                    str += "://"
                    str += ipaddress
                    str += ":"
                    str += arr[2]
                    filewrite += str
                else:
                    filewrite += line

            file.seek(0)
            # print(filewrite)
            file.write(filewrite)