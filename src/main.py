#!/usr/bin/env python

import csv
import sqlalchemy
import json

# connect to the database
engine = sqlalchemy.create_engine("postgresql://codetest:password@database:5432/codetest")
connection = engine.connect()

metadata = sqlalchemy.schema.MetaData(engine)

# make an ORM object to refer to the tables

Places = sqlalchemy.schema.Table('places', metadata, autoload=True, autoload_with=engine)
People = sqlalchemy.schema.Table('people', metadata, autoload=True, autoload_with=engine)

# read the places CSV data file into the table
with open('/data/places.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader:
    connection.execute(Places.insert().values(city = row[0], county = row[1], country = row[2] ))


# read the people CSV data file into the table
with open('/data/people.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader:
    connection.execute(People.insert().values(given_name = row[0], family_name = row[1], date_of_birth = row[2], place_of_birth = row[3] ))

# output the table to a JSON file

results = ("SELECt people.place_of_birth, places.country, COUNT (people.place_of_birth) AS citizen from People JOIN places on people.place_of_birth = places.city GROUP BY people.place_of_birth, places.country ")

with open('/data/summary_output.json', 'w') as json_file:
  rows = connection.execute(results).fetchall()
  data = {}

  for row in rows:
    if row['country'] in data:
      data[row['country']] = data[row['country']] + row['citizen']
    else:
      data[row['country']] = row['citizen']
  json.dump(data, json_file, separators=(',', ':'))