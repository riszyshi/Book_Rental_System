from flask import render_template, redirect, url_for, request, abort, session,Response,json
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *
book_schema = BookSchema()

nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# load_dotenv()
# cnx = mysql.connector.connect(host = os.getenv("APP_URL"),user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database= os.getenv("DB_DATABASE"))
# cursor = cnx.cursor()
# book_schema = BookSchema()
# course_schema = CourseSchema()
db = SQLAlchemy()

def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)



def rents_index():
    if 'logged_in' in session:
        books = Book.query.all()
        data2 = book_schema.dump(books,many=True) 
        return render_template('front_view/index.html', data = data2)
    else:
        return abort(401)

def rents_store():
    ...

def rents_show():
    ...

def rents_update():
    ...

def rents_destroy():
    ...