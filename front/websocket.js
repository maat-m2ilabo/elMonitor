const socket = new WebSocket('ws://localhost:8000');
const targetFile = "exampleFiles/test.txt"

socket.addEventListener('open', function (event) {
    socket.send(targetFile);
});

socket.addEventListener('message', function (event) {
    var log = document.getElementById("log");
    log.innerHTML = event.data.replace(/\n/g, "<br>");
});