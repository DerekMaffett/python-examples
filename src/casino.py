# Here we import from the `collection.py` file. Python automatically knows that the module is called "collection"
# We could also `import *`, but that would pull all defined functions, and we don't want that. 
from collection import filter_for_indices

# We can break this problem into smaller ones, each its own function:

# 1. The base function. This does a non-standard filter on a list of strings, filtering on word-match criteria, 
#    so we just do that and push the weird filter function and word match aside for now to tackle them later. 
# 2. The filter function. We'll do that in `collection.py` and import the function into this file. 
# 3. The word-match function for a single doc. This is most of the actual "logic" so we tackle it and split it up as necessary.

def word_search(doc_list, search_term):
    contains_passed_search_term = lambda text: doc_contains_term(search_term, text)

    return filter_for_indices(contains_passed_search_term, doc_list)


# Below are examples of how we could gradually build up the logic. Each step is paired with the writing of new (failing) tests 
# in casino_test.py as described in that file, with the tests written first, then the code to make them pass. 

# Of course in reality we wouldn't copy-paste the steps - this is for demonstration purposes.




# Basic implementation of the logic. We leave this as a first pass to confirm it
# passes the simplest "happy path" tests.

# def doc_contains_term(search_term, text):
#     return search_term in text



# Adding the "ignore partial word match" requirement

# def doc_contains_term(search_term, text):
#     words = text.split()
#
#     # You could also use a lambda function like we did in the word_search function,
#     # but apparently a generator comprehension like this below is more "normal" in Python. 
#     # I'm not very familiar with them but it's a similar concept. 
#     return any(word_matches(search_term, word) for word in words)
#
# def word_matches(search_term, word):
#     return word == search_term



# Added case-insensitivity tests, so now we need the word match to satisfy that

# def doc_contains_term(search_term, text):
#     words = text.split()
#
#     return any(word_matches(search_term, word) for word in words)
#
# def word_matches(search_term, word):
#     return word.lower() == search_term.lower()



# Added punctuation ignoring tests. This completes all the requirements!

def doc_contains_term(search_term, text):
    words = text.split()

    return any(word_matches(search_term, word) for word in words)

def word_matches(search_term, word):
    return word.lower().strip(".,") == search_term.lower()
