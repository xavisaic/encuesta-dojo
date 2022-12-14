from mysqlconnection import connectToMySQL
from flask import flash

class Form:
    def __init__(self,data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.location = data['location']
        self.fav_language = data['fav_language']
        self.comentario = data['comentario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO esquema_encuesta_dojo.dojos (first_name,location,fav_language,comentario,created_at,updated_at) VALUES (%(first_name)s,%(location)s,%(fav_language)s,%(comentario)s,NOW(),NOW())"
        return connectToMySQL('esquema_encuesta_dojo').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        form_from_db =  connectToMySQL('esquema_encuesta_dojo').query_db(query)
        forms =[]
        for b in form_from_db:
            forms.append(cls(b))
        return forms

    @staticmethod
    def validate_form(form):
        is_valid = True # asumimos que esto es true
        if len(form['first_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(form['location']) < 3:
            flash("location must be at least 3 characters.")
            is_valid = False
        if len(form['location']) < 3:
            flash("location must be at least 3 characters.")
            is_valid = False
        if len(form['fav_language']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        return is_valid
