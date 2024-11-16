def create_dict_from_lists(keys, values):
    """
    This function returns a dict made from two lists.
    """
    return dict(zip(keys,values))

def merge_two_dicts(d1, d2):
    """
    Merge two Python dictionaries into one
    """
    d1.update(d2)
    return d1


def init_dict_with_values(lst, d1):
    """
    Create a dict with default values for each key listed.

    """
    d2 = {}
    for i in lst:
        d2[i] = d1

    return d2


def extract_keys_to_dict(datadict, keylist):
    """
    Create a dictionary by extracting the keylist from a given dictionary
    """
    d = {}
    for i in keylist:
      d[i] = datadict[i]
      
    return d

def delete_keys_from_dict(datadict, keylist):
    """
    Delete a list of keys from a dictionary
    """
    d = datadict.copy()
    for i in keylist:
      d.pop(i)
      
    return d

def check_dict_for_key(datadict, key):
    """
    Check if a value exists in a dictionary
    (NO FOR loops!)
    """
    return key in datadict.values()

def get_key_of_min_value(ddd):
    """
    Get the key of the minimum value from a dictionary
    """

    s = min(ddd.values())
    for key, value in ddd.items():
      if value == s:
          return key
    

def get_key_of_max_value(ddd):
    """
    Get the key of the maximum value from a dictionary
    """
    s = max(ddd.values())
    for key, value in ddd.items():
      if value == s:
          return key