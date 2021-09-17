import gmplot
import os.path
from os import path
from geopy.geocoders import Nominatim

peopleExist = path.exists("People.txt")
addressesExist = path.exists("Addresses.txt")

if peopleExist:
	peopleFile = open('People.txt', 'r', encoding="UTF-8")
	people = peopleFile.readlines()
	print("Found People.txt")

	pLatitudes = [0] * len(people)
	pLongitudes = [0] * len(people)
else:
	print("Error: Could not find People.txt in folder")

if addressesExist:
	addressesFile = open('Addresses.txt', 'r', encoding="UTF-8")
	addresses = addressesFile.readlines()
	print("Found Addresses.txt")

	aLatitudes = [0] * len(addresses)
	aLongitudes = [0] * len(addresses)
else:
	print("Error: Could not find Addresses.txt in folder")

if peopleExist & addressesExist:
	print(len(people))
	print(len(addresses))
	if len(people) > 0:
		geolocator = Nominatim(user_agent="HeatMap")

		print("Loading people into map...")
		for idx, x in enumerate(people):
			location = geolocator.geocode(x)
			if location is None:
				print("Error: " + people[idx], end='')
			else:
				print("Loaded: " + people[idx], end='')
				pLatitudes[idx] = location.latitude
				pLongitudes[idx] = location.longitude

		print("Loading addresses into map...")
		for idx, x in enumerate(addresses):
			location = geolocator.geocode(x)
			if location is None:
				print("Error: " + addresses[idx], end='')
			else:
				print("Loaded: " + addresses[idx], end='')
				aLatitudes[idx] = location.latitude
				aLongitudes[idx] = location.longitude

		gmap = gmplot.GoogleMapPlotter(pLatitudes[0], pLongitudes[0], 13)
		gmap.heatmap(pLatitudes, pLongitudes, radius=75, opacity=0.3, max_intensity=5, dissipating = False)
		gmap.scatter(aLatitudes, aLongitudes, c='#3B0B39', size = 40, marker = False )
		gmap.draw("C:\\Users\\marti\\Desktop\\map.html")
	else:
		if len(people) == 0:
			print("No people in People.txt")
		if len(addresses) == 0:
			print("No addresses in Address.txt")