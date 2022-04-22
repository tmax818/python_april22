from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from pprint import pprint

DATABASE = 'paintings'

class Painting:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        # if 'first_name' in data:
        #     self.first_name = data['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # ! CREATE
    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO paintings (title,description,price) VALUES (%(title)s,%(description)s,%(price)s);"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    # ! READ/RETRIEVE ALL
    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM paintings;"
        results = connectToMySQL(DATABASE).query_db(query)
        pprint(results)
        # results will be a list of dictionaries
        paintings = []
        for dictionary in results:
            # dictionary is a dictionary in the list
            paintings.append( cls(dictionary) )
            # adding an instance of the painting class to the paintings list
        return paintings
    
    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM paintings WHERE id = %(id)s";
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    # ! UPDATE
    @classmethod
    def update(cls,data:dict) -> int:
        query = "UPDATE paintings SET title=%(title)s,description=%(description)s,price=%(price)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! DELETE
    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM paintings WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # ! VALIDATIONS
    @staticmethod
    def validate_painting(painting:dict) -> bool:
        is_valid = True # we assume this is true
        if len(painting['title']) < 3:
            flash("Tyler! Remember to change this.")
            is_valid = False
        if len(painting['description']) < 3:
            flash("Tyler! Remember to change this.")
            is_valid = False
        if len(painting['price']) < 2:
            flash("Tyler! Remember to change this.")
            is_valid = False
        return is_valid