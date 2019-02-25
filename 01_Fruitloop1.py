## Fruitloop 1
"""
Declare and initialize an array of any six fruit names.
Set up a FOR loop and iterate through them (displaying each
value in the console)
"""

"""
This one starts with the very basics - data structures (an array)
and control flow (a FOR loop).

In brief, an array is a set of variables organised and ordered
by an index, starting at zero in most languages. Something like
this:

0 - variable_a
1 - variable_b
...
n - variable_n

In python, we can create an array like this:
"""

my_fruit = ["Apple", "Orange", "Banana", "Pear", "Grape", "Plum"]

"""
Note in particular the square brackets around the data; some other
data structures work in a similar way, and in programming it is
critical we use the right symbols in order to get predictable
behaviour from our code.

Control flow is the concept of changing the order in which code is
executed. There are a few basic control flow statements - IF, ELSE
FOR, WHILE, SWITCH - depending on your language. FOR simply does
whatever is within the loop a set number of times.

In this case, we are going to do something for each item in the
array, so first we're going to grab the length of the array:
"""

array_length = len(my_fruit)

"""
And then we'll declare a FOR loop to run that many times:
"""

for i in range(0, array_length):
    """
    Note that we're now one tab, or four spaces, to the right.
    This is important in Python but not so much in other
    languages.
    
    Now we need to declare what the array should actually do.
    In this case:
    """
    print(my_fruit[i])

    """
    All done! Accessing arrays is easy, just the name of the
    array, and then square braces around the index you want.

    Notice that in the FOR loop, the index i starts at 0 and
    goes up one-by-one until it hits the number BEFORE the top
    of the range. This half-open interval is common in lots of
    languages and frameworks, so get used to it.
    """
