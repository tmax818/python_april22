from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from pprint import pprint

DATABASE = 'dojo_survey'

class Dojo:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO dojos (name,location,language,comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # results will be a list of dictionaries
        dojos = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            dojos.append( cls(dictionary) )
            # adding an instance of the dojo class to the dojos list
        return dojos
    
    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM dojos WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    # ! UPDATE
    @classmethod
    def update(cls,data:dict) -> int:
        query = "UPDATE dojos SET name=%(name)s,language=%(language)s,location=%(location)s,comment=%(comment)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! DELETE
    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! VALIDATIONS
    @staticmethod
    def validate_dojo(dojo:dict) -> bool:
        is_valid = True # we assume this is true
        if len(dojo['name']) < 1:
            flash("Tyler! Remember to change this.")
            is_valid = False
        if not dojo['location']:
            flash("Tyler! Remember to change this.")
            is_valid = False
        if not dojo['language']:
            flash("Tyler! Remember to change this.")
            is_valid = False
        return is_valid