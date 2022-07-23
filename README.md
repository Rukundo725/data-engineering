# Code test for data engineering candidates

## Purpose

There are two stages to this code test:

1. Preparing code at home ahead of your interview
2. Pairing with us at the interview, making additions to your code

The pairing phase is to give us an indication of what it will be like to work together, and should be regarded as a collaborative effort.

## Prerequisites

- Knowledge of relational databases, create tables, insert data, and query data.
- Knowledge of a Python programming language
- Some familiarity with Docker for container management
- Familiarity with Git for source control

We have included sample data and python code. The example schema creates a simple table with python code to load data from a CSV file and output to a JSON file. 
There are instructions towards the bottom of this document explaining how to use the Docker containers, start the database, and use the example.

## Background

We have provided a Github repo containing:

- A **docker-compose.yml** file that configures a container for the Postgres database, and the example app containers.
- An **example_schema.sql** file containing a table schema used by the python script.
- A **data** folder containing four files:
  - **example.csv** A tiny dataset, used by the example scripts.
  - **places.csv** 113 rows, where each row has a city, county, and country name.
  - **people.csv** 10,000 rows, where each row has a first name, last name, date of birth, and city of birth.
  - **sample_output.json** Sample output file, to show what your output should look like.

## Problem

There are a sequence of steps that we would like you to complete. We hope this won't take more than a couple of hours of your time.

1. Fork this git repo to your own Github account.
2. Devise a database schema to hold the data in the people and places CSV files, and apply it to the Postgres database. You may apply this schema via a script, via the Postgres command-line client, or via a GUI client.
3. Create a Docker image for loading the CSV files, places.csv and people.csv, into the tables you have created in the database. Make sure the appropriate config is in the docker compose file. Your data ingest process can be implemented in any way that you like, as long as it runs within a Docker container. You may implement this via programme code in a language of your choice, or via the use of ETL tools.
4. Create a Docker image for outputting a summary of content in the database. You may implement this using a programming language of your choice. The output must be in JSON format, and be written to a file in the data folder called **data/summary_output.json**. It should consist of a list of the countries, and a count of how many people were born in that country. We have supplied a sample output **data/sample_output.json** to compare your file against.
5. Share a link to your cloned Github repo with us so we can review your code ahead of your interview.

We have provided an example schema and code that shows how to handle a simple data ingest and output.

Details of how to run and connect to the database are below, together with how to use the example schema and code.

### Notes on completing these tasks

- There is no right way to do this. We are interested in the choices that you make, how you justify them, and your development process.
- Consider how normalized your schema should be, and whether you should be using foreign keys to join tables.
- When you create a container, make sure that you add the container config to the docker-compose.yml file, and add your Dockerfile and code to the src folder.
- Consider what kind of error handling and testing is appropriate.
- All data input, storage, and output should be in UTF-8. Expect multi-byte characters in the data.
- The Postgres database storage is ephemeral; it will not persist, so make sure all schema and data queries are repeatable.
- You may find it easier to work with a subset of the data when developing your ingest.

## Pairing activity at your interview

We will spend 60 minutes during the interview pairing with you. This will include:

- Looking at your current code and solution.
- Modifying your output code, to add several new output files containing different subsets of the data. Be prepared to make different queries of the database, to manipulate data in your programme code, and to output data to disk as JSON and CSV files.

## Notes on using the images in the git repo

### Requirements

Make sure you have recent versions of Docker and Docker Compose.

### Building the images

This will build all the images referenced in the Docker Compose file. You will need to re-run this after making code changes.

```
docker-compose build
```

### Starting Postgres

To start up the Postgres database. This will take a short while to run the database’s start-up scripts.

```
docker-compose up database
```

### Example scripts

We have provided example code written Python. It shows how to use the code in a separate Docker container to connect to the database, using an ORM library where appropriate, to load data from a CSV file, and to query data to output as a JSON file.
It should be regarded as illustrative; it is fine to use any of these examples as the basis of your own solution, but we would prefer that you use technologies that you feel comfortable with.

Then make sure that the containers have been built with `docker-compose build` and start the app with:

```
docker-compose up app
```

In each case, the programme loads data from the data/example.csv file into that table, and exports data from the database table to a JSON file in the data folder. Note that the scripts do not truncate the table, so each one you run will add additional content.

### Cleaning up

To tidy up, bringing down all the containers and deleting them.

```
docker-compose down -v --remove-orphans
```
