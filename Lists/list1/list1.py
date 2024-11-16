from xml.dom.expatbuilder import parseString


## Think SLICING for many of these.

def create_list_from_tuple(t):
    """
    This function takes a tuple of elements and returns a list containing those elements of the tuple.
    """
    return list(t)
    
def drop_last(lst):
    """
    This function takes a list and returns a list with the last item removed.
    """
    return lst[:-1]


def drop_first_two(lst):
    """
    This function takes a list and returns a list with the first two items removed.
    """
    return lst[2:]

def drop_mangle(lst):
    """
    This function takes a list and returns a list with the first two items AND last item removed.
    """
    return  drop_first_two(drop_last(lst))

def add_item_front(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item prepended to the list
    """
    lst.insert(0, a)
    return lst

def add_item_end(lst, a):
    """
    This function takes a list and an item,
    returning the list with the item appended to the list
    """
    lst.append(a)
    return lst

def add_list_to_list(lsta, lstb):
    """
    This function takes two lists and appends one to the other,
    returning a list
    """
    return lsta + lstb

def list_and_list_to_tuple(lsta, lstb):
    """
    This function takes two lists and returns a tuple containing the two lists
    """
    return lsta, lstb

def list_and_list_to_list(lsta, lstb):
    """
    This function takes two lists and returns a list containing the two lists
    """
    return [lsta, lstb]

##
##
##

def list_from_range(n):
    """
    This function returns list with 0..n as integers in a list
    """
    a = list(range(n))
    return a

def list_from_range2(n, m):
    """
    This function returns list with n..m (without m) as integers in a list
    """
    a = list(range(n, m))
    return a

def list_from_range3(n, m):
    """
    This function returns list with n..m (including m(!)) as integers in a list
    """
    a = list(range(n, m+1))
    return a

def list_from_range4(n, m):
    """
    This function returns list with n..m (WITHOUT n and including m) as integers in a list
    """
    a = list(range(n+1, m+1))
    return a

def list_from_range_by(n, step):
    """
    This function returns list with 0..n as integers by step in a list
    (read the test)
    """
    a = list(range(n))
    return a[::step]

def rev_list(lst):
    """
    This function returns list which is a reverse of the argument list
    (read the test)
    """
    return list(reversed(lst))
  
def concat_list_indexwise(lst1, lst2):
    """
    Write a program to add two lists index-wise. 
    Create a new list that contains the 0th index item from both the list, 
    then the 1st index item, and so on till the last element. 
    Any leftover items will get added at the end of the new list.
    """
    a = []
    for i in range(min(len(lst1), len(lst2))):
        a.append(lst1[i] + lst2[i])

    a.extend(lst1[len(lst2):])
    a.extend(lst2[len(lst1):])

    return a


def square_each_item(lst):
    """
    This function returns list which each item in argument list has been squared
    (read the test)
    """

    return [x ** 2 for x in lst]

def remove_empty_strs(lst):
     """
     Remove empty strings from the list of strings
     """
     for x in lst:
         if x == "":
             lst.remove(x)
     return lst

def remove_item_from(lst, aaa):
    """
    Remove all occurrences of a specific item from a list.
    """
    return [x for x in lst if x != aaa]

def leave_item_in(lst, aaa):
    """
    Leave all occurrences of a specific item in a list.
    """
    return [x for x in lst if x == aaa]

def length_of(lst):
    """
    return the length of the list
    """
    return len(lst)