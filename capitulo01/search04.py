import socket
from urllib.parse import quote_plus

KEY_API = ''

request_text = """\
GET /maps/api/geocode/json?address={}&sensor=false&key={} HTTP/1.1\r\n
Host: maps.google.com:80\r\n
User-Agent: search04.py (Foundations of Python Network Programming)\r\n
Connection: close\r\n
\r\n
"""


def geocode(address):
	sock = socket.socket()
	sock.connect(('maps.google.com', 80))
	request = request_text.format(quote_plus(address), KEY_API)
	sock.sendall(request.encode('ascii'))
	raw_reply = b''
	while True:
		more = sock.recv(4096)
		if not more:
			break
		raw_reply += more
	print(raw_reply.decode('utf-8'))


if __name__ == '__main__':
	geocode('')
