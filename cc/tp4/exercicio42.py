import socket

target_host = "localhost"
target_port = 9997

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

client.send(b"GET / HTTP/1.1\r\nHost: lms.infnet.edu.br/\r\n\r\n")
response = client.recv(4096)
print(response.decode())
client.close()
