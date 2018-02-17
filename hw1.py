print ("hello")

"""
1- Install and Test Python Environment Install python 2.7
environment, save the following code with name "hw1.py"
(note that python is indentation sensitive)
"""


def test_print():
    print "This is a test statement."


if __name__ == '__main__':
    test_print()

"""
2. Define Objects:
Define a function called 'list_set_length' to assign items_list= [1, 2, 3, 4, 3, 2, 1] as a list object,
and items_set = {1, 2, 3, 4, 3, 2, 1} as a set object.Use the len function, print the size of the list and
size of the set


"""

item_list = [1, 2, 3, 4, 3, 2, 1]
set_list = {1, 2, 3, 4, 3, 2, 1}


def list_set_define():
    return list(item_list)
    return set(set_list)


def length_list(item_list, set_list):
    print(len(item_list))
    print(len(set_list))


length_list(item_list, set_list)

""" 3. Comprehension for intersection between two given sets """

s = {1, 2, 3, 4, 6, 5, 8, 7}
t = {2, 3, 5, 6}


def set_intersect(s, t):
    intersect = {element for element in s if element in t}
    display_intersect(intersect)
    return intersect


def display_intersect(intersect):
    print(intersect)


set_intersect(s, t)


""" 4. Function three tuples that includes triple comprehension and returns list of all those elements whose
 sum is equal to 0.
"""

ex = {-4, -2, 1, 2, 5, 0}


def three_tuple(ex):
    result = {(i, j, k) for i in ex for j in ex for k in ex if i + j + k == 0}
    print(result)


three_tuple(ex)

""" 5. dictionary """

dicionary_list = [{'Neo': 'Keanu', 'Morpheus': 'Laurence', 'Trinity': 'Carrie-Anne'}]


def dict_find(dictionary_list):
    key = 'Neo'
    result = {d.get(key, 'NOT PRESENT') for d in dictionary_list}
    print(result)


dict_find(dicionary_list)

"""
 6. 'file_line_count 'to open a file and  return the number of lines that it has
"""


def file_line_count(file_name):
    num_lines = sum(1 for line in file_name)
    print(num_lines)


file_line_count(open('small_stories.txt'))

"""7. Mini Search engine"""

"""a. making of inverse index"""

input_list = open('small_stories.txt').readlines()  # input list of documents as strings

inverseIndex = {}  # empty set


def make_inverse_index(text1):
    for (i, doc) in enumerate(text1):
        for word in doc.split():
            if word in inverseIndex:
                inverseIndex[word].add(i)
            else:
                inverseIndex[word] = set()
                inverseIndex[word].add(i)
    print(inverseIndex)
    return inverseIndex


make_inverse_index(input_list)


"""7.b 
an inverse index and a list of words query, and returns the set of document numbers specifying
all documents that contain any of the words in query."""


def or_search(inverseIndex, query):
    res = set()  # empty
    for word in query:
        if word not in inverseIndex:
            return res  # if query not found
        for id in inverseIndex[word]:
            res.add(id)
    print(res)
    return res


test1 = ['the']

or_search(inverseIndex, query=test1)

""" 7.c 
an inverse index and a list of words query, and returns the set of document numbers specifying
all documents that contain all of the words in query."""


def and_search(inverseIndex, query):
    res1 = set()  # empty
    for word in query:
        if word not in inverseIndex:
            return res1  # if query not found

    res1 = inverseIndex[query[0]]
    for word in query:
        res1 = res1 & inverseIndex[word]
    print(res1)
    return res1


test2 = ['four', 'military-news']

and_search(inverseIndex, query=test2)

