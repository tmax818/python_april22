# Connecting to a Database

>For every project involving a database, we'll go through the following steps.

1. create a database in sql workbench.
2. create a new flask project with a file to connect to the database:
   - [mysqlconnection.py](mysqlconnection.py)
3. create a model for each database table.
4. update [server.py](server.py) to import our model
5. run the server and visit [localhost:5000](http://localhost:5500/)