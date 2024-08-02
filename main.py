from rentsmart_boston.rentsmart import query_iterator
from rentsmart_boston.gis_layer_creation import parse_config
import arcpy
# Initialize a blank list to hold all entries
blank = []

# Call the query_iterator function to populate the list
try:
    all_entries = query_iterator(blank)
    print("Success with ETL")
except Exception as e:
    print("error:", e)


gdb_path = parse_config()
feature_class_name = "rentsmart_fc"
gdb_path = f"{gdb_path}/{feature_class_name}"
print(gdb_path)

print("Buidling FC Into: ", gdb_path)

arcpy.conversion.JSONToFeatures("data.geojson", gdb_path, "POINT" )
print("Success!")
