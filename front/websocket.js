const socket = new WebSocket('ws://localhost:8000');


//socket.addEventListener('open', function (event) {
//    socket.send('Connection Established');
//});

socket.addEventListener('message', function (event) {
    console.log("le serveur a dit : " + event.data);
}); 

var i = 1
const contactServer = () => {
    socket.send(i);
    i++;
}

function test() {
    socket.send("ahah");
}