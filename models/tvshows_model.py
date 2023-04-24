from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import users_model
from flask_app import DATABASE

class Tvshow:
    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.title=data['title']
        self.network=data['network']
        self.description=data['description']
        self.Release_date= data['Release_date']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        user=users_model.User.get_by_id({'id':self.user_id})
        self.owner = f"{user.first_name} {user.last_name}"
        
        
        
    @classmethod
    def create_tvshow(cls,data):
        query="""insert into tvshows  (user_id, title, network, description, Release_date)
                 Values (%(user_id)s,%(title)s, %(network)s, %(description)s, %(Release_date)s);"""
        results=connectToMySQL(DATABASE).query_db(query,data)
        return results
    
    @classmethod
    def get_by_id(cls,data):
        query="""select * from tvshows where id=%(id)s"""
        results=connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if len(results)<1:
            return False
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query="""Update tvshows set title=%(title)s, network=%(network)s, description=%(description)s, Release_date=%(Release_date)s
        where id =%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def delete(cls,data):
        query="""delete from tvshows where id=%(id)s; """
        results=connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        return results
    @classmethod
    def get_all(cls):
        query="""select * from tvshows """
        results=connectToMySQL(DATABASE).query_db(query)
        print(results)
        tvshows=[]
        for row in results:
            tvshows.append(cls(row))
        return tvshows
    
    #=======validations======
    @staticmethod
    def validate(data):
        is_valid=True 
        if len(data['title'])<3:
            is_valid=False
            flash('title must be at least 3 characters')
        if len(data['network'])<3:
            is_valid=False
            flash('network must be at least 3 characters')
        if len(data['description']) <3:
            is_valid=False
            flash('description must be at least 3 characters')
        if data['description']== "":
            is_valid=False
            flash('description  must not be blank')
        if data['Release_date'] =="":
            is_valid=False
            flash('release_date must not be blank')
       
        return is_valid
    