users = []

class User():
    def __init__(self, username, pin, balance=0):
        self.username = username
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount} into account {self.username}")
        self.print_balance()

    def deposit_with_input(self):
        self.deposit(get_amount())

    def withdrawal(self, amount):
        self.balance -= amount
        print(f"Withdrew ${amount} from account {self.username}")
        self.print_balance()

    def withdrawal_with_input(self):
        self.withdrawal(get_amount())

    def request_balance(self):
        return self.balance

    def print_balance(self):
        print(f"Balance for {self.username}: ${self.balance}")

users.append(User("spudmix", "1234"))

def check_user_exists(username):
    return username in [user.username for user in users]

def get_user(username):
    return [user for user in users if user.username == username][0]

def check_user_pin(user, pin):
    return user.pin == pin

def try_username(max_tries):
    user_prompt = "Enter Username: "

    for i in range(max_tries):
        user_input = input(user_prompt)
        if check_user_exists(user_input):
            return get_user(user_input)
        else:
            print("User not found")
    return False

def try_pin(max_tries, user):
    pin_prompt = "Enter Password: "

    for i in range(max_tries):
        pin_input = input(pin_prompt)
        if check_user_pin(user, pin_input):
            return user
        else:
            print("Wrong password")
    return False

def get_amount():
    while True:
        amount_prompt = "Enter Amount: $"
        input_amount = validate_number(input(amount_prompt))
        if input_amount:
            return input_amount
        else:
            print("Please enter a number")

def validate_number(num):
    try:
        return float(num)
    except:
        return False

def main_menu(current_user):
    options = {
        '1': current_user.deposit_with_input,
        '2': current_user.withdrawal_with_input,
        '3': current_user.print_balance,
        '4': False,
        'x': False,
    }

    prompt = "Choose an option: \n"\
             "1: Deposit\n"\
             "2: Withdrawal\n"\
             "3: Request Balance\n"\
             "4: Exit\n"

    while True:
        input_string = input(prompt).strip()
        if input_string in options:
            if not options[input_string]:
                break
            else:
                options[input_string]()
        else:
            print("Please choose an option from the list")

def login():
    user = try_username(3)
    if user:
        current_user = try_pin(3, user)
        if current_user:
            print(f"Succesfully logged in as {current_user.username}")
            return current_user
        else:
            print(f"Password lockout")
            return False
    else:
        print(f"Username lockout")
        return False

current_user = login()
if current_user:
    main_menu(current_user)