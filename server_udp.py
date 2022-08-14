import socket
from tabnanny import check
from itertools import cycle

def check_e(x):
    new = '0'.encode('utf-8')
    for i in range(0,len(x)):
        a = x[i]
        a = str(a).encode('utf-8')
        new = bytes([new ^ a for new, a in zip(new, cycle(a))])
    return new

SERVER_IP ="127.0.0.1"
PORT = 12321
MAX_SIZE = 100
recived_msg="start"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_IP, PORT))
print("Server is up")
s_list=[]
#delete while?
while(True):
    d = None
    (client_message, client_address) = server_socket.recvfrom(MAX_SIZE)
    recived_msg = client_message.decode()
    if recived_msg is not int:
        s_list.append(recived_msg)
    elif isinstance(recived_msg, int):
        d=recived_msg
    else:
        check_sum = recived_msg
    print("Client sent: " + recived_msg)
    response =  recived_msg
    server_socket.sendto(response.encode(), client_address)
    if(d==len(s_list)):
        print("All messeges recieved!")
    else:
        mis_msg = check_e(s_list)
        print("Not all messeges recieved\n The missing message is: ", mis_msg)

    

# keeps all messages in array -Done
# wait for checksum message to stop reading - ?
# check d value and count the messages we saved -Done
# take checksum and xor it with all the messages we got - we should get the lost message -Done 