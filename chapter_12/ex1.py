import socket

url = input('Enter url to connect to:\n>')
url_parts = url.split('/')
host = url_parts[2]
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysocket.connect((host, 80))
except:
    print('ERROR: URL MALFORMED OR NONEXISTANT!')
    exit()
cmd = f'GET %s HTTP/1.0\r\n\r\n'%url
mysocket.send(cmd.encode())
while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysocket.close()
