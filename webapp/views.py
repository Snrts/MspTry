

from flask import Blueprint, flash, jsonify, render_template, request
from flask_login import login_required, current_user
views = Blueprint('views', __name__)
from . import db 
from .models import Note
import json

@views.route('/')
@login_required
def home():
    return render_template('homepage.html', user=current_user)

@views.route('/selection', methods=['GET','POST'])
@login_required
def selection():
    if request.method == 'POST':
        course1 = request.form.get('course1')
        course2 = request.form.get('course2')
        skill = request.form.get('skill')
        
        if len(course1) < 1:
            flash('note too short', category='error')
        elif len(course2) < 1:
            flash('note too short', category='error')
        elif len(skill) < 1:
            flash('note too short', category='error')
        else:
            select = Note(course1=course1, course2=course2, skill=skill, user_id = current_user.id)
            db.session.add(select)
            db.session.commit()
            flash('Note added', category='succes')

    return render_template('selection.html', user=current_user)

@views.route('/delete-select', methods=['POST'])
def delete_select():
    select = json.loads(request.data)   #loads the id that we passed into the js file
    selectId = select['selectId']       #in js we turned the id into a string, this turns it into an library object
    select = Note.query.get(selectId)   #Looks through the Note database to find entry with that id
    if select: #if exists
        if select.user_id == current_user.id:
            db.session.delete(select)
            db.session.commit()
    return jsonify({})                  #
