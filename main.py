"""In the code cell below, complete the following:

    Make a copy of starting_list in a variable called sliced_copy by indexing the whole list to make a copy
    Make a copy of starting_list in a variable called copy_copy by using the built in .copy() method
    Make a copy of starting_list in a variable called list_copy by using the built in list() function

"""

# Make copies of this list
starting_list = ["This", "is", "a", "list", "that", "needs", "to", "be", "copied"]

# Make copies below
sliced_copy = ["This", "is", "a", "list", "that", "needs", "to", "be", "copied"]
copy_copy = starting_list.copy()
list_copy = list(starting_list)
