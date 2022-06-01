
from flask import Blueprint, flash, render_template, request
from flask_login import login_required, current_user
views = Blueprint('views', __name__)
from . import db 
from .models import Note

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
