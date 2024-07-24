import json 
import urllib.request

url = 'https://data.boston.gov/api/3/action/datastore_search?resource_id=dc615ff7-2ff3-416a-922b-f0f334f085d0&limit=5&q=title:jones'  
fileobj = urllib.request.urlopen(url)
print(type(fileobj))
response_dict = json.loads(fileobj.read())
# print(type(response_dict))

for element in response_dict['result']['fields']:
    print(element)
    print(type(element))
# print(type(response_dict['result']['fields']))
# print(response_dict.keys())