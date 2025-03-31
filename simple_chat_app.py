import socket
host = "localhost"
chat_port = 9901
buffer_size=1024
backlog=5
def chat():
    rol=input("İnput (s) for server, input (c) for client\n").lower()

    if rol=="s":
        chat_server()
    elif rol=="c":
        chat_client()

def chat_server():
   
    #create a server socket,bind it to a ip/port , and listen
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,chat_port))
    server.listen(backlog)

    #accept any incoming connection and let them know they are connected
    print("Server is running....")
    client,client_address=server.accept()
    client.send("You are connected to the server....\n If you want to quit write {quit}".encode("utf-8"))

    #send/recieve messages
    while True:
        #Recieve information from the client
        message = client.recv(buffer_size).decode("utf-8")
        #Quit if the client wants to {quit},else display the message
        if message == "{quit}":
            client.send("quit".encode("utf-8"))
            print("\nEnding the chat...goodbye!")
            break
        else:
           
           print(f"\n{message}")
           message=input(" Message: ")
           client.send(message.encode("utf-8"))

    #close the server socket
    server.close()


def chat_client():
    #create a client socket and connect to the server
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,chat_port))

    #send and recieve messages

    while True:
        #recieve information from the server
        message=client.recv(buffer_size).decode("utf-8")

        #quit if the connected server wants to quit , else keep sending messages
        if message == "{quit}":
           client.send("quit".encode("utf-8"))
           print("\nEnding the chat...goodbye:)")
           break
        else:
            print(f"\n{message}")
            message=input("Message:")
            client.send(message.encode("utf-8"))

    #close the client socket
    client.close()



chat()
