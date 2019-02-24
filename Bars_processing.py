import json

bars = []
all_bars = {}
for business in open('yelp_academic_dataset_business.json', 'r'):
    place = json.loads(business)
    if place['categories'] is not None and "Nightlife" in place['categories']:
        all_bars['name'] = place['name']
        all_bars['latitude'] = place['latitude']
        all_bars['longitude'] = place['longitude']
        all_bars['categories'] = place['categories']
        #print(place['name'], place['latitude'], place['longitude'], place['categories'])
        bars.append(all_bars.copy())
print(bars)

with open("bars.json", "w") as outfile:
    json.dump(bars, outfile)
#print(type(json.dumps(bars)))

