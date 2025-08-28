import sys
import socket
import threading
import os
from termcolor import colored

name = ""

def connect(s):
    while True:
        r_msg = s.recv(1024)
        if not r_msg:
            break
        if r_msg == '':
            pass
        else:
            print(r_msg.decode())

def receive(s):
    while True:
        s_msg = input().replace('b', '').encode('utf-8')
        if s_msg == '':
            pass
        if s_msg.decode() == 'exit':
            print("wan exit")
            break
        else:
            s.sendall(bytes(name, 'utf-8') + b':' + s_msg)

def start(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((ip, int(port)))
    thread1 = threading.Thread(target = connect, args = ([s]))
    thread2 = threading.Thread(target = receive, args = ([s]))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

def init():
    os.system('color')

    global name
    name = input("Enter your alias:")

    ip = input("Target ip:")
    port = input("Target port:")

    start(ip, port)


if __name__ == '__main__':
    init()


