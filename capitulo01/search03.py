
import http.client
import json
from urllib.parse import quote_plus

base = '/maps/api/geocode/json'
key = ''


def geocode(address):
	path = '{}?address={}&sensor=false&key={}'.format(base, quote_plus(address), key)
	connection = http.client.HTTPConnection('maps.google.com')
	connection.request('GET', path)
	rawreply = connection.getresponse().read()
	reply = json.loads(rawreply.decode('utf-8'))
	print(reply)


if __name__ == '__main__':
	geocode('207 N. Defiance St, Archbold, OH')
