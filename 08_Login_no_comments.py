users = []

class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password

users.append(User("spudmix", "asd"))
current_user = None

def check_user_exists(username):
    return username in [user.username for user in users]

def get_user(username):
    return [user for user in users if user.username == username][0]

def check_user_password(user, password):
    return user.password == password

def try_username(max_tries):
    user_prompt = "Enter Username: "

    for i in range(max_tries):
        user_input = input(user_prompt)
        if check_user_exists(user_input):
            return get_user(user_input)
        else:
            print("User not found")
    return False

def try_password(max_tries, user):
    pass_prompt = "Enter Password: "

    for i in range(max_tries):
        pass_input = input(pass_prompt)
        if check_user_password(user, pass_input):
            return user
        else:
            print("Wrong password")
    return False

user = try_username(3)
if user:
    current_user = try_password(3, user)
    if current_user:
        print(f"Succesfully logged in as {current_user.username}")
    else:
        print(f"Password lockout")
else:
    print(f"Username lockout")