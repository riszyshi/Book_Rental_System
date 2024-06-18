from flask import render_template, redirect, url_for, request, abort, session,Response,json
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *


nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
load_dotenv()
cnx = mysql.connector.connect(host = os.getenv("APP_URL"),user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database= os.getenv("DB_DATABASE"))
cursor = cnx.cursor()
User_schema = UserSchema()
db = SQLAlchemy()


def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)



def user_index():
    if 'logged_in' in session:
        customers = User.query.all()
        data2 = User_schema.dump(customers,many=True) 
        return render_template('users/index.html',data=data2)
    else:
        return abort(401)
    

def user_store():
    data = request.get_json()
    cursor.execute("INSERT INTO `users`(`email`, `firstname`, `middlename`, `lastname`, `address`, `contact_no`, `verify`, `created_at`, `updated_at`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",([data['emails'],data['firstname'],data['middlename'],data['lastname'],data['address'],data['contact_no'],'1',nows, nows]))
    cnx.commit() 
    return '1'

def user_show():
    ...

def user_update():
    data = request.get_json()
    cursor.execute("UPDATE `users` SET `email`=%s,`firstname`=%s,`middlename`=%s,`lastname`=%s,`address`=%s,`contact_no`=%s,`updated_at`=%s WHERE `id` = %s",([data['emails'],data['firstname'],data['middlename'],data['lastname'],data['address'],data['contact_no'],nows,data['id']]))
    cnx.commit()
    return '1'

def user_destroy():
    data = request.get_json()
    cursor.execute("DELETE FROM `users` WHERE `id`=%s ",([data['id']]))
    cnx.commit()
    return  "1"