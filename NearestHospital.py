import redis
import pandas as pd
from googleplaces import GooglePlaces, types, lang
import requests
import json
import geocoder
from urllib.parse import urlencode

from requests.models import Response

#hospitals= pd.read_csv("C:/Users/Dell/Documents/SRH_Course/DataEngineering1/Yellow/shruthi/HospitalData.csv")
#hospitals.head()


# Initialising the GooglePlaces constructor


def AddHospitals(ApiKey,Mannheim_lat,Mannheim_lng,redis_connection):
#placed geo co-ordinates for  Mannheim=49.4875° N, 8.4660° E
 placeapi_base_url="https://maps.googleapis.com/maps/api/place/nearbysearch/json"
 params = { 
           "location": f"{Mannheim_lat},{Mannheim_lng}",
            "radius":20000,
            "type":"hospital",
            "language": "en",
            "key": ApiKey,
            "sensor":"true"}
 url_params = urlencode(params)
 url = f"{placeapi_base_url}?{url_params}"
 print("url")
 url=url+'&opennow'
 print(url)
 #Making call to google APis
 response=0
 response = requests.get(url)
 print("status code")
 print(response.status_code)
 #print(len(result.json()['results']))
 if response.status_code in range(200, 299):  
    print(requests)  
    hospital_iterator = iter(response.json()[results])
    try:
      for hospital in hospital_iterator:
        if hospital is not None:
          geometry_coordinates = hospital[geometry]
          if geometry_coordinates is not None:
           location_coordinates=geometry_coordinates[location]
           name=hospital['name']
           print(name)
           opening_hours=hospital['opening_hours']           
           print(opening_hours)
           if opening_hours is not None:
             open_now=opening_hours['open_now']
             #check if hospital is open at that time 
             print(open_now)
             if open_now==True :
              redis_connection.geoadd(main_key_for_db, location_coordinates['lat'],location_coordinates['lng'],name)
    except KeyError:
      print("Oops!  Try again...")
      print(KeyError)



def getAddress(place, redis_connection):
  address=redis_connection.get(place)
  return address
  

def geoCordinates(place, address,Apiy_key,redis_connection):
  geocode_base_url="https://maps.googleapis.com/maps/api/geocode/json"
  params = {             
           "key": Apiy_key,
            }
  #for key, value in places_mannheim.items():
  print("iterating over key and value")
  params['address']=address
  url_params = urlencode(params)
  url = f"{geocode_base_url}?{url_params}"
  print("url")
  print(url)
  try:
    response= requests.get(url)
    if response.status_code in range(200, 299):
      location= response.json()['results'][0]['geometry']['location']
      print(location)
      name=response.json()['results'][0]['address_components'][0]['long_name']
      print(name)
      redis_connection.geoadd(main_key_for_db, location['lat'],location['lng'],place)
  except:
    print("Oops! That was no valid number.  Try again...")

def searchNearByHospital(place,redis_connection):
 increments=[1,5,10,50]
 for i in increments:
  print(i)
  search_results=redis_connection.georadiusbymember(main_key_for_db , place, i, unit="km")
  for j in range(0, len(search_results)):
    search_results[j]=(search_results[j]).decode('UTF-8')
  if place in search_results:
    search_results.remove(place)
  if(len(search_results)>0):
   search_results=set(search_results)
   return search_results
  
  elif(len(search_results)==0):
    continue
 
  return search_results



#start 

redis_connection = redis.Redis(port=6379)
API_KEY = 'AIzaSyCl4WcOwBQrQ51RtZ8l3M-ioEYs9ooXqNo'
Mannheim_lat, Mannheim_lng = 49.488888, 8.469167
results='results'
geometry='geometry'
location='location'
opening_hours='opening_hours'
main_key_for_db='hospitals:Mannheim'
main_key_for_places='places:Mannheim'


#Using Mannhheaim's cordinates get all hospitals in Mannheim calling Google Search API
AddHospitals(API_KEY,Mannheim_lat,Mannheim_lng,redis_connection)

places_mannheim={
      
       #'jungbusch':'jungbusch,Hafenstrasse, 68159 Mannheim',
        'Richard-Wagner-Str':'Richard-Wagner-Str 4, 68165 Mannheim'   ,
        'Friedrichsplatz':'Friedrichsplatz, 68165 Mannheim'  
     #   'AmSteingarten':'AmSteingarten 14, 68169 Mannheim'
}


place="Friedrichsplatz"

address=getAddress(place,redis_connection)

geoCordinates(place,address,API_KEY,redis_connection)


search_results=searchNearByHospital(place,redis_connection)
print('final search results')
for i in search_results:
  print(i)
 
