
# GAME ROOMS

#### Video Demo:

#### Description

for as long i could remember trying to find people to find people i could play online games with or simply just join in a discussion about a particular game or game related topic was always messy. i would move from one social media app to another posting and hoping someone will also want to play .
in situations where my fiends were available that was ok but when they were not and you simply wanted to find someone to jump on a game with was pretty faustrating . most apps i tried to find people on where not driven on that purpose and that is why i had this idea to make my project about a web app where gamers can connect on , hang out , have discussions and ultimately find people to gamw with

I call this project the "Game Rooms" and this decision came after numerous considerations against many other names i felt was very cool at the time .
but alas this is the name thta won. i will descripe this as a web application that provides users the ability to connect with other people , either strangers or even people 
they already are associated with. Game rooms allows people to connect and talk about topic that iterest them , such as video games which was mt origional inspiration when making this
application. i imagained a web app that would provide people with the option of joining a dicussion on video games that interested them and ultimately find 
someone to play with . the application is sort of a mini social media app which will serve minimum but a  precise  purpose . send messages on a general timeline feed where everybody can see and create or join chatrooms for discussions.

want to find someone to play games with? start a chatroom and post the name on the timeline to invite interested people , similarly you could join one that has been started by others have created.

this is a platform that allows people to connect over iterested topics primarily games

"name" could also serve thise who choose to just read messages from the timeline feed and share thier views . you would realize that without signing in or signing up , the feed timeline remains visible  to everyone. you can see in real time all messages that are sent by users to the timeline

you can however only be able to send messages to the timeline if you have an account and after signing in


users have the ability to post on the timeline and join chatrooms only when signed in. otherwise you only can read messages from the timeline feed without being able to post or share your views too 

is  a ganers connection app that allows people to chat with each other in rooms based on the topics(which is usually games). the app allows users to create chatrooms where other users can join and then have fun interactions with  other people in the room with them.messages sent in achatroom can only be viewed when youre in the chatroom or join the chatrrom.chatroom interactions are chtroom specific,users have to be in it to take part or view.but there is the timeline feed which every user with an account or  logged in can both view messages and send post .they dony have to join a chatroom for that.the time line page is a general purpose page for all users . also gives users the feature of a timeline feed where everbody can post messages and can be seen about every user. these messages could be announcement of chatrroms users have started themselves or just what users are thinking. the timeline feed can be thought of as the biggest chatroom whose topic is not specified or general . evryone can talk bout whatever they want to and will be seen by everybosy else on the feed page  



"name"  is a simple connection app for friends, gamers and whoever finds its purpose desiring . it brings together poeple from all around the world.
 



 //about structure and files 

 this project required a lot of effort , among them was the planning of how to structure or find a software design that will makw the development process 
 easy . As i knew it was going to take a while and it was probably best if i did not know where to find errors to correct or navigate the code nd make changes . i dreaded the idea of implementing the whole project or most of it (that is the python code part) in one file so i really out in a lot of time researching online. i chanced upon certain github repositories which had some good structuring so i adopted some.


 my project follows to a degree the app structure , i have the temolates and static directories which contain my templates , javasrcipt files and css files 


 inside my project directory is a webapp directory, this contains a static directory, a templates directory and several python files which include auth.py,views.py,database_models, socketevents.py and the dunder __init__.py

 the init.py contain all the various instantiating and required  flask connfigurations . in the file is where i initiate my flask app.
 this is where the configuration for the flask app such as session type , database and secrete key configuration is done .

 inside the init.py i also register blueprints i made for the app which are basically different tyes of views associated with routes. this was as a result of my attempt to keep parts of my project in seperate files 

 i use login manager which is a module in the flask_login library in my application to manage user sessions . inside the init.py i instatiate the login manager object and initiate it with my flaks app. i also configure the view for it which is the default view users see when the login requirements are not satisfied or in other words , when users are not logged in 


i create my sqlalchemy object in my init.py and initiate it with my python app

the ini.py in the webapp makes it possibme for me to do imports of objects and variables inside the webapp directory even outside the diretory because the dunder init.py turns the directory into a python package and this was suitable for me cause at the end i could import my application and run it in another fike from the outside


\
for this project, i required to use websocket technology.after a lot of google searches and research i learnt that it would be perfect for what i wanted to do. i came accross several implentations by people using python sockets. most of these were chat apps applications where two parties could exchange inforemation.
this was perfect 


sockets establishes a path through which a computer can communictate with another

"SocketIO is a cross-browser Javascript library that abstracts the client application from the actual transport protocol."
according to sites and documentation when using socketIo , browsers that support  websockets which is almost all these days can connect to the applocation



flask has an extension called  ‘flask-socketio’ which was perfect for my project ..it gives flask applications access to bi-directional communications between the clients and the server. The client-side application can use any of the SocketIO official client libraries in Javascript, C++, Java and Swift, or any compatible client to establish a permanent connection to the server. and for this project i used the javasrcipt client librabry which is the socket.js
\


 for my database , i used flask_sqlalchemy which is an object relationalmapping tool. it made it possible for me to represent the relational database tables in my database as objects .
 inside the database_models.py i define several classes which represent my databae tables. 