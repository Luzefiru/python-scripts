import pandas as pd

target = "raw_data.csv" # change me to the data you want to sort

# builds the key:value pairs into their own list's indices
fh = open(target, "r"); 


keywords = []
descriptions = []

x = True
for i in fh:
    if x:
        keywords.append(i[0:-1])
    else:
        descriptions.append(i[0:-1])
    x = not x

fh.close()

# creates a list containing sorted keyword:description pairs
dictionary = dict(zip(keywords, descriptions))
sortedPairs = sorted(dictionary.items())

# writes the keyword:description pairs to a new .csv
fh = open("sorted_data.csv", "w")

for k,v in sortedPairs:
    fh.write(f"{k},{v}\n")

fh.close()
