import random

prompt = "Ask me a question!\n"

answers = [
    "Definitely",
    "Maybe",
    "Probably",
    "Probably not",
    "Pay me $5.00 and it'll happen",
    "Only on the third Wednesday in September",
    "Never!",
    "The law requires that I answer no"
]

while True:
    input(prompt)
    print(random.choice(answers))
    choice = input("Want to try again? (y/n)\n")
    while choice not in ["y", "n"]:
        print("That wasn't an option")
        choice = input("Want to try again? (y/n)\n")

    if choice == "n":
        break