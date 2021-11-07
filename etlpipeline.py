# Akhil Havaldar; ash2sfp

# Importing libraries
import json
import pandas as pd
import boto3

# Benchmark 1: Reading in the original data source from CSV
filename = r'C:\Users\a8hav\Desktop\cs1110\recipeData.csv'
beer_data = pd.read_csv(filename, encoding='latin-1')       # using the pandas library to read in the csv
print(beer_data)

# Benchmark 2: Modifying the columns
beer_data = beer_data.dropna(axis='columns')         # Drops all the columns that have NA's
print(beer_data)

# Benchmark 3: Converting the pandas df to a json file
result = beer_data.to_json(orient="split")      # Converting to json
parsed = json.loads(result)                     # Parsing the result
json_new = json.dumps(parsed, indent=4)             # Loading into a json file

with open('pipeline.json', 'w') as json_file:       # writes the json text to a json file locally
    json.dump(json_new, json_file)


# Extra: Benchmark 4: Pushing the resulting json file to an S3 bucket
# This is the code I would use to try and push my json file to an s3 bucket.
# I don't have access to create a key so I could not get this code to run.

# s3 = boto3.client('s3')
# json_object = json_new
# s3.put_object(
#      Body=json.dumps(json_object),
#      Bucket='ash2sfp-pipeline',
#      Key='**********'
# )
