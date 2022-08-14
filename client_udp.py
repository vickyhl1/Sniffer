import socket
import time
import random
import math
import socket
from time import sleep
import sys
import os
from time import sleep as pause
from itertools import cycle
import random
import argparse

def check_sum(my_list):
    e=[]
    x=[]
    new = '0'.encode('utf-8')
    for i in range(0, len(message)-2, 4):
        e.append(message[i:i + 4])

    for i in my_list:
        x.append(i)

    for i in range(0,len(x)):
        a = x[i]
        a = str(a).encode('utf-8')
        new = bytes([new ^ a for new, a in zip(new, cycle(a))])
    return new

#udp client

SERVER_IP = "127.0.0.1"
PORT = 12321
MAX_SIZE = 100
message="Lord Voldemort: [Deleted scene] Why do you live? Harry Potter: Because I have something worth living for. Lord Voldemort: There is no good and evil. There is only power... and those too weak to seek it. Harry's Modesty ""But I Am The Chosen One."
d = random.randint(2,11)
my_list = []
e = '0'.encode('utf-8')

for i in range(0, len(message)-2, 4):
    my_list.append(message[i:i + 4])
e = check_sum(my_list)
main_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("the client is ready")
while(1):
    #sending all messsages
    for i in my_list:
        main_socket.sendto(i.encode(), (SERVER_IP, PORT))
    main_socket.sendto(str(d).encode(), (SERVER_IP, PORT)) #sending d num
    main_socket.sendto(str(e).encode(), (SERVER_IP, PORT)) #sending e (check_sum)
    (response, remote_address) = main_socket.recvfrom(MAX_SIZE)
    recived_msg = response.decode()
    print("The server recived " + recived_msg)
    # message = raw_input("Input: \n")
    time.sleep(3)

main_socket.close()

