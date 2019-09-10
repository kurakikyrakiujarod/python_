import socket

client = socket.socket()
HOST, PORT = '127.0.0.1', 9999
client.connect((HOST, PORT))
while True:
    send_msg = input('>>>').strip()
    if not send_msg:
        continue
    client.send(send_msg.encode('utf-8'))
    rec_msg = client.recv(1024).decode('utf-8')
    if rec_msg == 'Q':
        break
    print(rec_msg)

client.close()
