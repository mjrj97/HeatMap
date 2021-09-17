from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="HeatMap")

file = open('Addresses.txt', 'r', encoding="UTF-8")
addresses = file.readlines()

latitudes = [0] * len(addresses)
longitudes = [0] * len(addresses)

if len(addresses) > 0:
	for idx, x in enumerate(addresses):
		location = geolocator.geocode(x)
		latitudes[idx] = location.latitude
		longitudes[idx] = location.longitude

	print("Latitudes:")
	for x in latitudes:
		print(x)

	print("\nLongtitudes:")
	for x in longitudes:
		print(x)
else:
	print("No addresses found.")