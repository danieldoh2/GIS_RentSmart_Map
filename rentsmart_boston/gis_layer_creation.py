
import arcpy
import json

with open('config.json', 'r') as file:
    d = json.load(file)


print(d['workspace_var'])