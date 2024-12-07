def login(username, password):
    # Sample user data for demonstration purposes
    users = {"user1": "password123", "user2": "mypassword"}
    
    if username in users and users[username] == password:
        return "Login successful!"
    else:
        return "Invalid username or password."
