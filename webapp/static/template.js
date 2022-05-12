
function displayPasswordRequirements(){
    document.getElementById("Password_info").innerHTML = "<i class='bi bi-info-square-fill'></i> Password must at least 8 charaters ,an uppercase ,a lowercase, a digit and one special character";
}

 

function hideit(){
    document.getElementById("send_message_prompt").style.display = "none";
}


function showit(){
    document.getElementById("send_message_prompt").style.display = "block";
}



window.setTimeout(function(){
    $(".alert").fadeTo(500,0).slideUp(500,function(){
        $("this").remove()
    });
},1000)
