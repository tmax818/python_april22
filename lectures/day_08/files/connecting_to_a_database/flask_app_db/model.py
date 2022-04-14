# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL

DATABASE = 'models_schema'

class Model:
    def __init__( self , data ):
        self.id = data['id']
        self.attribute1 = data['attribute1']
        self.attribute2 = data['attribute2']
        self.attribute3 = data['attribute3']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM models;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of friends
        models = []
        # Iterate over the db results and create instances of friends with cls.
        for model in results:
            models.append( cls(model) )
        return models
            