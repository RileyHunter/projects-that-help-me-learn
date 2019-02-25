def cels_to_fahr(cels):
    return (cels * (9.0/5.0)) + 32

def fahr_to_cels(fahr):
    return (fahr - 32) * (5.0/9.0)

def is_a_num(num):
    try:
        float(num)
        return True
    except:
        print(f"{num} is not a number")
        return False

conversion_options = {
    'a': cels_to_fahr,
    'b': fahr_to_cels
    }

continue_options = {
    'y': True,
    'n': False
    }

while True:
    choice = input(f"Choose a conversion: "\
                   f"\na: Celsius to Fahrenheit"\
                   f"\nb: Fahrenheit to Celsius\n")

    if not choice in conversion_options:
        print("That wasn't an option")
        continue

    num = input(f"Enter a temperature: ")
    while not is_a_num(num):
        num = input(f"Enter a temperature: ")

    print(f"{num} converts to {conversion_options[choice](float(num))}")

    choice = input(f"Continue? (y/n)")
    while not choice in continue_options:
        print("That wasn't an option")
        choice = input(f"Continue? (y/n)")

    if not continue_options[choice]:
        break
