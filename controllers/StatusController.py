from flask import render_template, redirect, url_for, request, abort, session,Response,json
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys, random
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *



nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

load_dotenv()
cnx = mysql.connector.connect(host = os.getenv("APP_URL"),user = os.getenv("DB_USERNAME"), password = os.getenv("DB_PASSWORD"), database= os.getenv("DB_DATABASE"))
cursor = cnx.cursor()

User_schema = UserSchema()
status_schema = StatusSchema()
book_schema = BookSchema()



db = SQLAlchemy()
def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)



def status_index():
    if 'logged_in' in session:
        return render_template('status/index.html')
    else:
        return abort(401)

def status_store():
    lower ="abcdefghijklmnopqrstuvwxyz"
    upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    tanan = lower + upper + numbers
    taas = 16
    request_codes = "".join(random.sample(tanan,taas))
    status = 'Rented'
    data = request.get_json()
    cursor.execute("INSERT INTO `status`(`request_code`, `user_id`, `book_id_requested`, `requested_date`, `requested_quantity`, `requested_amount`, `status`, `is_delete`, `created_at`, `updated_at`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",([request_codes,data['user_id'],data['book_id_requested'],data['requested_date'],data['rent_qty'],data['rent_ams'],status,0,nows,nows]))
    cnx.commit() 
    return '1' 

def status_show():
    customer = User.query.all()
    data2 = User_schema.dump(customer,many=True) 
    return data2

def status_update():
    data = request.get_json()
    now1s = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("UPDATE `status` SET `status`='Return' , `updated_at`=%s WHERE `id` = %s",([now1s, int(data['id'])]))
    cnx.commit()
    
    return '1'

def status_destroy():
    ...

def status_rented():
    if 'logged_in' in session:
        rented = Status.query.filter(Status.is_delete != 1)
        kostomer = User.query.all()
        palabas = Book.query.all()

        data2 = status_schema.dump(rented,many=True)
        data3 = User_schema.dump(kostomer,many=True) 
        data4 = book_schema.dump(palabas,many=True)

        name = {}
        for a in data3:
            name[a['id']] = a['lastname']



        booka = {}
        for b in data4:
            booka[b['id']] = b['title']
           



        return render_template('status/index.html', data=data2, names = name, books=booka)
    else:
        return abort(401)

def updete_iddelete():
    data = request.get_json()

    cursor.execute("UPDATE `status` SET `is_delete`='1' , `updated_at`=%s WHERE `book_id_requested` = %s",([nows, int(data['id'])]))
    cnx.commit()

    return '1'