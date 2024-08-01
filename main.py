from rentsmart_boston.rentsmart import query_iterator
import arcpy
# Initialize a blank list to hold all entries
blank = []

# Call the query_iterator function to populate the list
try:
    all_entries = query_iterator(blank)
except Exception as e:
    print("error:", e)


# Check the result
# if all_entries:
#     print("Data retrieval successful.")
# else:
#     print("No entries retrieved.")

# arcpy.conversion.JSONToFeatures("data.json", r'C:\Users\ddoh\Documents\ArcGIS\Projects\MyProject\MyProject.gdb\rentsmart_fc', "POINT" )