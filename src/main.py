#!/usr/bin/env python

import csv
import sqlalchemy
import json

# connect to the database
engine = sqlalchemy.create_engine("postgresql://codetest:password@database:5432/codetest")
connection = engine.connect()

metadata = sqlalchemy.schema.MetaData(engine)

# read the places CSV data file into the table
def load_places_data():
  try:
    with open('/data/places.csv') as csv_file:
      reader = csv.reader(csv_file)
      next(reader)
      for row in reader:
        connection.execute(Places.insert().values(city = row[0], county = row[1], country = row[2] ))
  except Exception as e:
    print("Error", e) 
    
# read the people CSV data file into the table
def load_people_data():
  try:
    with open('/data/people.csv') as csv_file:
      reader = csv.reader(csv_file)
      next(reader)
      for row in reader:
        connection.execute(People.insert().values(given_name = row[0], family_name = row[1], date_of_birth = row[2], place_of_birth = row[3] ))
  except Exception as e:
    print("Error", e)   
      
# output the table to a JSON file
def summary_output (results):
  try:
    with open('/data/summary_output.json', 'w') as json_file:
      rows = connection.execute(results).fetchall()
      data = {}

      for row in rows:
        if row['country'] in data:
          data[row['country']] = data[row['country']] + row['citizen']
        else:
          data[row['country']] = row['citizen']
      json.dump(data, json_file, separators=(',', ':'))

  except Exception as e:
      print("Error", e) 

if __name__ == "__main__":

  # make an ORM object to refer to the tables
  Places = sqlalchemy.schema.Table('places', metadata, autoload=True, autoload_with=engine)
  People = sqlalchemy.schema.Table('people', metadata, autoload=True, autoload_with=engine)

  #load data to the tables
  load_places_data()
  load_people_data()

  #query to retrieve data from the database
  results_query = ("SELECt people.place_of_birth, places.country, COUNT (people.place_of_birth) AS citizen from People JOIN places on people.place_of_birth = places.city GROUP BY people.place_of_birth, places.country ")

  #outputing the results in JSON file 
  summary_output(results_query)