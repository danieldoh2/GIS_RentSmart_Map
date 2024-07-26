import json 
import urllib.request
import arcpy
import urllib.parse
import pandas

base_url = "https://data.boston.gov/api/3/action/datastore_search_sql?"
# sql_query = 'SELECT * from "dc615ff7-2ff3-416a-922b-f0f334f085d0" LIMIT 5'
sql_query = 'SELECT * from "dc615ff7-2ff3-416a-922b-f0f334f085d0"'

encoded_sql_query = urllib.parse.quote_plus(sql_query)

# Construct the full URL by appending the encoded query
full_url = f"{base_url}sql={encoded_sql_query}"

# url = 'https://data.boston.gov/api/3/action/datastore_search_sql?sql=SELECT * from "dc615ff7-2ff3-416a-922b-f0f334f085d0" WHERE "title" LIKE \'jones\''
fileobj = urllib.request.urlopen(full_url)
# print(type(fileobj))
response_dict = json.loads(fileobj.read())
# print(type(response_dict))
# print(response_dict['result'])

print(len(response_dict['result']['records']))
# for element in response_dict['result']['records']:
#     print(element)
#     print(type(element))



