
import arcpy
import json

with open('config.json', 'r') as file:
    workplace = json.load(file)


workplace_val = workplace['workspace_var']

try:
    arcpy.management.CreateFeatureclass(workplace_val, "rentsmart_fc", geometry_type= "POINT")

except Exception as e:
    print("Error! :", e)