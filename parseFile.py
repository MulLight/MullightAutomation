import os
import socket
import netifaces as ni

def parse():

    ipaddress = ""
    for interface in ni.interfaces():
        try:
            if not ni.ifaddresses(interface)[ni.AF_INET][0]['addr'].__contains__("127"):
                ipaddress = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
        except KeyError as k:
            if k == 2:
                pass

    print("IP address :",socket.gethostbyname(socket.gethostname())+":8000")
    cwd = os.getcwd()  # used by static file server
    print("Current Working directory :" + cwd)

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