from flask import render_template, redirect, url_for, request, abort, session,Response,json
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys
from dotenv import load_dotenv
from sqlalchemy import func
from models.Models import *
from models.Schema import *


nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
load_dotenv()
cnx = mysql.connector.connect(host = os.getenv("APP_URL"),user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database= os.getenv("DB_DATABASE"))
cursor = cnx.cursor()
book_schema = BookSchema()
# course_schema = CourseSchema()
db = SQLAlchemy()


def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)



def books_index():
    if 'logged_in' in session:
        books = Book.query.all()
        data2 = book_schema.dump(books,many=True) 
        return render_template('books/index.html', data = data2)
    else:
        return abort(401)

def books_store():
    data = request.get_json()

    # Convert both titles to lowercase for case-insensitive comparison
    new_title_lower = data['title'].lower()

    # Check if a book with a similar title (case-insensitive) already exists
    existing_book = Book.query.filter(func.lower(Book.title) == new_title_lower).first()



    
    if existing_book:
        id = existing_book.id
        available = int(existing_book.available) + int(data['available'])
        newqty = int(existing_book.qty) + int(data['available'])
    
        cursor.execute("UPDATE `books` SET `available`=%s,`qty`=%s,`updated_at`=%s WHERE `id` = %s",([available,newqty,nows, id]))
        cnx.commit()
        
    
        return '1'

    cursor.execute(
        "INSERT INTO `books`(`title`, `genre`, `cast`, `img`, `amount`, `available`, `created_at`, `updated_at`, `qty`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        ([data['title'], data['genre'], data['cast'], data['image'], data['amount'], data['available'], nows, nows,
          data['available']]))
    cnx.commit()
    return '1'


def books_show():
    ...

def books_update():
    data = request.get_json()
    cursor.execute("UPDATE `books` SET `title`=%s,`genre`=%s,`cast`=%s,`amount`=%s,`available`=%s,`updated_at`=%s WHERE `id` = %s",([data['title'],data['genre'],data['cast'],data['amount'],data['available'],nows, data['id']]))
    cnx.commit() 
    return '1'

def books_destroy():
    data = request.get_json()
    cursor.execute("DELETE FROM `books` WHERE `id`=%s ",([data['id']]))
    cnx.commit()
    return  "1"

def updete_available():
    data = request.get_json()
    books = Book.query.filter(Book.id == int(data['id']))
    data2 = book_schema.dump(books,many=True) 
    to_update = int(data2[0]['available']) - int(data['vals'])
    
    cursor.execute("UPDATE `books` SET `available`=%s,`updated_at`= %s WHERE `id` = %s",([to_update,nows, int(data['id'])]))
    cnx.commit() 
    return '1'
