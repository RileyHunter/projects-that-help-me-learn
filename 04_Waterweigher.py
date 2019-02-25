## Waterweigher
"""
Assume that a gallon of water weighs 8.33 pounds
Prompt the user to enter a number of gallons
Display the total weight of the water in pounds
"""

"""
This one is quite a bit shorter than the previous one, the only
tricky bit is ensuring that the user is giving you a number and
not some other garbage.

First, let's store a constant for our weight ratio:
"""

ratio = 8.33

"""
Then, we need a way to tell if a string is able to be read as
a number. To do this we're going to use a try-except block:
"""

def is_a_number(num):
    try:
        """
        string.strip() is a useful pre-process tool to help
        sanitise strings and prevent whitespace from breaking
        things
        """
        float(num.strip())
        return True
    except:
        print(f"{num} is not a number")
        return False
    """
    What the above code does is tries to cast the number we set
    as a floating point number (think a decimal). The try-except
    block functions such that if anything goes wrong, instead of
    crashing the program, it simply executes the except block.
    """

"""
Now that we're set up, we need a loop until a certain condition
is met. This is the place for a WHILE.

Notice that we ask once, then verify the number while asking
again until it works.
"""

num = input("Please enter a number of gallons: ")
while not is_a_number(num):
    """
    WHILE <condition> simply keeps going until the condition is
    no longer true - in this case, we want to keep going until
    it is not true that num is not a number. Double negative,
    I know.
    """
    num = input("Please enter a number of gallons: ")

"""
Finally, cast the number to a float (we know this will work now)
and print out. You can perform calculations like * inside
f-formatted strings.
"""
num = float(num)
print(f"{num} gallons weighs {num * ratio} lbs")
