import urllib.parse
import urllib.request
import json

def grab_length():
    try:
        base_url = "https://data.boston.gov/api/3/action/datastore_search_sql?"
        sql_query = 'SELECT COUNT(*) from "dc615ff7-2ff3-416a-922b-f0f334f085d0"'
        encoded_sql_query = urllib.parse.quote_plus(sql_query)
        
        # Construct the full URL by appending the encoded query
        full_url = f"{base_url}sql={encoded_sql_query}"
        
        print(f"Fetching total length from: {full_url}")
        fileobj = urllib.request.urlopen(full_url)
        response_dict = json.loads(fileobj.read())
        
        # Check if the expected keys are in the response
        if 'result' in response_dict and 'records' in response_dict['result']:
            count = int(response_dict['result']['records'][0]['count'])
            print(f"Total entries count: {count}")
            return count
        else:
            print("Unexpected response structure in grab_length")
            return 0

    except (urllib.error.URLError, json.JSONDecodeError, KeyError) as e:
        print(f"Error retrieving length: {e}")
        return 0

def retrieve_data(start, end=None, last=False):
    try:
        base_url = "https://data.boston.gov/api/3/action/datastore_search_sql?"
        
        if last:
            sql_query = f'SELECT * from "dc615ff7-2ff3-416a-922b-f0f334f085d0" WHERE _id > {start}'
        else:
            sql_query = f'SELECT * from "dc615ff7-2ff3-416a-922b-f0f334f085d0" WHERE _id >= {start} AND _id < {end}'
        
        encoded_sql_query = urllib.parse.quote_plus(sql_query)

        # Construct the full URL by appending the encoded query
        full_url = f"{base_url}sql={encoded_sql_query}"

        print(f"Retrieving data from: {full_url}")
        fileobj = urllib.request.urlopen(full_url)
        response_dict = json.loads(fileobj.read())
        
        if 'result' in response_dict and 'records' in response_dict['result']:
            records = response_dict['result']['records']
            print(f"Retrieved {len(records)} records from index {start} to {end if end else 'end'}")
            return records
        else:
            print("Unexpected response structure in retrieve_data")
            return []

    except (urllib.error.URLError, json.JSONDecodeError, KeyError) as e:
        print(f"Error retrieving data: {e}")
        return []

def query_iterator(all_entries_list):
    length = grab_length()
    
    # Check if length was successfully retrieved
    if length == 0:
        print("Failed to retrieve data length.")
        return []

    num_remainder = length % 32000
    full_queries = length // 32000
    start_index = 0
    end_index = 0

    for i in range(1, full_queries + 1):
        start_index = end_index  # Setting start_index from the ending point
        end_index = start_index + 32000
        print(f"Executing query from index {start_index} to {end_index}")
        entries = retrieve_data(start_index, end_index, last=False)
        all_entries_list.extend(entries)
        
    if num_remainder > 0:
        # Handle remaining entries if the total length is not an exact multiple of 32000
        print(f"Executing last query from index {end_index}")
        entries = retrieve_data(end_index, last=True)
        all_entries_list.extend(entries)

    print(f"Total entries retrieved: {len(all_entries_list)}")
    geo_json_transformation(all_entries_list)
    # return all_entries_list
    # export_to_json(all_entries_list)


def geo_json_transformation(data: list) -> list:
    '''
    Loops through data, creates new features from old data features, preparing them for GeoJSON.

    Args:
        data (list): list of dictionaries, where each dictionary is a feature
    
    Returns:
        new_data(list): List of dictionaries with extra geojson keys added
    '''

    geojson_data = {
    "type": "FeatureCollection",
    "features": []
    }

    for feature_dict in data:
        new_dict = {
            "type": "Feature", 
            "geometry": {
                "type": "Point",
                "coordinates": [float(feature_dict["longitude"]), float(feature_dict["latitude"])]
            },
            "properties": {
                 "_id": feature_dict["_id"],
                "date": feature_dict["date"],
                "violation_type": feature_dict["violation_type"],
                "description": feature_dict["description"],
                "address": feature_dict["address"],
                "neighborhood": feature_dict["neighborhood"],
                "zip_code": feature_dict["zip_code"],
                "parcel": feature_dict["parcel"],
                "owner": feature_dict["owner"],
                "year_built": feature_dict["year_built"],
                "year_remodeled": feature_dict["year_remodeled"],
                "property_type": feature_dict["property_type"]
  }
        }
        geojson_data["features"].append(new_dict)
    
    export_to_json(geojson_data)



def export_to_json(data):
    try:
        with open("data.geojson", "w+") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Error in the export process!: ", e)

    # try:
    #     with open("data.json", 'w+') as myfile:
    #         json.dump(data, myfile, indent= "")
    # except Exception as e:
    #     print("Error in the export process!: ", e)



