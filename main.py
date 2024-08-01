from rentsmart_boston.rentsmart import query_iterator
from rentsmart_boston.gis_layer_creation import parse_config

import arcpy
# Initialize a blank list to hold all entries
blank = []

# Call the query_iterator function to populate the list
try:
    all_entries = query_iterator(blank)
    print("Success!")
except Exception as e:
    print("error:", e)



gdb_path = parse_config()
print(gdb_path)
arcpy.conversion.JSONToFeatures("data.geojson", gdb_path, "POINT" )
print("Success!")
