from flask import render_template, redirect, url_for, request, abort, session,Response,json
from flask_sqlalchemy import SQLAlchemy
from models.Models import *
from models.Schema import *
import sys

db = SQLAlchemy()
def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)



def history_index():
    if 'logged_in' in session:
        return render_template('history/index.html')
    else:
        return abort(401)

def history_store():
    ...

def history_show():
    ...

def history_update():
    ...

def history_destroy():
    ...