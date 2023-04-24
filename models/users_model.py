from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re 
from flask_app import DATABASE
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


    @classmethod
    def create(cls,data):
        query="""insert into users (first_name, last_name, email, password)
                Values (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"""
        results= connectToMySQL(DATABASE).query_db(query,data)
        print("***************",results)
        return results 
    
    @classmethod
    def get_by_id(cls,data):
        query="""select * from users where id=%(id)s"""
        results=connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if len(results)<1:
            return False
        return cls(results[0])
    
    @classmethod
    def get_by_email(cls,data):
        query="""select * from users where email=%(email)s"""
        results=connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if len(results)<1:
            return False
        return cls(results[0])
    
    
    #=======validations======
    @staticmethod
    def validate(data):
        is_valid=True 
        if len(data['first_name'])<2:
            is_valid=False
            flash('first_name not valid', 'register')
        if len(data['last_name'])<2:
            is_valid=False
            flash('last_name not valid', 'register')
        if len(data['password']) <7:
            is_valid=False
            flash('password not valid', 'register')
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Email is required !!!!!", 'register')
        if User.get_by_email({'email':data['email']}):
            is_valid = False
            flash("Email already taken hopefully by you !!!!!", 'register')
        elif data['password'] != data['confirm_password']:
            is_valid = False
            flash("Passwords must match !!!!! ", 'register')
        return is_valid