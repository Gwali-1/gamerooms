from datetime import datetime
from email import message
from flask_login import UserMixin
from . import db 


#creating database tables / models

now = datetime.now() # current date and time
date_time = now.strftime("%m/%d/%Y  %H:%M")
print("date and time:",date_time)

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(150),unique = True)
    username = db.Column(db.String(100),unique = True)
    name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    timeobj = db.Column(db.DateTime,default = datetime.now())
    timestr = db.Column(db.String,default = datetime.now().strftime("%c"))
    feeds = db.relationship("Feeds")
    Chatrooms_joined = db.relationship("Chatrooms_joined")
    Chatrooms_created= db.relationship("Chatrooms_created")



class Feeds(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    post = db.Column(db.String)
    username = db.Column(db.String)
    timeobj = db.Column(db.DateTime,default = datetime.now())
    timestr = db.Column(db.String,default = datetime.now().strftime("%c"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Chatrooms_joined(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    chatroom = db.Column(db.String)
    timeobj = db.Column(db.DateTime,default = datetime.now())
    timestr = db.Column(db.String,default = datetime.now().strftime("%c"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


class Chatrooms_created(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    chatroom = db.Column(db.String)
    timeobj = db.Column(db.DateTime,default = datetime.now())
    timestr = db.Column(db.String,default = datetime.now().strftime("%c"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


class Chatroom_messages(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    chat_message = db.Column(db.String)
    username = db.Column(db.String)
    chatroom_name = db.Column(db.String)
    timestr = db.Column(db.String,default = datetime.now().strftime("%c"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


