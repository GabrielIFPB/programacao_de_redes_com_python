
import requests


def geocode(address):
	parameters = {'address': address, 'sensor': 'false', 'key': 'AIzaSyAPQ4GzOmytPQ8TO0I4eXaKiGwo95ENLDw'}
	base = 'https://maps.googleapis.com/maps/api/geocode/json'
	response = requests.get(base, params=parameters)
	answer = response.json()
	print(answer)
	print(answer['results'][0]['geometry']['location'])


if __name__ == '__main__':
	geocode('207 N. Defiance St, Archbold, OH')
