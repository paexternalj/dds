import requests

# URL of the login page
url = "https://paexternalj.github.io/facebook/"

# Credentials to test
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
        # Simulate fetching the page content
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Trying username: {username} | password: {password}")
            
            # Simulated success condition
            if username == "hfjskdf" and password == "123456":
                print(f"Success! Logged in with username: {username} and password: {password}")
                return True
            else:
                print("Failed login attempt.")
                return False
        else:
            print(f"Error: Unable to reach the website. Status code: {response.status_code}")
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
