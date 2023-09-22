import socket

# Define the server's host and port
host = "10.51.0.94"  # Listen on all available network interfaces
port = 12345

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

   
    file_data = b''
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        file_data += data

    with open('received_file.txt', 'wb') as file:
        file.write(file_data)

        print("File received and saved successfully.")
        print("Data type: File")
    # Close the client socket
    client_socket.close()