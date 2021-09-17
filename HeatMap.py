import gmplot
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="HeatMap")

file = open('Addresses.txt', 'r', encoding="UTF-8")
addresses = file.readlines()

latitudes = [0] * len(addresses)
longitudes = [0] * len(addresses)

if len(addresses) > 0:
	for idx, x in enumerate(addresses):
		location = geolocator.geocode(x)
		if location is None:
			print("Error: " + addresses[idx], end='')
		else:
			print("Loaded: " + addresses[idx], end='')
			latitudes[idx] = location.latitude
			longitudes[idx] = location.longitude

	gmap = gmplot.GoogleMapPlotter(latitudes[0], longitudes[0], 13)
	gmap.heatmap(latitudes, longitudes, radius=75, opacity=0.3, max_intensity=5, dissipating = False)
	gmap.draw("C:\\Users\\marti\\Desktop\\map.html")
else:
	print("No addresses found.")