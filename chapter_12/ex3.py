import urllib.request, urllib.parse, urllib.error

data = urllib.request.urlopen('http://data.pr4e.org')
size = 0
while True:
    info = data.read(3000)
    if len(info) < 1 or size >= 3000: break
    size += len(info)

print(size, 'characters read')
