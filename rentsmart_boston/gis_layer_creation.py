import json
import os 

def parse_config():
    try:
        with open('config.json', 'r') as file:
            workplace = json.load(file)
        workplace_val = workplace['workspace_var']
        return workplace_val
    except Exception as e: 
        print("Error with parsing!", e)

    # try:
    #     arcpy.management.CreateFeatureclass(workplace_val, "rentsmart_fc", geometry_type= "POINT")

    # except Exception as e:
    #     print("Error! :", e)