from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db_name = "dojos_and_ninjas"
    def __init__(self,db_data) -> None:
        self.id = db_data["id"]
        self.first_name = db_data["first_name"]
        self.last_name = db_data["last_name"]
        self.age = db_data["age"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]
        self.dojo_id = db_data["dojo_id"]
        
        self.ninjas = []

        

    @classmethod
    def addNinja(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(),%(dojo_id)s);"
        return connectToMySQL("dojosandninjas").query_db(query,data)

    @classmethod
    def getAllNinjas(cls,id):
        #query = f"SELECT * FROM ninjas WHERE dojo_id = {id}"
        query = "SELECT * FROM ninjas AS n INNER JOIN dojos AS d WHERE n.dojo_id = %(id)s ORDER BY n.dojo_id LIMIT 1"
        data = {
            "id": id
        }
        results = connectToMySQL("dojosandninjas").query_db(query,data)
        ninjaLists = []
        for n in results:
            ninjaLists.append(cls(n))
        return ninjaLists

    @classmethod
    def getOneNinja(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.dojo_id = %(dojo_id)s;"
        result = connectToMySQL("dojosandninjas").query_db(query,data)
        return cls(result[0])

        

        