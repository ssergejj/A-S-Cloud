import socket
import threading
import os


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "[DISCONNECTED]"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Create a directory to store received files
save_directory = "received_files"
os.makedirs(save_directory, exist_ok=True)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
            file_name = conn.recv(1024).decode()
        

            # Specify the complete path where the file will be saved
            file_path = os.path.join(save_directory, file_name)

            # Receive and handle the file data
            with open(file_path, 'wb') as file:
                file_data = conn.recv(1024)
                while file_data:
                    file.write(file_data)
                    file_data = conn.recv(1024)

            print(f"File '{file_name}' received and saved successfully.")
            print("Data type: File")
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
    
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] Server starting...")
start()