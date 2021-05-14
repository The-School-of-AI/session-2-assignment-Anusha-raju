# KINDLY GO THROUGH TEST FILE TO UNDERSTAND
from typing import List
import time
import gc
# Here in this code we will be leaking memory because we are creating cyclic reference.
# Find that we are indeed making cyclic references.
# Eventually memory will be released, but that is currently not happening immediately.
# We have added a function called "clear_memory" but it is not able to do it's job. Fix it.
# Refer to test_clear_memory Test in test_session2.py to see how we're crudely finding that
# this code is sub-optimal.
class Something(object):
    def __init__(self):
        super().__init__()
        self.something_new = None
    def __repr__(n):
        return "Something's class __repr__"
class SomethingNew(object):
    def __init__(self, i: int = 0, something: Something = None):
        super().__init__()
        self.i = i
        self.something = something
    def __repr__(n):
        return "SomethingNew class __repr__"
def add_something(collection: List[Something], i: int):
    something = Something()
    something.something_new = SomethingNew(i, something)
    collection.append(something)
def reserved_function():
    # to be used in future if required
    pass
def clear_memory(collection: List[Something]):
    # you probably need to add some comment here
    collection.clear()
    gc.collect()
def critical_function():
    collection = list()
    for i in range(1, 1024 * 128):
        add_something(collection, i)
    clear_memory(collection)
# Here we are suboptimally testing whether two strings are exactly same or not
# After that we are trying to see if we have a particular character in that string or not
def compare_strings_old(n):
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    for i in range(n):
        if a == b:
            pass
    char_list = list(a)
    for i in range(n):
        if 'd' in char_list:
            pass
def compare_strings_new(n):
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    if a is b:
        pass
    new_char_list=list(a)
    if "d" in new_char_list:
        pass
