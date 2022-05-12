
from sys import flags
from unicodedata import category
from flask import Blueprint,render_template,redirect, request, session, url_for,flash
from flask_login import current_user
from . import db 
from .database_models import Chatroom_messages, Feeds,Chatrooms_joined,Users
from .auth import CHATROOM_USERS



views = Blueprint("views",__name__) #initialize blueprint

members = CHATROOM_USERS
print(F" CHATROOM MEMBERS VARIABLE  ={members} ")

#defining routes for templates 
#feed
@views.route("/",methods = ["POST","GET"])
def index():
    feed_posts = Feeds.query.order_by(Feeds.id.desc()).limit(100).all()
    if current_user.is_authenticated:
        chatrooms = Chatrooms_joined.query.filter_by(user_id = session["user_id"]).order_by(Chatrooms_joined.id.desc()).limit(6).all()
        return render_template("feed.html", user = current_user,feed_posts = feed_posts, chatrooms = chatrooms)
    else:
        return render_template("feed.html", user = current_user,feed_posts = feed_posts)


#chatroom
@views.route("/chatroom", methods = ["POST","GET"])
def chat():
    print(F"CURRENT CHATROOM MEMBERS  ={members} ")
    if not "Room" in session:
        return redirect(url_for("auth.configchat"))
    
    try:
        current_members = members[session["Room"]]
    except KeyError:
        print(f"\nSERVER ERROR MEMBER VARIABLE NULL = {members} \n")
        session.pop("Room")     
        return redirect(url_for("auth.configchat"))

    print("from chat get",members)
    Chat_messages = Chatroom_messages.query.filter_by(chatroom_name = session["Room"]).all()
    print("\nRETRIEVING CHATROOM MESSAGES...\n")
    return render_template("chatroom.html",user = current_user, Chat_messages = Chat_messages,members = current_members)



#leave chatroom route
@views.route("/leave" ,methods = ["POST"])
def leave_chatroom():
    user_id = request.form.get("user") #get userid
    room = request.form.get("room") #get the current room

    print(f"USERID SENT{user_id} , ROOM SENT{room}")

    if user := Users.query.filter_by(id = user_id).first(): #select username based on id and check if exist using the 
                                                            #assignment expression operator
        name = user.username                                
        print(f"USERNAME MATCHED {name}")
        if room == session.get("Room"): #CHECK IF ROOM SENT IS THE ROOM USER IS CURRENTLY IN
            if name in members[room]:                        
                members[room].remove(name)
                print(f"\nREMOVED {name} FROM {room}")      
                print(members[room])
                print("\n")
                session.pop("Room")
                flash(f"Left {room} ",category= "success")                            #empty the room session
                return redirect(url_for("views.index"))  #take user back to feed page
            return redirect(url_for("auth.configchat"))
        else:
            print(f"MALICIOUS BEHAVIOUR {name}")
            return redirect(url_for("views.chat"))             #error hanlling
    else:
        print(f"MALICIOUS BEHAVIOUR {user_id}")
        return redirect(url_for("views.chat"))                  #error handling 


