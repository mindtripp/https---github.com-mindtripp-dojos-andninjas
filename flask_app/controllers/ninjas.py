from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def display_ninjas():
    return render_template('ninja.html')

@app.route('/create/ninja', methods=['POST'])
def add_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')
