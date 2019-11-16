import socket

url = input('Enter url to connect to"\n>')
url_parts = url.split('/')
if len(url_parts) < 2:
    print('ERROR: Please enter a full url path including http or https')
    exit()
host = url_parts[2]
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysocket.connect((host, 80))
except:
    print('ERROR: URL not found or is invalid!')
    exit()
cmd = f'GET %s HTTP/1.0\r\n\r\n'%url
mysocket.send(cmd.encode())
characters_sent = 0
while True:
    data = mysocket.recv(100)
    if len(data) < 1 or characters_sent == 3000:
        break
    characters_sent += len(data)
    print(data.decode(), end='')
    print('\n',characters_sent)
mysocket.close()
