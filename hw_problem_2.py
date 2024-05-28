# HW_P2: Dictionary Manipulation and Optimization
'''
Objective: Understand Python dictionaries by exploring advanced manipulation techniques and optimization strategies.

Problem Statement: Explore advanced manipulation techniques and optimization strategies for Python dictionaries. Implement various dictionary operations and optimize them for improved performance.
'''

# Task 1
# Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. Analyze the time and space complexity of this operation.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] = value
        else:
            merged_dict[key] = value
    return merged_dict

# Time complexity is O(n) and space complexity is O(n)

ex1 = {
    'apple': 10,
    'banana': 20,
    'cherry': 30
}
ex2 = {
    'banana': 22,
    'mango': 40
}

print(merge_dictionaries(ex1, ex2))


# Task 2
# Implement a function to find the intersection of two dictionaries, i.e., keys common to both dictionaries along with their values. Analyze the time and space complexity of this operation.
def intersection_dictionary(dict1, dict2):
    for key in dict1:
        if key in dict2:
            if dict1[key] == dict2[key]:
                pass
            else:
                pass

# Time complexity is O(n**2) and space complexity is O(1)

# Task 3
# Implement a function to count the frequency of each unique word in a list using a dictionary. Analyze the time and space complexity of this operation.
def word_frequency(list):
    counter = {}
    for word in list:
        if word in counter:
            counter[word] +=1
        else:
            counter[word] = 1
    return counter

# Time complexity is O(1) and space complexity is O(n)