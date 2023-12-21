import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 55555

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# List to store client sockets
client_sockets = []
client_usernames = {}


def broadcast(message, sender_socket):
    for client_socket in client_sockets:
        # Send the message to all clients except the sender
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except:
                # Remove the client if unable to send the message
                remove_client(client_socket)


def remove_client(client_socket):
    if client_socket in client_sockets:
        client_sockets.remove(client_socket)
        username = client_usernames[client_socket]
        print(f"Connection with {username} closed.")
        broadcast(f"{username} has left the chat.", client_socket)
        del client_usernames[client_socket]


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            username = client_usernames[client_socket]
            broadcast(f"{username}: {message}", client_socket)
        except:
            remove_client(client_socket)
            break


def start_server():
    server_socket.listen()

    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Prompt the client for a username
        client_socket.send("Enter your username: ".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8')

        # Add the client to the list
        client_sockets.append(client_socket)
        client_usernames[client_socket] = username

        # Broadcast a welcome message to all clients
        broadcast(f"{username} has joined the chat.", client_socket)

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


if __name__ == "__main__":
    start_server()

