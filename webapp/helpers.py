from os import path
from functools import wraps
from flask import session, redirect



#initializinng databasee
def create_database(database_name, db_object, app_object):
      if not path.exists(f"webapp/{database_name}"):
        db_object.create_all(app=app_object )
        print("database created")




# can be used to chache result 
def chacher(chache,func,quote):  #chache can be a data structure like a dict , func is a request function and quote the url passed in the func
    print("fetching ...")
    if quote not in chache:
        chache[quote] = func(quote)
    return chache[quote]



def login_required(f):  #this is an implementayion of the login required decorator from the flask login module
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
