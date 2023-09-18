import socket
import os

host = "localhost"  # Replace with the server's IP or hostname
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Decide whether to send a message or a file
choice = input("Enter 'M' to send a message or 'F' to send a file: ").strip().upper()

if choice == 'M':
    # Send a message
    message = input("Enter your message: ")
    client_socket.send(b'M')  # Indicate that a message is being sent
    client_socket.send(message.encode())
    print("Message sent successfully.")
elif choice == 'F':
    # Send a file
    file_path = input("Enter the path to the file to send: ").strip()
    if not os.path.exists(file_path):
        print("File not found.")
    else:
        file_name = os.path.basename(file_path)
        with open(file_path, 'rb') as file:
            file_data = file.read()
        # Send the file name followed by a marker
        client_socket.send(b'F')  # Indicate that a file is being sent
        client_socket.send(file_name.encode())  # Send the file name with extension
        #client_socket.send(b'FILE_MARKER')  # Send a marker to separate file name and contents
        client_socket.sendall(file_data)  # Send the file contents
        
        print(f"File '{file_name}' sent successfully.")
else:
    print("Invalid choice. Please enter 'M' or 'F'.")

# Close the client socket
client_socket.close()
