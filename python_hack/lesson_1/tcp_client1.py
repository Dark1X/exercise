import socket
target_host="192.168.10.108"
target_port=9999
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send("ASD")
response=client.recv(4096)
print response
