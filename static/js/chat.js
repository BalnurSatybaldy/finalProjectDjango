var chat = document.getElementsByClassName("messages")[0];
let for_the_first_time = true;
let startswith = 0;
let endswith = 100;
let no_more_message = false;
let is_loaded = false;
let last_message_pk = 0;

function show_messages(messages, type=null) {
    if (messages.length != 0) {
        last_message_pk = messages[0]["pk"]
    }
    for (var i = 0; i < messages.length; i++) {
        var message = ``
        if (messages[i]["fields"]["user"] == user_pk) {
            message = `
                <div class="my message">
                    <h4>Вы</h4>
                    <p>${messages[i]["fields"]["message"]}</p>
                </div>
            `
        } else {
            message = `
                <div class="ans message">
                    <h4>${messages[i]["fields"]["username"]}</h4>
                    <p>${messages[i]["fields"]["message"]}</p>
                </div>
            `
        }
        if (type == "recent") {
            chat.innerHTML = chat.innerHTML + message
        } else {
            chat.innerHTML = message + chat.innerHTML
        }
    }
}

function get_messages() {
    is_loaded = false;
    if (!(no_more_message)) {
        $.ajax({
            url: `/chat/${chat_pk}/get_messages/?startswith=${startswith}&endswith=${endswith}`,
            success: (response) => {
                show_messages(response["messages"], "previous");
                no_more_message = response["no_more_message"];
                if (!(no_more_message)) {
                    startswith = endswith
                    endswith += 100;
                }
                is_loaded = true;
                if (for_the_first_time) {
                    chat.scrollTop = chat.scrollHeight;
                    for_the_first_time = false;
                }
            },
            error: (error) => {
                console.log(error);
            }
        });
    }
}

chat.onscroll = function() {
  if (!no_more_message && is_loaded && chat.scrollTop <= 0) {
    get_messages();
  }
};

$("form").submit(function(event) {
    var message_input = document.getElementById("message_input");
    message_input.value = message_input.value.trim()
    if (message_input.value == "") {
        event.preventDefault()
        alert("Empty message is not allowed")
    }
})

function get_recent_messages() {
    $.ajax({
        url: `/chat/${chat_pk}/get_recent_messages/?last_message_pk=${last_message_pk}`,
        success: (response) => {
            show_messages(response["recent_messages"], "recent");
            chat.scrollTop = chat.scrollHeight;
        },
        error: (error) => {
            console.log(error);
        }
    });
}

const interval = setInterval(get_recent_messages, 1500);

get_messages()
