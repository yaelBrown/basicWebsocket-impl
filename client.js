const socketClient = () => {
    console.log("Trying to connect...")
    
    const socket = io("http://localhost:5000");
    
    socket.on('connect', () => {
        socket.send("I am connected");
    });

    socket.on('message', data => {
        console.log("Message recieved: " + data);
    })
}