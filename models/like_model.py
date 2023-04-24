from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Like:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.tvshow_id = data['tvshow_id']

    @classmethod
    def user_liked_tvshow(cls, tvshow_id, user_id):
        query = """SELECT * FROM likes WHERE tvshow_id = %(tvshow_id)s AND user_id = %(user_id)s;"""
        data = {
            'tvshow_id': tvshow_id,
            'user_id': user_id
        }
        results = connectToMySQL(DATABASE).query_db(query, data)
        return True if results else False

    @classmethod
    def add_like(cls, tvshow_id, user_id):
        query = """INSERT INTO likes (tvshow_id, user_id) VALUES (%(tvshow_id)s, %(user_id)s);"""
        data = {
            'tvshow_id': tvshow_id,
            'user_id': user_id
        }
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def remove_like(cls, tvshow_id, user_id):
        query = """DELETE FROM likes WHERE tvshow_id = %(tvshow_id)s AND user_id = %(user_id)s;"""
        data = {
            'tvshow_id': tvshow_id,
            'user_id': user_id
        }
        return connectToMySQL(DATABASE).query_db(query, data)
