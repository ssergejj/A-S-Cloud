import socket
import os

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)


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

client_socket.close()
