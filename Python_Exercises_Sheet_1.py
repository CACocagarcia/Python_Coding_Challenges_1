"""
Coding Challenges Questions were obtained from Pierian-Data/Complete-Python-3-BootCamp
Challenges solutions and Solutions Explanation paragraph were developed by me
"""

# PROBLEM 1
# Use for, .split(), and if to create a Statement that will print out words that start with 's'

st = 'Print only the words that start with s in this sentence'
st = st.split()
#print(st) #the split method splits a string into a list

for first in st:
    if first[0] == "s":
        print(first)
    else:
        pass
"""
SOLUTION EXPLAINED
- convert the string into a list using the .split() method
- go through each token of the list using a For Loop
- String are arrays of characters in python >> you can grab the index[0] of that word and compare it to the character s
---- if true then print out the word, otherwise you can use the pass function which basically tells the loop that nothing will happen and the program will finish
"""


#PROBLEM 2
#Use range() to print all the even numbers from 0 to 100

x = range(0,100,2)
for n in x:
    if n == 0:
        pass
    else:
        print(n)

"""
SOLUTION EXPLAINED
- Range function behaviour: range(start, end, step)
- pass fucntion in python lets the code running
""" 

#PROBLEM 3
#Use the List Comprehension to create a list of all numbers between one and 50 that are divisible by 3
y = range(1,50)
mylist =  [ m for m in y if m%3 == 0]
print(mylist)
"""
SOLUTION EXPLAINED
- Using the range function to generate a number from 1 to 50
- m is the iterative variable and it's returned if it's true.
- not sure why it behave that it just automatically adds a new number to the list, but that's how it works
"""

#PROBLEM 4
#Go through the string below and if the length of a word is even print "even!"

st2 = 'Print every word in this sentence that has an even number of letters'
st2 = st2.split() #split method splits a string into a list

for word in st2:
    #print(len(word)) #the length of each word is printed

    if len(word)%2 == 0:
        print("even!")
    else:
        print(word)
"""
SOLUTION EXPLAINED
- convert the string into a list using the .split() method
- iterate the list using a For Loop
- Nest inside the For Loop an IF Statment comparing if the length remainder of the list token (length of the word) is 0
"""

#PROBLEM 5
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" ostead of the number
# and for the muples of five print "Buzz". For numbers that are multiples of both three and five print "FizzBuzz"

z = range(1,100)

for zz in z:
    if zz%3 == 0 and zz%5 != 0:
        print("Fizz")
    elif zz%5 == 0 and zz%3 != 0:
        print("Buzz")
    elif zz%3 == 0 and zz%5 == 0:
        print("FizzBuzz")
    else:
        print(zz)
"""
SOLUTION EXPLAINED
- using the range function, generate a set of numbers from 1 to 100
- iterate the set with a For Loop
- Nest an IF Statement with triple conditionals and a default
------ to allow the FizzBuzz to happen, you need to add a reverse comparison and check both mods >> otherwise the first available
------ conditional will execute
"""

#PROBLEM 6
#Use List Comprehension to create a list of the first letters of every word in the string below

st3 = 'Create a list of the first letters of every word in this string'
st3 = st3.split() #split method creates a list of words(strings) that are part of the string
#print(st3) #testing that the list was properly made

output = [] #creating an empty list to be filled with the first letters of each word

for word2 in st3:
    output.append(word2[0]) #Strings in python are arrays of bytes >> each word is an array, we can grab the first token of the array
    #print(output) #verify that each letter per iteration is saved
print(output)
"""
SOLUTION EXPLAINED
-- convert the string into a list using .split() method
-- create an empty list that will save the first letter of each word of the st3 list
-- using a For Loop iterate the st3 list
-- Since strings are arrays in python, and every word in the list is a string you can grab the first letter of the word (the first token of the array)
-- append each token to the output list for a cleaner print
"""

