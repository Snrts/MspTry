
import email
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/Login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() #will look through the database and find the first (and should be only) account with that email
        if user:
            if check_password_hash(user.password, password): #takes the password associated in db with that email and checks it against the password filled in in form
                flash('Logged in succesfully', category='succes')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('No account found with this E-mail', category='error')

    return render_template('Loginpage.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        firstname = request.form.get('First Name')
        lastname = request.form.get('Last Name')
        password1 = request.form.get('password1')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('This E-mail address is already in use', category='error')
        elif password1 != password:
            flash('Passwords do not match', category='error')
        elif len(password)<7:
            flash('Password must have more than 7 characters', category='error')
        else:
            new_user = User(email=email, firstname=firstname, lastname=lastname, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category="succes")
            return redirect(url_for('views.home'))
    return render_template('sign_up.html', user=current_user)
   