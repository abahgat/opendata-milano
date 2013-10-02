import csv
import geojson

def convert():
  with open('stops.txt', 'r') as stops_file:
    reader = csv.DictReader(stops_file)
    features = {}
    for row in reader:
      stop_id = row['stop_id']
      name = row['stop_name']
      latitude = row['stop_lat']
      longitude = row['stop_lon']
      feature = geojson.Feature(id=stop_id,
                  							geometry=geojson.Point([longitude, latitude]),
                  							properties={'count': 0,
                                            'name': name})
      features[stop_id] = feature
  with open('stop_times.txt', 'r') as times_file:
    reader = csv.DictReader(times_file)
    for row in reader:
      stop_id = row['stop_id']
      features[stop_id].properties['count'] += 1

  collection = geojson.FeatureCollection(features=features.values())
  print geojson.dumps(collection)

if __name__ == "__main__":
  convert()