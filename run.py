import http.client
import json

# List advanced example
host = "paexternalj.github.io"
path = "/facebook/"

#Lists example mock data
credentials = [
    {"username": "hfjskdf", "password": "123456"},
    {"username": "testuser1", "password": "password123"},
    {"username": "exampleuser", "password": "examplepass"},
    {"username": "admin", "password": "admin123"},
    {"username": "user2024", "password": "secure2024"},
    {"username": "johndoe", "password": "doe12345"},
    {"username": "janedoe", "password": "password456"},
    {"username": "guestuser", "password": "guestpass"},
    {"username": "developer", "password": "devcode"},
    {"username": "manager", "password": "manager1"},
    {"username": "tester", "password": "testme123"},
    {"username": "rootadmin", "password": "rootpass"},
    {"username": "coderlife", "password": "code123"},
    {"username": "backenddev", "password": "backend456"},
    {"username": "frontenddev", "password": "frontend789"},
    {"username": "supportuser", "password": "support123"},
    {"username": "guest2024", "password": "welcome2024"},
    {"username": "tempuser", "password": "temporary1"},
    {"username": "newuser", "password": "newpassword"},
    {"username": "adminuser", "password": "secureadmin"}
]

# Function to attempt login
def attempt_login(username, password):
    try:
        # Establish connection
        conn = http.client.HTTPSConnection(host)
        conn.request("GET", path)
        response = conn.getresponse()
        
        # Check the response status
        if response.status == 200:
            print(f"Trying username: {username} | password: {password}")

            # Simulated success condition
            if username == "hfjskdf" and password == "123456":
                print(f"Success! Logged in with username: {username} and password: {password}")
                conn.close()
                return True
            else:
                print("Failed login attempt.")
                conn.close()
                return False
        else:
            print(f"Error: Unable to reach the website. Status code: {response.status}")
            conn.close()
            return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

# Iterate over credentials and test each pair
for cred in credentials:
    username = cred["username"]
    password = cred["password"]
    if attempt_login(username, password):
        break
