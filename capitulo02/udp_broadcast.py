
import socket
import argparse

BUFSIZE = 65535


def server(interface, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((interface, port))
	print('Listening for datagrams at {}'.format(sock.getsockname()))
	
	while True:
		data, address = sock.recvfrom(BUFSIZE)
		text = data.decode('ascii')
		print('The client at {} says: {!r}'.format(address, text))
		

def client(network, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	text = 'Broadcast datagram!'
	sock.sendto(text.encode('ascii'), (network, port))


if __name__ == '__main__':
	choices = {'client': client, 'server': server}
	parser = argparse.ArgumentParser(description='send, receive UDP broadcast')
	parser.add_argument('role', choices=choices, help='which role to take')
	msg = 'interface the server listens at: network the client send to'
	parser.add_argument('host', help=msg)
	parser.add_argument('-p', metavar='port', type=int, default=1060, help='UDP port (default 1060)')
	args = parser.parse_args()
	function = choices[args.role]
	function(args.host, args.p)
