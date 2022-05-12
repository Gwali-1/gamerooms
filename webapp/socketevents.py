from email import message
from . import socketio,db
from flask_socketio import join_room, leave_room, emit
from flask import  session,flash
from flask_login import current_user
from .database_models import Users,Feeds,Chatroom_messages
from datetime import datetime






#events 

#when a user joins chat
@socketio.on("join", namespace= "/chatroom")
def join_chat(message):
    room = session.get("Room")
    name = session.get("username")
    join_room(room)
    emit("joined_status",{"username": name }, room = room)



#when a  user send a message in chat
@socketio.on("message_text", namespace= "/chatroom")
def send_message(message):
    message_sent = message["chat_msg"].strip()
    room = session.get("Room")
    time = datetime.now().strftime("%c") 

    #for when a user clicks the send button without a message 
    if not message_sent or message_sent.isspace() == True:
        return None

        #entering chat into db
    if  message_sent:
        chat_message = Chatroom_messages(chat_message = message_sent, username = current_user.username, chatroom_name = room, user_id = current_user.id )
        db.session.add(chat_message)
        try:
            db.session.commit()
            print("[ADDED CHAT MESSAGE]")
        except Exception as e:
            db.session.rollback()
            print("[COULDNT ADD CHAT MESSAGE]")
            print(e)

    emit("chat_text",{"chat_message":f"{message.get('chat_msg')}","username":session.get("username"),"chat_time" : time},room = room)





#when a user post message on the feed
@socketio.on("feed_message",namespace= "/")
def send_feed(message):
    username = session.get("username")
    feed_post = message.get("feed_txt").strip()
    time = datetime.now().strftime("%c")  #time of post
 
    if not feed_post or feed_post.isspace() == True:
        return None
  

    #only addds to database if user sends an atual post nit an empty string
    if feed_post:
        new_post = Feeds(post = feed_post, user_id = current_user.id, username = current_user.username)
        db.session.add(new_post)
        try:
            db.session.commit()
            print(username,"added_post")
        except Exception as e:
            db.session.rollback()
    
    emit("feed_post",{"feed_message":feed_post.strip() ,"username":username, "post_time":time}, broadcast = True)





#when user leaves a chatroom
@socketio.on('leave', namespace='/chatroom')
def left(message):
    room = session.get('room')
    username = session.get('username')
    leave_room(room)
  
    emit('left_status', {'username': username}, room=room)

