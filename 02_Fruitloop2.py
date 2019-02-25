## Fruitloop2
"""
Repeat Fruitloop1, but for each fruit name that you display, on
the next line display the number of periods that is equal to the
number of the index of the array.

Example: "Banana" . //one period
"Orange" .. //two periods etc.
"""

"""
We'll follow the same structure for this question as the last,
but we're going to use a new concept: a function!

We need a function to create the string of periods of some
length later, and in Python this needs to be defined before
(above) where it is called. You can think of a function as
a little chunk of code that you might use multiple times,
so you put it somewhere safe for later reference.

This begins with a function definition, like so:
"""

def get_period_string(num_periods):
    """
    Then, we define the logic for creating a string of periods
    of arbitrary length, using a FOR loop again:
    """
    output = ""
    for i in range(num_periods):
        output += "."
    """
    Then the return statement tells the program to send something
    back out to the main program, or wherever this function is
    called:
    """
    return output

    """
    We can now call this to get a string of periods as long as we
    need, whenever we need it, by typing get_period_string(num)
    """

"""
Same setup as last time:
"""

my_fruit = ["Apple", "Orange", "Banana", "Pear", "Grape", "Plum"]
array_length = len(my_fruit)

for i in range(0, array_length):
    """
    Now, we're going to print a fruit name:
    """
    print(my_fruit[i])
    """
    But before we go on, we need a way to get a string with some
    number of periods in it. I remember making one of those!
    """
    print(get_period_string(i + 1))
    """
    Just the same as we called print() with an item to print out,
    we can create ourselves a NEW function to create a string, or
    a sequence of characters, to our specifications. In this case
    we want a string of periods, as long as the number of
    iterations in our FOR loop. Remember our loop counts
    half-open, like this: (0, n] so we need to pass in the
    iteration plus one to get the right number of periods.
    """

