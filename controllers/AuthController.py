from flask import render_template, redirect, url_for, request, abort, session,Response,json,Flask,flash
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *


db = SQLAlchemy()
load_dotenv()



def login():
    if 'logged_in' in session:
        return redirect(url_for('dashboards.dashboad_index'))
    else:
        if request.method == 'POST':
            usernamePost = request.form.get('username')
            passwordPost = request.form.get('password')
            user = Admin.query.filter_by(username=usernamePost).first()
            if user:
                if check_password_hash(user.password, passwordPost):
                    session['logged_in'] = True
                    session['name'] = user.email


                    return redirect(url_for('dashboards.dashboad_index'))
            
                else:
                    print('Incorrect Password')
            else:
                print('Username not available, Contact the Administrator')
              
    return render_template('auth/login.html')

def logout():
    session.clear()
    return redirect(url_for('auth.login'))

















