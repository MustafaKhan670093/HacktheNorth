from ipstack import GeoLookup
geo_lookup = GeoLookup("367b4e6fe41e712cfd85feb52af4cb11")
location = geo_lookup.get_own_location()
print(location.get('latitude'))
print(location.get('longitude'))
