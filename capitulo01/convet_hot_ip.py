
import socket

hostname = 'www.udemy.com'
addr = socket.gethostbyname(hostname)
print('The IP address of {} is {}'.format(hostname, addr))
