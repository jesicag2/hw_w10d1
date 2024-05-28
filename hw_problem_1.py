# HW_P1: Advanced Operations on Python Lists
'''
Objective: Understand Python lists by exploring more complex operations, such as list comprehension, slicing, and sorting, and analyzing their time and space complexities.

Problem Statement: Delve deeper into Python lists and master advanced operations. Implement various complex tasks using lists and analyze their efficiency in terms of time and space complexities.
'''

# Task 1
# Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, where n is a parameter. Analyze the time and space complexity of this operation.
def new_list(n):
    squares = []
    for i in range(1, n+1):
        squared = (i**2)
        squares.append(squared)
    return squares

# Time complexity is O(n) and space complexity is O(n)

print(new_list(2))
print(new_list(4))
print(new_list(8))
print(new_list(10))


# Task 2
# Implement a function to reverse a sublist within a list from index i to j (inclusive). Analyze the time and space complexity of this operation
def reverse_sublist(arr, i, j):
    arr[i:j+1] = reversed(arr[i:j+1])
    return arr

# Time complexity is O(n) and space complexity is O(1)

example = [1, 2, 3, 4, 5, 6, 7, 8]
print(reverse_sublist(example, 2, 5))


# Task 3
# Implement a function to merge two sorted lists into a single sorted list. Analyze the time and space complexity of this operation.
def merged_sprted_lists(arr, arr2):
    arr = sorted(arr)
    arr2 = sorted(arr2)
    merged_list = arr + arr2
    return merged_list

# Time complexity is O(n) and space complexity is O(n)

ex1 = [2, 4, 88, 5, 9]
ex2 = [5, 8, 10, 4]
print(merged_sprted_lists(ex1, ex2))