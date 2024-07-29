import json 
import urllib.request
import arcpy
import urllib.parse
import pandas
import multiprocessing


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




def query_iterator(length):
    
    num_remainder = length % 32000
    full_queries = int(length / 32000)
    start_index = 1
    end_index = 0
    for i in range(1, full_queries + 1):
        if i == div + 1 #Last iteration, including the remainders
           retrieve_data(start)
        else:
            if start_index = 1:
                start_index += 1
                pass
            else:
                start_index = end_index #resetting start_index back to 0
                end_index += 32000
                retrieve_data(start_index, end_index, False)

def retrieve_data(start, end, last):
    if last == True:
        sql_query = 'SELECT * from "dc615ff7-2ff3-416a-922b-f0f334f085d0" WHERE (_id > {starter})'.format(starter = start)
        encoded_sql_query = urllib.parse.quote_plus(sql_query)

        # Construct the full URL by appending the encoded query
        full_url = f"{base_url}sql={encoded_sql_query}"

        fileobj = urllib.request.urlopen(full_url)
        response_dict = json.loads(fileobj.read())      
        
    else:
        sql_query = 'SELECT * from "dc615ff7-2ff3-416a-922b-f0f334f085d0" WHERE (_id > {starter}) AND (_id < {ender})'.format(starter = start, ender = end)





