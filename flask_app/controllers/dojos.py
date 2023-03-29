from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def display_dojos():
    return render_template("index.html")
@classmethod
def save(cls, data):
    query = "INSERT INTO dojos (name) VALUES (%(name)s);"
    result = connectToMySQL('dojo_ninjas').query_db(query, data)
    return result


@app.route('/dojo/<int:dojo_id>')
def view_dojo(dojo_id):
    data = {
        "id": dojo_id
    }
    return render_template('dojo.html', dojo=Dojo.get_one_with_ninjas(data))