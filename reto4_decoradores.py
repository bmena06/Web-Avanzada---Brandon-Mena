class AuthenticationError(Exception):
    pass

user_database = {
    "user": {"password": "user123", "role": "user"},
    "admin": {"password": "admin123", "role": "admin"},
    "superadmin": {"password": "superadmin123", "role": "superuser"}
}

def authenticate(username, password, required_role):
    if username in user_database and user_database[username]["password"] == password:
        user_role = user_database[username]["role"]
        if user_role == required_role:
            return True
    return False

def auth_required(required_role):
    def decorator(func):
        def wrapper():
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate(username, password, required_role):
                return func(username, password)
            else:
                print("AuthenticationError: Insufficient privileges")
        return wrapper
    return decorator

@auth_required("user")
def user_function(username, password):
    print(f"User function accessed by {username}")

@auth_required("admin")
def admin_function(username, password):
    print(f"Admin function accessed by {username}")

@auth_required("superuser")
def superuser_function(username, password):
    print(f"Superuser function accessed by {username}")

if __name__ == "__main__":
    user_function()
    admin_function()
    superuser_function()
