from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import DateTime
db = SQLAlchemy()
#===================================================
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    genre = db.Column(db.String(30))
    cast = db.Column(db.String(100000))
    img = db.Column(db.String(100000))
    amount = db.Column(db.String(1000))
    qty = db.Column(db.String(1000))
    available = db.Column(db.String(1000))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'genre' : self.genre,
            'cast' : self.cast,
            'img' : self.img,
            'amount' : self.amount,
            'qty' : self.qty,
            'available' : self.available,
        }
#===================================================
class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    request_code = db.Column(db.String(500))
    user_id = db.Column(db.String(150))
    book_id_requested = db.Column(db.String(500))
    requested_date = db.Column(db.String(500))
    requested_quantity = db.Column(db.String(500))
    requested_amount = db.Column(db.String(500))
    status = db.Column(db.String(500))
    is_delete = db.Column(db.String(500))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'request_code' : self.request_code,
            'user_id' : self.user_id,
            'book_id_requested' : self.book_id_requested,
            'requested_date' : self.requested_date,
            'requested_quantity' : self.requested_quantity,
            'requested_amount' : self.requested_amount,
            'status' : self.status,
            'is_delete' : self.is_delete,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at,
        }

#=================================================== balik ka lang dito lagi.. ito mga need natin na data.
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    firstname = db.Column(db.String(25))
    middlename = db.Column(db.String(25))
    lastname = db.Column(db.String(25))
    address = db.Column(db.String(300))
    contact_no = db.Column(db.String(25))
    verify = db.Column(db.String(25))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'email' : self.email,
            'firstname' : self.firstname,
            'middlename' : self.middlename,
            'lastname' : self.lastname,
            'address' : self.address,
            'contact_no' : self.contact_no,
            'verify' : self.verify,
            
        }
#===================================================   

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    request_code = db.Column(db.String(20))
    book_id = db.Column(db.String(20))
    user_id = db.Column(db.String(20))
    duration = db.Column(db.String(4))
    collected = db.Column(db.String(15))
    remark = db.Column(db.String(15))
    remark_date = db.Column(db.String(150))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'request_code' : self.request_code,
            'book_id' : self.book_id,
            'user_id' : self.user_id,
            'duration' : self.duration,
            'collected' : self.collected,
            'remark' : self.remark,
            'remark_date' : self.remark_date,
        }

#===================================================
class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    username = db.Column(db.String(25))
    password = db.Column(db.String(300))
    access = db.Column(db.String(50))
    active = db.Column(db.String(1))
    created_at = db.Column(DateTime, default=datetime.now)
    updated_at = db.Column(DateTime, default=datetime.now, onupdate=datetime.now)
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'email' : self.email,
            'username' : self.username,
            'password' : self.password,
            'access' : self.access,
            'active' : self.active,
        }