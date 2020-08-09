#!/usr/bin/python3

from ans1 import *

# CSCI 656: practice w/ list comprehensions
# Due Fri Feb 14 at 11:59 PM

# CORRECTED VERSION of Thu 2/13/2020
# - Deadline extended
# - Additional comments added
# - Duplicate answer to #7 deleted
# - Buggy answer to #13 in corrected

# Assignment: Write each of these functions without any for-loops or while-loops.

# Using list comprehensions is fine. While they have the same effect as for-loops,
# put less cognitive load on the programmer, i.e., you can think more about the
# data structure you are trying to build and less about how to creat it.

# Using lambda functions is fine also, but will be harder for most people.

# Rules:
# - No for-loops or while-loops
# - Follow style guide
# - You must use the auxiliary function you write!
# - Functions should not wipe out their own input.

# Submission: Submit a file containing only your functions. 

# Use the following format for submission:
# Name your function ans1.py
# Zip it up in a file called hw1-xxxx.zip, where xxxx = your 4-letter ID in lower case
# Submit the zip file on Blackboard

# Zip means zip, not bzip2 or gzip or rar or whatever
# No extra files, extra subdirectories or whatever


# I will grade your functions by running my own driver, which uses the same
# calling sequences but different data.

# I suggest you test your functions as follows:
# ./driver1.py > your_output.py
# diff -Bb your_output.py out1.py

# Suggestions:

# 1) Here are some functions you might find useful:
# any, all, sum, zip, enumerate

# 2) Also google 'python 3 functional programming'. There is a HOWTO on
# python.org, but I don't think it's one of the better ones.

# 3) You are welcome to write your own auxiliary functions too.

# 4) If you are looking for ways to ensure that elements of a list are unique,
# try building a 'dict' or 'set'

# --

# 1. Write a function alpha_fn(x) that takes a string and returns True if
# the string is alphabetic, otherwise False. If the input is the empty string,
# return True (all of its characters are alphabetic; there just don't happen
# to be any. This is the mathematical approach to empty lists, but it's
# not how Python treats them).

# See the comments to #4 for further discussion of how empty sequences
# (strings or lists) should be treated, and how those functions should
# be named.

# It's fine to call an existing Python function to check for alphas. In fact,
# it's a good idea for two reasons. Reinventing the wheel is a waste of time,
# and also has the disadvantage that it might create an inconsistency between
# your definition and the system definition.

# The purpose of the question is to show how you can convert a member function
# to a non-member function if you want one, for example, as an argument to a
# lambda.

print ("1. ", "is '3' alphabetic?  ", alpha_fn('3'))
print ("   ", "is 'x$z' alphabetic?", alpha_fn('x$z'))
print ("   ", "is '' alphabetic?   ", alpha_fn(''))
print ("   ", "is 'été' alphabetic?", alpha_fn('été'))
print()


# 2. Write a function is_noun(x) that takes a part of speech such as
# 'NNP' and returns True if the POS represents a noun, otherwise False.
# A POS represents a noun if its first two letters are 'NN'.

print ("2. ", "is NNP a noun? ", is_noun('NNP'))
print ("   ", "is VP a noun?  ", is_noun('VP'))
print ("   ", "is N a noun?   ", is_noun('N'))
print ("   ", "is PNN a noun? ", is_noun('PNN'))
print ("   ", "is nn a noun?  ", is_noun('nn'))
print()


# 3. Write a function is_even(x) that returns True if x is an even number,
# otherwise False. You can assume that the function will only be called
# with integer arguments.

print ("3. ", "is 3 even?  ", is_even(3))
print ("   ", "is 0 even?  ", is_even(0))
print ("   ", "is -2 even? ", is_even(-2))
print()

# 4. Write a function is_any_even(x) that returns True if any element of
# the input list is even, or if the list is empty.
# Use the function you wrote above.
# You can assume that all of the elements in the original list are numeric.

# Having this function return True makes sense in an application where you
# want to ensure that only even numbers get through a pipeline.

# It would not make sense in a different kind of application, where
# you wanted to guarantee that there were some even numbers available in
# the pipeline.

# In my own code, I would call the function "at_least_one(x)" if I
# wanted the other meaning. But now that both Python and Java streams do it
# the other way, perhaps I should be the one to change. Lisp avoids this
# problem by calling the corresponding predicate 'some()'.

print("4. ", "[1, 2, 3]", is_any_even([1, 2, 3]))
print("   ", "[1, 3, 5]", is_any_even([1, 3, 5]))
print("   ", "[]       ", is_any_even([]))
print()      

# 5. Given a list such as v1 = [1, 3, 5, 7, 9], write a function
# f1(v) that returns a list containing (x + 1)^2 for each element
# in the input.
# You can assume that all of the elements in the original list are numeric.

v1 = [2, 0, -2, 4, 6]
v2 = f1(v1)

print("5. ", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()

# 6. Similar to the previous question, write a function f2(v) that
# returns x^2 + 2x + 1 for each element x in the list.
# You can assume that all of the elements in the original list are numeric.

v1 = [2, 0, -2, 4, 6]
v3 = f2(v1)

print("6. ", "If the input is ", v1)
print("   ", "the output is   ", v3)
print()

# 7. Write a function are_same(list1, list2) that can be used
# to see if the answers to the preceding two questions are the same

print("7. ", "If the inputs are ", v2, " and ", v3)
print("   ", "the output is", are_same(v2,v3))
print()

# 8. Given a list such as v2 = ['N', 'V', "JJ", "NS", "N$"],
# write a function drop_bad(x) that returns a list that contains only
# the alphabetic elements in x, using the function you wrote earlier.
# In this example the result would be ['N', 'V', "JJ", "NS"].

v1 = ['abc', 'x$z', '3']
v2 = drop_bad(v1)

print("8. ", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()

# 9. Given a list such as v2 = ['N', "N$"],
# write a function label_bool(x) that labels all the elements in x
# as alphabetic or non-alphabetic using the following form:
# [['N', True], ['N$', False]]
# Use the function you wrote earlier.

v1 = ['abc', 'x$z', '3']
v2 = label_bool(v1)

print("9. ", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()


# 10. Given a list such as v2 = ['N', "N$"],
# write a function label_bad(x) that labels all the elements in x
# as alphabetic or non-alphabetic using the following form:
# [['N', 'yes'], ['N$', 'no']]
# Use the function you wrote earlier.

v1 = ['abc', 'x$z', '3']
v2 = label_bad(v1)

print("10.", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()


# 11. Given a list in the format of the output from #9,
# write a function count_good(x) that counts the number of
# elements marked true

v1 = [['abc', True], ['def', False], ['ghi', True]]
n = count_good(v1)

print("11.", "If the input is ", v1)
print("   ", "the output is   ", n)
print()


# 12. Given a list in the format of the output from #10,
# write a function count_bad(x) that counts the number of
# elements not labeled 'yes'

v1 = [['abc', 'yes'], ['def', 'no'], ['ghi', 'whatever'], ['jkl', 'no']]
n = count_bad(v1)

print("12.", "If the input is ", v1)
print("   ", "the output is   ", n)
print()


# 13. Given a list of words and parts of speech such as
# v2 = [['book', ['NN', 'VB']], ['is', ['VBZ']], ['of', ['PP']]]

# write a function show_nouns2(x) that returns a list of the same format
# containing only the nouns.

# Given an expression [s, list], s is a noun if at least one of the
# items in the list is a noun label. Use the function you wrote
# earlier.

# (What this data structure is showing is that words like 'book and
# 'flour' can be either nouns or verbs.)

v1 = [['book', ['NN', 'VB']], ['flour', ['VB', 'NN']], ['the', ['DT']]]
v2 = show_nouns2(v1)

print("13.", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()

# 14. Given a list of the format above, write a function show_nouns3(x)
# that returns a simple list containing only the nouns, e.g.
# ['book', 'x']. Use the function you wrote earlier.

v1 = [['book', ['NN', 'VB']], ['flour', ['VB', 'NN']], ['the', ['DT']]]
v2 = show_nouns3(v1)

print("14.", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()


# 15. Given a list of lists of numbers
# where the sublists do not necessarily have the same lengths
# e.g., v1 = [[1, 2, 3], [5, 4]],
# write a function show_count(x) that produces the total number of entries
# in the sublists, e.g., 5 for the list above.

v1 = [[1, 2, 3], [5, 4]]
v2 = show_count(v1)

print("15.", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()

            
# 16. Write a function show_totals(x) that produces a list where each
# sublist has been summed, e.g., [6, 9] for the list above.

v1 = [[1, 2, 3], [5, 4]]
v2 = show_totals(v1)

print("16.", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()


# 17. Write a function show_total(x) that produces the sum of the values
# in the sublists e.g. 15 for the list above.

v1 = [[1, 2, 3], [5, 4]]
v2 = show_total(v1)

print("17.", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()


# 18. Given a list containing two sublists of the same length
# e.g., v2 = [[1, 2, 3], [5, 4, 7]], 
# write code to produce the dot product of the sublists, e.g. 34 for the 
# list above (= 1*5 + 2*4 + 3*7)

v1 = [[1, 2, 3], [5, 4, 7]]
v2 = dot_product(v1)

print("18.", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()


# 19. Given a list of words, write a function count_distinct(x)
# write that returns the number of distinct
# words in the sentence, e.g., 5 for the sentence above.
# This function should be case-independent, i.e., 'the' and 'The'
# and 'THE' are the same word.
# Strings with non-alphabetic characters do not count as words.
# Note: NLP calculations are usually case-independent. That is usually
# achieved by making a lower-case version of the input.

v1 = ['The', 'black', 'horse', 'named', 'Black', 'is', 'black', '.']
v2 = count_distinct(v1)

print("19.", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()


# 20. Prof. Untel (that is French for “So-and-so”) represents student
# grades in a list, as follows:
# [['Aaa', 'g', [2, 4, 5]],['Bbb', 'u', [4, 5, 6]], etc.] means that
# student Aaa got 2 on HW1 (not HW0!), 4 on HW2, etc.
# The second argument represents grad/undergrad. Write a function
# avg_grade(x) giving the average grade for HW1.

v1 = [['Aaa', 'g', [2, 4, 5]],
      ['Bbb', 'u', [4, 5, 6]],
      ['Ccc', 'g', [7, 8, 9]],
      ['Ddd', 'u', [1, 2, 3]],
      ['Eee', 'u', [4, 5, 7]]]

v2 = avg_grade(v1)

print("20.", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()


# 21. Write a function ugrad_points(x) giving the total number of points
# earned on HW2 by undergraduates.

v2 = ugrad_points(v1)

print("21.", "If the input is ", v1)
print("   ", "the output is   ", v2)
print()
