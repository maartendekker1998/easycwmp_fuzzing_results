import json, re

# Opening JSON file
f = open('crash_chains_transfer_complete_response.json')

# returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json list
x = 0

for i, j in data.items():
    y = json.dumps(j)
    if re.match(".*tree.*", y):
        x =x+1
        print(x)


# Closing file
f.close()