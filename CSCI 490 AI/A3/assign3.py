#!/usr/bin/python3

# CSCI 656: movie reviews
# Due Thursday Apr. 16 2020
# Matthew Lord Z1848456

with open('/home/turing/t90rkf1/d656/dhw/hw3-recom/movie-names.txt', encoding='iso-8859-1') as f:
    movieNames = f.readlines()
print(movieNames[0:5])

with open('/home/turing/t90rkf1/d656/dhw/hw3-recom/movie-matrix.txt') as f:
   rawRatings = f.readlines()

#loop through raw ratings
length = len(rawRatings)

for x in range(length):
    rawRatings[x] = rawRatings[x].replace(';;', ';0;')
    rawRatings[x] = rawRatings[x].split(';')
    rawRatings[x] = [i for i in rawRatings[0] if i]
    rawRatings[x].pop()

for x in range(length):
    if len(rawRatings[x]) > 769:
        rawRatings[x].pop()


print("the number of reviewers for " + movieNames[0] + " are: \n")
print(len(rawRatings[0]))
print("\nthe number of reviewers for " + movieNames[1] + " are: \n ")
print(len(rawRatings[1]))
print("\nthe number of reviewers for " + movieNames[2] + " are: \n ")
print(len(rawRatings[2]))

for x in range(length):
    if len(rawRatings[x]) != 769:
        print("\n" + movieName[x] + " is lenght " + len(rawRatings[x]))
