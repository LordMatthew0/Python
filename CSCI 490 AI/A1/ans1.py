#!/usr/bin/python3

# CSCI 656: practice w/ list comprehensions
# Due Thu Feb 13 at 11:59 PM

# Assignment: Write each of these functions without any for-loops or while-loops.

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

# 3) You are welcome to write your own auxiliary functions to

# 1. Write a function alpha_fn(x) that takes a string and returns True if
# the string is alphabetic, otherwise False. If the input is the empty string,
# return True (all of its characters are alphabetic; there just don't happen
# to be any. This is the mathematical approach to empty lists, but it's
# not how Python treats them). 

def alpha_fn(x):
    if (len(x)) == 0: #check if string is empty 
        return "True"
    elif (len(x)) > 0:
        return x.isalpha() #see if string is alphabetical
    else:
        return "False"

def isnotalpha(x):
    if x.isalpha():
        return False
    else:
        return True

# 2. Write a function is_noun(x) that takes a part of speech such as
# 'NNP' and returns True if the POS represents a noun, otherwise False.
# A POS represents a noun if its first two letters are 'NN'.

def is_noun(x):
    first_char = 'f'
    second_char = 'f'
    if (len(x)) >= 2:
        first_char = x[0]
        second_char = x[1]
        
    if (first_char == 'N' and second_char == 'N'):
        return "True"
    else:
        return "False"

# 3. Write a function is_even(x) that returns True if x is an even number,
# otherwise False. You can assume that the function will only be called
# with integer arguments.

def is_even(x):
    if (x % 2) == 0:
        return "True"
    else:
        return "False"    

# 4. Write a function is_any_even(x) that returns True if any element of
# the input list is even, or if the list is empty.
# Use the function you wrote above.
# You can assume that all of the elements in the original list are numeric.

def is_any_even(x):
    if (len(x)) == 0:
        return "True"
    f = sum(x)
    if (is_even(f)) == "True":
        return "True"
    else:
        return "False"
         

# 5. Given a list such as v1 = [1, 3, 5, 7, 9], write a function
# f1(v) that returns a list containing (x + 1)^2 for each element
# in the input.
# You can assume that all of the elements in the original list are numeric.

def f1(v):
    return [(x+1)**2 for x in v]

# 6. Similar to the previous question, write a function f2(v) that
# returns x^2 + 2x + 1 for each element x in the list.
# You can assume that all of the elements in the original list are numeric.

def f2(v):
    return [((x)**2 + 2*x +1) for x in v]

# 7. Write a function are_same(list1, list2) that can be used
# to see if the answers to the preceding two questions are the same

def are_same(list1, list2): 
    if (list1 == list2):
        return "True"
    else:
        return "False"

# 8. Given a list such as v2 = ['N', 'V', "JJ", "NS", "N$"],
# write a function drop_bad(x) that returns a list that contains only
# the alphabetic elements in x, using the function you wrote earlier.
# In this example the result would be ['N', 'V', "JJ", "NS"].

def drop_bad(x):
    return [f for f in x if f.isalpha()]

# 9. Given a list such as v2 = ['N', "N$"],
# write a function label_bool(x) that labels all the elements in x
# as alphabetic or non-alphabetic using the following form:
# [['N', True], ['N$', False]]
# Use the function you wrote earlier.

def label_bool(x):
    return [[f,f.isalpha()] for f in x]

# 10. Given a list such as v2 = ['N', "N$"],
# write a function label_bad(x) that labels all the elements in x
# as alphabetic or non-alphabetic using the following form:
# [['N', 'yes'], ['N$', 'no']]
# Use the function you wrote earlier.

def label_bad(x):
    k = [[f,"yes"] for f in x if f.isalpha()]
    g = [[f, "no"] for f in x if isnotalpha(f)]
    k.append(g)
    return k

# 11. Given a list in the format of the output from #9,
# write a function count_good(x) that counts the number of
# elements marked true

def count_good(x):
    return sum(g.count(True) for g in x)
    

# 12. Given a list in the format of the output from #10,
# write a function count_bad(x) that counts the number of
# elements not labeled 'yes'

def count_bad(x):
    return sum(g.count('no') for g in x)

# 13. Given a list of words and parts of speech such as
# v2 = [['book', ['NN', 'VB']], ['is', ['VBZ']], ['of', ['PP']]]


# write a function show_nouns2(x) that returns a list of the same format
# containing only the nouns.

# Given an expression [s, list], s is a noun if at least one of the
# items in the list is a noun label. Use the function you wrote
# earlier.

# (What this data structure is showing is that words like 'book and
# 'flour' can be either nouns or verbs.)

def show_nouns2(x):
    return [a for a in x for b in a for c in b if is_noun(c) == "True"]


# 14. Given a list of the format above, write a function show_nouns3(x)
# that returns a simple list containing only the nouns, e.g.
# ['book', 'x']. Use the function you wrote earlier.

def show_nouns3(x):
        return [a[0] for a in x for b in a for c in b if is_noun(c) == "True"]

  
# 15. Given a list of lists of numbers
# where the sublists do not necessarily have the same lengths
# e.g., v1 = [[1, 2, 3], [5, 4]],
# write a function show_count(x) that produces the total number of entries
# in the sublists, e.g., 5 for the list above.

def show_count(x):
    return len(x[0]) + len(x[1]);
            
# 16. Write a function show_totals(x) that produces a list where each
# sublist has been summed, e.g., [6, 9] for the list above.

def show_totals(x):
    f = '[' + str(sum(x[0])) + ', ' + str(sum(x[1])) + ']'
    return  f

# 17. Write a function show_total(x) that produces the sum of the values
# in the sublists e.g. 15 for the list above.

def show_total(x):
    return sum( sum(g) if isinstance(g, list) else g for g in x )

# 18. Given a list containing two sublists of the same length
# e.g., v2 = [[1, 2, 3], [5, 4, 7]], 
# write code to produce the dot product of the sublists, e.g. 34 for the 
# list above (= 1*5 + 2*4 + 3*7)

def dot_product(x):
    return sum(i[0] * i[1] for i in zip(x[0], x[1]))

# 19. Given a list of words, write a function count_distinct(x)
# write that returns the number of distinct
# words in the sentence, e.g., 5 for the sentence above.
# This function should be case-independent, i.e., 'the' and 'The'
# and 'THE' are the same word.
# Strings with non-alphabetic characters do not count as words.
# Note: NLP calculations are usually case-independent. That is usually
# achieved by making a lower-case version of the input.

def count_distinct(x):
    words = [l.lower() for l in x]
    alpha_only = [l for l in words if l.isalpha()]
    unique_words = set(alpha_only)
    unique_word_count = len(unique_words)
    return unique_word_count

# 20. Prof. Untel (that is French for “So-and-so”) represents student
# grades in a list, as follows:
# [['Aaa', 'g', [2, 4, 5]],['Bbb', 'u', [4, 5, 6]], etc.] means that
# student Aaa got 2 on HW1 (not HW0!), 4 on HW2, etc.
# The second argument represents grad/undergrad. Write a function
# avg_grade(x) giving the average grade for HW1.

def avg_grade(x):
    l = [a[2] for a in x ]
    s = sum(a[0] for a in l)
    c = len(x);
    return s/c

# 21. Write a function ugrad_points(x) giving the total number of points
# earned on HW2 by undergraduates

def ugrad_points(x):
    l = [a[2] for a in x if a[1] == 'u']
    s = sum(a[1] for a in l)
    return s
