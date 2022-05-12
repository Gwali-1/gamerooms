from flask import Blueprint,render_template,redirect, session, url_for,request,flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user ,logout_user, current_user
from . import db 
from flask_socketio import join_room
from .database_models import Chatrooms_created, Users,Chatrooms_joined
import re




auth = Blueprint("auth",__name__)
password_verification_pattern = "^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$"

CHATROOM_USERS ={}

#defining routes for templates 


#signup
@auth.route("/signup", methods=["POST","GET"])
def signup():
    print(request.method)
    if request.method == "POST":
        print("item")
        name = request.form.get("name").strip()
        user_email = request.form.get("email").strip()
        username = request.form.get("username").strip()
        password_1 = request.form.get("password").strip()
        password_2 = request.form.get("confirmationPassword").strip()
        
        check_username = Users.query.filter_by(username = username).first()
        check_email = Users.query.filter_by(email = user_email).first()
        
        print("name is ",name)


        print()

        if check_username:
            return_message = "Username Taken"
            return render_template("signup.html",Err_message = return_message, user = current_user)

        elif check_email:
            return_message = "Existing Account Associated With This Email"
            return render_template("signup.html",Err_message = return_message, user = current_user)
        elif len(name) < 2 or not name or name.isspace() == True:
            return_message = "Enter Valid name"
            return render_template("signup.html",Err_message = return_message, user = current_user)
        
        elif not username or username.isspace() == True:
            return_message = "Enter Valid Username"
            return render_template("signup.html", Err_message = return_message, user = current_user)

        elif len(username) < 5 :
            return_message = "minimum 8 character username"
            return render_template("signup.html", Err_message = return_message, user = current_user)

        elif len(user_email) < 4 or not user_email or user_email.isspace() == True:
            return_message = "Enter Valid Email"
            return render_template("signup.html",Err_message = return_message, user = current_user)

        elif password_1 != password_2:
            return_message = "Invlid, Passwords Are Not The Same"
            return render_template("signup.html", Err_message = return_message, user = current_user)

        elif len(password_1) < 8 or password_1.isspace() == True:
            return_message = "minimum * character password"
            return render_template("signup.html", Err_message = return_message, user = current_user)

        elif  not re.search(password_verification_pattern , password_1):
            return_message =  "Password Does Not Satisfy Requirements"
            print("[PASSWORD REQUIREMENT ERROR]")
            return render_template("signup.html", Err_message = return_message, user = current_user)

        else:
            new_user = Users(name = name, email = user_email, username = username, password = generate_password_hash(password_1,method = "sha256"))
            db.session.add(new_user)
            try:
                db.session.commit()
                print("[NEW USER ADDED]")
                flash("Created Account",category = "success")
            except Exception as e:
                print(e)
                db.session.rollback()
                flash("Account Couldn't b Created , Try Again Later",category= "error")
                print("[COULD NOT ADD NEW USER]")
                #return signup page again
                return render_template("signup.html", user = current_user)

            #if everything succesfful send user to login page to login
            return redirect(url_for("auth.login"))

    #if get requets
    return render_template("signup.html", user = current_user)







#login
@auth.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username.isspace() == True or password.isspace() == True:
            return_message = "Provide Valid Inputs"
            return render_template("login.html",Err_message = return_message, user = current_user)

        if not username or not password:
            return_message = "Provide Valid Inputs"
            return render_template("login.html",Err_message = return_message, user = current_user)


        user = Users.query.filter_by(username = username).first()
        
        if user:
            print("[USER FOUND]")
            if check_password_hash(user.password,password):
                login_user(user, remember = True)
                flash("Logged In", category="success")
                session["username"] = username
                session["user_id"] = current_user.id
                return redirect(url_for("views.index"))
            else:
                return_message = "Invalid password"
                return render_template("login.html",Err_message = return_message , user = current_user)
        else:
            return_message = "Invalid username"
            return render_template("login.html",Err_message = return_message, user = current_user)



    #if get request
    return render_template("login.html", user = current_user)






#chatconfig
@auth.route("/configchat",methods=["POST","GET"])
def configchat():
   
    if request.method == "POST":
        room = request.form.get("chatroomname")

        if not room or room.isspace() == True:
            return_message = "Provide a Valid Room Name"
            return render_template("chatroom_settings.html",Err_message = return_message, user = current_user)
        
        #checking if chatroom name is already in database
        check = Chatrooms_created.query.filter_by(chatroom = room).first()
        check2 = Chatrooms_joined.query.filter_by(user_id = current_user.id, chatroom = room).first()


        #todo  show user whether chatroom exist or is being created



        #if chatroomname exist we dont add it to database again / to keep chatroom names unique / this help to keep the chats persistent in the rooms
        if not check2:
            new_chatroom_joined = Chatrooms_joined(chatroom = room, user_id = current_user.id)
            db.session.add(new_chatroom_joined)
            try:
                db.session.commit()
                print("CHATROOM JOINED ADDED ")
            except Exception as e:
                db.session.rollback()
                print("COULDNT ADD TO CHATROOM JOINED TABLE ")
                
        if check:
            session["Room"] = room

            if room not in CHATROOM_USERS:   #still checking cause why not
                CHATROOM_USERS[room] = []
            
            if session["username"] not in CHATROOM_USERS[room]:
                CHATROOM_USERS[room].append(session["username"])

            flash("Joined Chatroom!",category="success")

            print(CHATROOM_USERS)
            return redirect(url_for("views.chat"))
        #we enter new chatroom to database and render the chatroom page
        else:
            new_chatroom = Chatrooms_created(chatroom = room , user_id = current_user.id)  #if chatrrom doesnt exist we enter it into database 
            db.session.add(new_chatroom)   
            try:
                db.session.commit()
                print("new chatroom added")
            except Exception:
                db.session.rollback()
                print("error")
                flash("Could Not Create Chatroom!", category= "error")
                return render_template("chatroom_settings.html", user = current_user)

            flash("Created Chatroom!", category= "success")
            session["Room"] = room
            
            CHATROOM_USERS[room] = []
            CHATROOM_USERS[room].append(session["username"])
            return redirect(url_for("views.chat"))

        

    return render_template("chatroom_settings.html",user = current_user )

       
    


#logout
@auth.route("/logout")
@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for("auth.login"))

