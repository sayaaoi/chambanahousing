import re
from geopy.geocoders import Nominatim
f = open('address_apartments.txt')
addresses = []
geolocator = Nominatim(user_agent="specify_your_app_name_here")
for line in f:
    addresses += line.strip('\n').split('  ')
# print(addresses)
coordinates = []
for address in addresses:
    if len(address) > 0:
        if address[0].isdigit():
            try:
                location = geolocator.geocode(address)
            except:
                raise Exception('This address is not valid({}).'.format(address))
            if location is not None:
                print(str(location.longitude).strip()+ ','+str(location.latitude).strip()+';')
       