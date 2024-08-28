import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))

done = False

while not done:
    message = input('Message: ')
    client.send(message.encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')

    if msg == 'quit':
        done = True
    else:
        print(f"server: {msg}")
client.close()
