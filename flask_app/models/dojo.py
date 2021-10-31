from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    # class variables to hold table name and connectToMySql
    # allows to press c then tab for cls, and then c and tab for the variable for connectToMySql to prevent repetitive typing
    cTMySql = connectToMySQL("dojos_and_ninjas")
    def __init__(self,db_data) -> None:
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

        # list for a container to hold ninjas
        self.ninjas = []

    def dojo_name(self):
        return "{{self.name}}"

    @classmethod
    def add_dojo(cls,data):
        query ="INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s,NOW(),NOW());"
        return cls.cTMySql.query_db(query,data)

    @classmethod
    def getAllDojos(cls,data):
        query = "SELECT * FROM dojos;"
        results = cls.cTMySql.query_db(query,data)
        dojos = []
        for dojo in results:
            dojos.append(dojo)
        return dojos

    @classmethod
    def getOneDojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = cls.cTMySql.query_db(query,data)
        return cls[result[0]]
    
    @classmethod 
    def updateDojo(cls,data):
        query = "UPDATE dojos SET name = %(name)s, updated_at = NOW() WHERE id = %(id)s;"