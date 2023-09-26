from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.email = data['email']
        self.dob = data['dob']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (name,email,dob,password,created_at,updated_at) VALUES (%(name)s,%(email)s,%(dob)s,%(password)s,NOW(),NOW());"
        return connectToMySQL('revise').query_db(query,data)