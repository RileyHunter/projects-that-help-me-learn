## MadLib
"""
Create a "MadLib" that asks the user for various pieces of
information. Store the information as strings. Once the
information has been collected, output a story using the
stored information. You can find a template if you don't want to
make one: http://www.madlibs.com/
"""

"""
This one is quite a step up. It involves a few new concepts, such
as storing user input.

First of all, I can see that we're going to want to repeatedly
ask a user for input, and store their answers somewhere. For this
task, we could use an array like FruitLoops, but let's not fill
it up yet:
"""

info_list = []

"""
Side note: this isn't really an array. It's a list. I lied.
Python is weird and does lots of strange stuff that other
languages cry about so it's not worth getting caught up on.

For our purposes, a list can be dynamically added to, which
is what we want.

Now let's define a function to get some input from the user and
put it in the info_array:
"""

def get_input_from_user(prompt):
    answer = input(prompt)
    info_list.append(answer)

"""
Python's input() function handles most of the heavy lifting here.
Put simply, the code above allows us to pass a prompt to the
function, which it will then ask the user, and add the reply
to our list of information.


Next, we need a story of sorts. We can make up whatever we want.
I'm going to mark out a basic one here, with placeholders for
the words we want our user to fill in:

    This morning, I <past tense action> and then get up and
    had a shower. In the shower, an <animal> flew in the window
    and scared me so bad that I screamed for my <relative>.

Next, let's get our user to fill in our placeholders:
"""

get_input_from_user("Please give me a past tense action: ")
get_input_from_user("Please give me an animal: ")
get_input_from_user("Please give me a relative: ")

"""
Now that we've got those stored, let's construct our story string
and print it back out. We're going to use f-formatting here,
which allows us to use curled brackets around variables names
inside a string to save us doing lots of string + string = string
"""

my_story = f"This morning, I {info_list[0]} and then got up "\
           f"and had a shower. In the shower, a"\
           f" {info_list[1]} flew in the window and scared me "\
           f"so bad that I screamed for my {info_list[2]}."

"""
Note the trailing backslashes which concatenate the lines of text.

Now, we just print it out:
"""

print(my_story)

"""
Side note: For general purposes, it's nice to not have to think
about which index you're looking for in a data structure if
you're just iterating over them, as above. We can, when using
iterable objects, define an iterator:
"""

info_iter = iter(info_list)

"""
And instead repeatedly call next() on it to achieve the same
result as above without hard-coding any particular values in:
"""

my_iterated_story = f"This morning, I {next(info_iter)} and "\
                    f"then got up and had a shower. In the "\
                    f"shower, a {next(info_iter)} flew in the "\
                    f"window and scared me so bad that I "\
                    f"screamed for my {next(info_iter)}"
