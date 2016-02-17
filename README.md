# swissgame

#### This project has 3 files:

##### 1. tournament.sql

###### This file is used to set up the database and tables for the tournament.	

##### 2. tournament.py

###### This file is used to provide access to the database with a list of functions that can perform operations on the database as requested by any other python program

##### 3. tournament_test.py

###### This is the client test file which manipulates the database in different ways and checks whether the results are valid. It uses the functions in the tournament.py module. This is a TDD style testing the functionality of the functions in the tournament.py

#### REQUIREMENTS:

###### Python 2.7 (recommended)
###### PostgreSQL (required)

#### To run the code:

##### Load the tournament.sql file into postgreSQL. This will create the schema
Then run the tournament_test.py file, and you will find success printed.