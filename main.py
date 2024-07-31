from rentsmart_boston.rentsmart import query_iterator

# Initialize a blank list to hold all entries
blank = []

# Call the query_iterator function to populate the list
all_entries = query_iterator(blank)

# Check the result
if all_entries:
    print("Data retrieval successful.")
else:
    print("No entries retrieved.")