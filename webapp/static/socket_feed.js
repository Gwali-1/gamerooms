

var socket;
$(document).ready(function(){
    socket = io.connect('http://' + document.domain + ':' + location.port + '/');
    socket.on('connect', function() {
        socket.emit('join', {});
        console.log("connected");
    });




    socket.on('status_message', function(data) {

        $('#chatbox').val($('#chatbox').val() + '<' + data.status_msg + '>\n');
        $('#chatbox').scrollTop($('#chatbox')[0].scrollHeight);
    });




    socket.on('feed_post', function(data) {
        message_sent = data.feed_message
        if (message_sent){
        let avarta = $("<i class='bi bi-person-circle fs-1 me-2'></i>")
        let user = $("<h2 class= 'fs-6 fw-bold text-success  lead '></h2>").append(avarta)
        user.append(data.username)
        let mssg = $("<p class = 'chat_text ps-3'></p>").text(data.feed_message)
        let time = $("<p class = 'chat_time ps-3  text-muted'></p>").text(data.post_time)

        let messg_box = $("<div class ='chat_text_box  ms-2 '></div>")
        messg_box.append(user)
        messg_box.append(mssg)
        messg_box.append(time)
        $('#feed_content').prepend(messg_box) ;
        }
    });





    $('#send_feed').click(function(e) {
        text = $('#feedmessage').val();
    
        $('#feedmessage').val('');
        console.log(text)
        socket.emit('feed_message', {feed_txt : text});
    });
});


