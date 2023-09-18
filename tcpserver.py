import socket
import os

# Define the server's host and port
host = "localhost"  # Listen on all available network interfaces
port = 12345

# Create a directory to store received files
save_directory = "received_files"
os.makedirs(save_directory, exist_ok=True)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections (max 5 clients in the queue)
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive the data type indicator ('M' for message, 'F' for file)
    data_type = client_socket.recv(1).decode()

    if data_type == 'M':
        # Receive and handle a message
        message = client_socket.recv(1024).decode()
        print(f"Received message: {message}")
        print("Data type: Message")
    elif data_type == 'F':
        # Receive the file name
        file_name = client_socket.recv(1024).decode()

        # Specify the complete path where the file will be saved
        file_path = os.path.join(save_directory, file_name)

        # Receive and handle the file data
        with open(file_path, 'wb') as file:
            file_data = client_socket.recv(1024)
            while file_data:
                file.write(file_data)
                file_data = client_socket.recv(1024)

        print(f"File '{file_name}' received and saved successfully.")
        print("Data type: File")
    else:
        print("Invalid data type received.")

    # Close the client socket
    client_socket.close()
