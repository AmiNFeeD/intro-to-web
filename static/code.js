(function (){

    const app    = document.querySelector(".app");
    const socket = io();

    let uname;
    document.getElementById("clear-history").addEventListener("click", () => {
        fetch("/clear", { method: "POST" })
            .then(() => location.reload());
    });
    app.querySelector(".join-screen #username")
        .addEventListener("keyup", e => {
            if (e.key === "Enter") app.querySelector(".join-screen #join-user").click();
         });
    app.querySelector(".chat-screen #message-input")
        .addEventListener("keyup", e => {
            if (e.key === "Enter") app.querySelector(".chat-screen #send-message").click();
        });
    app.querySelector(".join-screen #join-user").addEventListener("click", async function (){
        let username = app.querySelector(".join-screen #username").value;
        if(username.length == 0){
            return;
        }

        const response = await fetch("/history")
        const history = await response.json()

        history.forEach(message => renderMessage((message.username === uname) ? "my" : "other", message))

        socket.emit("newuser",username);

        uname = username;

        app.querySelector(".join-screen").classList.remove("active");
        app.querySelector(".chat-screen").classList.add("active");
    });

    app.querySelector(".chat-screen #send-message").addEventListener("click", function (){
        let message = app.querySelector(".chat-screen #message-input").value;
        if(message.length == 0){
            return;
        }
        socket.emit("chat",{
            username:uname,
            text:message
        });
        app.querySelector(".chat-screen #message-input").value = "";
    });

    app.querySelector(".chat-screen #exit-chat").addEventListener("click", function (){
       socket.emit("exituser",uname);
       window.location.href = window.location.href;
    });

    socket.on("update", function (update){
       renderMessage("update", update);
    });

    socket.on("chat",function (message){
       renderMessage("other", message);
    });

    socket.on("history", function (msgs) {
    msgs.forEach(m => {
        const type = (m.username === uname) ? "my" : "other";
        renderMessage(type, m);
    });
});


    function renderMessage(type, message){
        let messageContainer = app.querySelector(".chat-screen .messages");
        if (type == "my"){
            let el = document.createElement("div");
            el.setAttribute("class", "message my-message");
            el.innerHTML = `
                <div>
                    <div class="name">You</div>
                    <div class="text">${message.text}</div>
                </div>
            `;
            messageContainer.appendChild(el);
        } else if(type == "other"){
            let el = document.createElement("div");
            el.setAttribute("class", "message other-message");
            el.innerHTML = `
                <div>
                    <div class="name">${message.username}</div>
                    <div class="text">${message.text}</div>
                </div>
            `;
            messageContainer.appendChild(el);
        } else if(type == "update"){
            let el = document.createElement("div");
            el.setAttribute("class", "update");
            el.innerText = message === `${uname} joined` ? "You joined" : message;
            messageContainer.appendChild(el);
        }
        //scroll chat
        messageContainer.scrollTop = messageContainer.scrollHeight - messageContainer.clientHeight;
    }

})();