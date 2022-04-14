from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

DATABASE = 'dojos_and_ninjas'

class Ninja:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO ninjas (name) VALUES (%(name)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # results will be a list of dictionaries
        ninjas = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            ninjas.append( cls(dictionary) )
            # adding an instance of the ninja class to the ninjas list
        return ninjas
    
    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM ninjas WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    # ! UPDATE
    @classmethod
    def update(cls,data:dict) -> int:
        query = "UPDATE ninjas SET column1=%(column1)s,column2=%(column2)s,column3=%(column3)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! DELETE
    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)