
from pygeocoder import Geocoder


if __name__ == '__main__':
	address = '207 N. Defiance St, Archbold, OH'
	key_api = ''
	print(Geocoder(key_api).geocode(address)[0].coordinates)
