
var socket;
$(document).ready(function(){
    socket = io.connect('http://' + document.domain + ':' + location.port + '/chatroom');
    socket.on('connect', function() {
        socket.emit('join', {});
    });

    //when user joins
    socket.on('joined_status', function(data) {
        let user = $("<p class = 'text-muted ' ></p>").text("@" + data.username)
        let users = document.getElementById('Chatroom_users');
        if(users.textContent.includes(data.username)){

          console.log("##");
          
        }else{
          $("#Chatroom_users").prepend(user);
        }
        
    
    });
      //when user leaves
    socket.on('left_status', function(data) {
      let users = document.getElementById('Chatroom_users');
      if(users.textContent.includes(data.username)){

      user.textContent(data.username).replace(data.username, "");
      console.log("hell");
      }
      
  
  });


      //messages from chatroom
    socket.on('chat_text', function(data) {
        let avarta = $("<i class='bi bi-person-circle '></i>")
        let user = $("<h2 class= 'fs-6 fw-bold text-success  lead '></h2>").append(avarta)
        user.append(data.username)
        let mssg = $("<p class = 'chat_text ps-3'></p>").text(data.chat_message)
        let time = $("<p class = 'chat_time ps-3  text-muted'></p>").text(data.chat_time)

        let messg_box = $("<div class ='chat_text_box  ms-2 '></div>")
        messg_box.append(user)
        messg_box.append(mssg)
        messg_box.append(time)

        $('#chatbox').append(messg_box) ;

        $('#chatbox').scrollTop($('#chatbox')[0].scrollHeight);
    });


        //button to send message from chatroom
    $('#send').click(function(e) {
        let text = $('#chatmessage').val();
        let user = $('#chatmessage').attr("name");
      
      
        $('#chatmessage').val('');
        console.log(user)
        socket.emit('message_text', {chat_msg : text, username:user});
    });
});

//function for when leave button
function leave_room() {
    socket.emit('left', {}, function() {
        socket.disconnect();
        // go back to the login page
      
    });
}

