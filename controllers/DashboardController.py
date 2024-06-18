from flask import render_template, redirect, url_for, request, abort, session,Response,json
from datetime import date, datetime, timedelta
import mysql.connector,os,ast,sys, random
from dotenv import load_dotenv
from models.Models import *
from models.Schema import *
from sqlalchemy import func, and_




nows = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
status_schema = StatusSchema()
User_schema = UserSchema()
db = SQLAlchemy()
def custom_response(res, status_code):
    return Response(mimetype="application/json",response=json.dumps(res),status=status_code)

def dashboad_index():
    if 'logged_in' in session:
        
        #Today
        todays = datetime.now().date()
        today_sales = Status.query.filter(func.date(Status.created_at) == todays).all()
        data2 = status_schema.dump(today_sales,many=True)
        tods = 0
        for sale in data2:
            tods = tods + (int(sale['requested_amount']) * int(sale['requested_quantity']))
       
        
        
        #weekly
        start_of_week = todays - timedelta(days=todays.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        weekly_sales = Status.query.filter(and_(Status.created_at >= start_of_week, Status.created_at <= end_of_week)).all()
            
        data2 = status_schema.dump(weekly_sales,many=True)
        weekly_earnings = 0
        for sale in data2:
            weekly_earnings = weekly_earnings + (int(sale['requested_amount']) * int(sale['requested_quantity']))
        
        
        #monthly
      
        start_of_month = todays.replace(day=1)
        if todays.month == 12:
            end_of_month = todays.replace(year=todays.year+1, month=1, day=1) - timedelta(days=1)
        else:
            end_of_month = todays.replace(month=todays.month+1, day=1) - timedelta(days=1)
        monthly_sales = Status.query.filter(and_(Status.created_at >= start_of_month, Status.created_at <= end_of_month)).all()
        
        data2 = status_schema.dump(monthly_sales,many=True)
        monthly_earnings = 0
        for sale in data2:
            monthly_earnings = monthly_earnings + (int(sale['requested_amount']) * int(sale['requested_quantity']))
            
        #Totalusers
        

        customer = User.query.all()
        cusa = User_schema.dump(customer,many=True) 
        
        return render_template('dashboard/index.html', today=tods, wek=weekly_earnings,mont=monthly_earnings, test='test',users=cusa)
    else:
        return abort(401)
     
# def dept_count():
#     data = Department.query.count()
#     return custom_response(data, 200)

# def subj_count():
#     data = Subject.query.count()
#     return custom_response(data, 200)

# def course_count():
#     data = Course.query.count()
#     return custom_response(data, 200)
    
# def users_count():
#     data = User.query.count()
#     return custom_response(data, 200)
    
# def student_count():
#     data = User.query.filter_by(access='student').count()
#     return custom_response(data, 200)

# def instructor_count():
#     data = User.query.filter_by(access='instructor').count()
#     return custom_response(data, 200)
    
