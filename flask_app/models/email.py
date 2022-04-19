from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all( cls ):
        query = 'SELECT * FROM emails'
        return connectToMySQL('email_schema').query_db(query)

    @classmethod
    def add(cls,data):
        query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(),NOW())'
        return connectToMySQL('email_schema').query_db(query, data)

    @staticmethod
    def validate_email(email):
        is_valid = True
        if not EMAIL_REGEX.match(email['email']):
            flash("Email is not valid!")
            is_valid = False
        return is_valid
