import json

def is_valid_user(username, password):
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    for entry in data:
        if entry["username"] == username and entry["password"] == password:
            return True
    
    return False

input_username = input("Enter your username: ")
input_password = input("Enter your password: ")

if is_valid_user(input_username, input_password):
    print("Login successful!")
else:
    print("Login failed. Invalid username or password.")