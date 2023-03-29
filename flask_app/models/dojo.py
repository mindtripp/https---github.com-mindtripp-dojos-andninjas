from flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import connectToMySQL



class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

   

class Dojo:
    

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        dojos = []

        try:
            cnx = mysql.connector.connect(user='root', password='rootroot', host='127.0.0.1', database='dojo_ninjas')
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            results = cursor.fetchall()

            for d in results:
                dojos.append(cls(d))

        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")
            
        finally:
            if cnx is not None and cnx.is_connected():
                cursor.close()
                cnx.close()

        return dojos


    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result

    @classmethod
    def find_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])

        for row in results:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo
