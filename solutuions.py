'''
#Exercise 1: Create a list by picking an odd-index items
#from the first list and even index items from the
#second

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []
for i in range(len(l1)):
    if i % 2 != 0 :
        l3.append(l1[i])
for i in range(len(l2)):
    if i % 2 == 0 :
        l3.append(l2[i])
print(l3)
'''

'''
#Exercise 2: Remove and add item in a list
#Write a program to remove the item present at index 4 and add it to the 2nd
#position and at the end of the list.

list1 = [54, 44, 27, 79, 91, 41]

del list1[4] #Take index 
list1.insert(2 , 91) #Take index , value
list1.insert(6 , 91)
print(list1)
'''

'''
#Exercise 3: Slice list into 3 equal chunks and reverse
#each chunk

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
l1 = list(sample_list[ : 3])
l1 = list(reversed(l1))
print(l1)

l2 = list(sample_list[3:6])
l2 = list(reversed(l2))
print(l2)

l3 = list(sample_list[6 : ])
l3 = list(reversed(l3))
print(l3)

'''



'''
#Exercise 4: Count the occurrence of each element from
#a list

#Write a program to iterate a given list and count the occurrence of each element
#and create a dictionary to show the count of each element.

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
d = {}

for i in sample_list:
    if i not in d :
        d[i] = 1 
    else :
        d[i] += 1 
        
print(d)
'''


'''
#Exercise 5: Create a Python set such that it shows the
#element from both lists in a pair

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

res = set()
for i in range(len(first_list)):
    res.add((first_list[i] , second_list[i]))

print(res)

'''




'''
#Exercise 6: Find the intersection (common) of two sets
#and remove those elements from the first set

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

ans = first_set.intersection(second_set)
print(ans)

for i in ans :
    first_set.remove(i)
    
print(first_set)
'''


'''
#Exercise 7: Checks if one set is a subset or superset of
#another set. If found, delete all elements from that set

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

if (first_set.issubset(second_set)):
    first_set.clear()
    
print(first_set)
print(second_set)
'''

'''
#Exercise 8: Iterate a given list and check if a given
#element exists as a key’s value in a dictionary. If not,
#delete it from the list


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

l = list(sample_dict.values())
print(l)
'''

'''
#Exercise 9: Get all values from the dictionary and add
#them to a list but don’t add duplicates

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
'july': 54, 'Aug': 44, 'Sept': 54}

l = set(speed.values())
print(l)

'''

'''

#Exercise 10: Remove duplicates from a list and create a
#tuple and find the minimum and maximum number


sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
d = {}

for i in sample_list:
    if i not in d :
        d[i] =1 
    else :
        d[i] +=1
        
new_list = []
for i in d :
    if d[i] == 1 :
        new_list.append(i)

print(new_list)

tup = tuple(new_list)
print(tup)

print(max(tup))
print(min(tup))

'''

'''
#Python List Exercise
list1 = [100, 200, 300, 400, 500]

list1 = list(reversed(list1))
print(list1)
'''

'''
#Exercise 2: Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly" , "hazem"]
n = min(len(list1) , len(list2))
ans = []

for i in range(n):
    ans.append(list1[i] + list2[i])

for j in range(i + 1 , len(list1)):
    ans.append(list1[j])
for j in range(i + 1 , len(list2)):
    ans.append(list2[j])
        
print(ans)
'''

'''

#Exercise 3: Turn every item of a list into its square
#Given a list of numbers. write a program to turn every item of a list into its
#square.

numbers = [1, 2, 3, 4, 5, 6, 7]
for i in  range(len(numbers)) :
    numbers[i] = pow(numbers[i] , 2 )
print(numbers)
    
'''


'''
#Exercise 4: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

ans = []
for i in range(len(list1)):
    for j in range(len(list2)):
        ans.append(list1[i] + list2[j])
        
print(ans)

'''
'''

#Exercise 5: Iterate both lists simultaneously
#Given a two Python list. Write a program to iterate both lists simultaneously and
#display items from list1 in original order and items from list2 in reverse order.


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
n = len(list2)
for i in range(len(list1)):
    print(list1[i] , list2[n - i - 1])


'''
'''
#Exercise 6: Remove empty strings from the list of
#strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in list1 :
    if i == "":
        list1.remove(i)
        
print(list1)
'''
'''
#Exercise 7: Add new item to list after a specified item
#Write a program to add item 7000 after 6000 in the following Python List

list1 = [10, 20, 6000 ,  [300, 400, 6000, [5000, 6000], 500], 30, 6000 , 40]

#print(list1[3][3][0])

for i in range(len(list1)):
    if (type(list1[i]) == int):
        if list1[i] == 6000:
            list1.insert(i+1 , 7000) 
    else :
        for j in range(len(list1[i])):
            if (type(list1[i][j]) == int):
                    if list1[i][j] == 6000:
                        list1[i].insert(j+1 , 7000)
            else :
                for k in range(len(list1[i][j])):
                    if list1[i][j][k] == 6000:
                        list1[i][j].insert(k+1 , 7000)


print(list1)
'''


'''

#Exercise 8: Extend nested list by adding the sublist
#You have given a nested list. Write a program to extend it by adding the
#sublist ["h", "i", "j"] in such a way that it will look like the following list.

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]

for i in sub_list:
    list1[2][1][2].append(i)
    
print(list1)

'''





'''
#Exercise 9: Replace list’s item with new value if found
#You have given a Python list. Write a program to find value 20 in the list, and if it
#is present, replace it with 200. Only update the first occurrence of an item.


list1 = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(list1)):
    if list1[i] == 20 :
        list1[i] = 200 
        break 
    
print(list1)
'''


'''
#Exercise 10: Remove all occurrences of a specific item
#from a list.
#Given a Python list, write a program to remove all occurrences of item 20.

list1 = [5, 20, 15, 20, 25, 50, 20]

for i in list1:
    if i == 20 :
        list1.remove(i)
print(list1)

'''


'''
#Python String Exercise

#Exercise 1A: Create a string made of the first, middle
#and last character

str1 = "James"
n = len(str1) // 2 
print(str1[0]+str1[n]+str1[-1])

'''



'''
#Exercise 1B: Create a string made of the middle three
#characters
#Write a program to create a new string made of the middle three characters of an
#input string.


str1 = "JhonDipPeta"
n = len(str1) // 2 
#print(n)
print(str1[n-1] + str1[n] + str1[n+1])

str2 = "JaSonAy"
n = len(str2) // 2 
#print(n)
print(str2[n-1] + str2[n] + str2[n+1])

'''

'''
#Exercise 2: Append new string in the middle of a given
#string

s1 = "Ault"
s2 = "Kelly"

middle = len(s1) // 2 
s3 = ""
for i in range(middle):
    s3 += s1[i]
    
for i in range(len(s2)):
    s3 += s2[i]

for i in range(middle , len(s1)):
    s3 += s1[i]
    
print(s3)

'''

'''
#Exercise 3: Create a new string made of the first,
#middle, and last characters of each input string
#Given two strings, s1 and s2, write a program to return a new string made of s1
#and s2’s first, middle, and last characters.


s1 = "America"
s2 = "Japan"

s3 = ""

middle1 = len(s1) // 2 
middle2 = len(s2) // 2 

s3 = s1[0] + s2[0] + s1[middle1]+s2[middle2] + s1[-1] + s2[-1]
print(s3)
'''

'''
#Exercise 4: Arrange string characters such that
#lowercase letters should come first

#Given string contains a combination of the lower and upper case letters. Write a
#program to arrange the characters of a string so that all lowercase letters should
#come first.

str1 = "PyNaTive"
ans1 = ""
ans2 = ""
res = ""
for i in range(len(str1)):
    if str1[i].islower():
        ans1 += str1[i]
    else :
        ans2 += str1[i]
        
res = ans1 + ans2 
print(res)
'''






'''
#Exercise 5: Count all letters, digits, and special symbols
#from a given string

str1 = "P@#yn26at^&i5ve"

d = 0 
c = 0 
for i in range(len(str1)):
    if str1[i].isalpha():
        c += 1 
    if str1[i].isdigit():
        d +=1
    
print('chars: ' , c)
print('digits: ' , d)
print('symbol: ' , len(str1) - (c + d))

'''

'''
#Exercise 6: Create a mixed String using the following
#rules

#Given two strings, s1 and s2. Write a program to create a new string s3 made of
#the first char of s1, then the last char of s2, Next, the second char of s1 and
#second last char of s2, and so on. Any leftover chars go at the end of the result.

s1 = "Abc"
s2 = "XyzhG"
s3 = ""
n = min(len(s1) , len(s2))

for i in range(n):
    s3 += s1[i]
    s3 += s2[len(s2) - i - 1]
    
for i in range(n , len(s1)):
    s3 += s1[i]

for i in range(len(s2) - n ):
    s3 += s2[i]

print(s3)

'''


'''
#Exercise 7: String characters balance Test
#Write a program to check if two strings are balanced. For example, strings s1 and
#s2 are balanced if all the characters in the s1 are present in s2. The character’s
#position doesn’t matter.


#s1 = "Yn"
#s2 = "PYnative"
s1 = "Ynf"
s2 = "PYnative"
d = {}

for i in range(len(s2)):
    if s2[i] not in d :
        d[s2[i]] = 1
    else :
        d[s2[i]] +=1 
        
ok = True 
for i in range(len(s1)):
    k = d.get(s1[i] , 0)
    if k == 0 :
        ok = False 
        break
    
print(ok)
'''

'''
#Exercise 8: Find all occurrences of a substring in a
#given string by ignoring the case
#Write a program to find all occurrences of “USA” in a given string ignoring the
#case.

str1 = "Welcome to USA. usa awesome, isn't it?"
count = 0 
for i in str1.split():
    x = list(i)
    s = ""
    for j in x :
        if j.isalpha():
            s += j 
    if s.lower() == 'usa':
        count += 1 
        
print(count)

'''


'''
#Exercise 9: Calculate the sum and average of the digits
#present in a string

#Given a string s1, write a program to return the sum and average of the digits
#that appear in the string, ignoring all other characters.

str1 = "PYnative29@#8496"
sm = 0 
count = 0 
for i in str1 :
    if i.isdigit():
        sm += int(i)
        count += 1 
        
print(f"sum of digits: {sm}")
print(f"average of digits: {sm / count}")

'''

'''
#Exercise 10: Write a program to count occurrences of
#all characters within a string

str1 = "Apple"
d = {}
for i in str1 :
    d[i] = d.get(i , 0) + 1 
    
print(d)
'''

'''
#Exercise 11: Reverse a given string

str1 = "PYnative"
str1 = str1[::-1]
print(str1)

'''
'''

#Exercise 12: Find the last position of a given substring
#Write a program to find the last position of a substring “Emma” in a given string.

str1 = "Emma is a data scientist who knows Python. Emma works at google."

ans = 0 

for i in range(len(str1) - 3):
    x = str1[i] +  str1[i+1] + str1[i+2] + str1[i+3].replace(" " , "")
    if x == "Emma":
        ans = max(ans , i)
print(ans)

'''


'''
#Exercise 13: Split a string on hyphens
#Write a program to split a given string on hyphens and display each substring.

str1 = "Emma-is-a-data-scientist"
str1 = str1.split("-")
for i in str1:
    print(i)

'''



'''
#Exercise 14: Remove empty strings from a list of
#strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

for i in str_list:
    if i == None or i == "":
        str_list.remove(i)
        
print(str_list)
'''

'''
#Exercise 15: Remove special symbols / punctuation
#from a string

str1 = "/*Jon is @developer & musician"

for i in str1:
    if i.isalpha() or i.isdigit():
        continue 
    else :
        str1 = str1.replace(i , " ")
        
print(str1.strip())
print()

str1 = "/*Jon is @developer & musician"

for i in str1.split():
    if len(i) == 1 :
        if i.isalpha() or i.isdigit():
            continue 
        else :
            str1 = str1.replace(i , " ")
            
    else :
        for j in i :
            if j.isalpha() or j.isdigit():
                continue 
            else :
                str1 = str1.replace(j , "")

print(str1)        
'''



'''
#Exercise 16: Removal all characters from a string
#except integers

str1 = 'I am 25 years and 10 months old'

for i in str1 :
    if i.isdigit():
        print(i , end = '')
'''


'''

#Exercise 17: Find words with both alphabets and
#numbers

#Write a program to find words with both alphabets and numbers from an input
#string.

str1 = "Emma25 is Data scientist50 and AI Expert"

for i in str1.split():
    ok1 = False
    ok2 = False  
    for j in i :
        if j.isalpha():
            ok1 = True
        if j.isdigit():
            ok2 = True
            
    if(ok1 and ok2 ):
        print(i)
'''


'''
#Exercise 18: Replace each special symbol with # in the
#following string

str1 = '/*Jon is @developer & musician!!'

for i in str1 :
    if i != " " and i.isdigit() == False and i.isalpha() == False:
        str1 = str1.replace(i , '#')
        
print(str1)

'''




'''
#Python Tuple Exercise
#Exercise 1: Reverse the tuple

tuple1 = (10, 20, 30, 40, 50)

tuple1 = tuple(reversed(tuple1))
print(tuple1)

'''


'''
#Exercise 2: Access value 20 from the tuple
#The given tuple is a nested tuple. write a Python program to print the value 20.

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

for i in range(len(tuple1)):
    y = tuple1[i]
    for j in y :
        if str(j) == '20':
            print(j)
            
'''

'''
#Exercise 4: Unpack the tuple into 4 variables
#Write a program to unpack the following tuple into four variables and display each variable.

tuple1 = (10, 20, 30, 40)

a , b , c , d =  tuple1
print(a)
print(b)
print(c)
print(d)
'''

''''
#Exercise 5: Swap two tuples in Python

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1 , tuple2 = tuple2 , tuple1
print(tuple1 , tuple2)

'''



'''
#Exercise 6: Copy specific elements from one tuple to a
#new tuple
#Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

tuple1 = (11, 22, 33, 44, 55, 66)

l = []
for i in tuple1:
    if i == 44 or i == 55 :
        l.append(i)
        
new_tuple = tuple(l)
print(new_tuple)
'''



'''
#Exercise 7: Modify the tuple
#Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following
#tuple to 222

tuple1 = (11, [22, 33], 44, 55)

l = list(tuple1)
ok = False 
for i in range(len(l)):
    if ok :
        break
    else :
        if type(l[i]) == int :
            if l[i] == 22 :
                l[i] = 222
                ok = True
                break
        else :
            for j in range(len(l[i])):
                if l[i][j] == 22 :
                    l[i][j] = 222
                    ok = True
                    break
                
print(l)

'''

'''
#Exercise 8: Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
l = list(tuple1)

l.sort(key= lambda x : x[1])
print(tuple(l))
'''

'''
#Exercise 9: Counts the number of occurrences of item
#50 from a tuple

tuple1 = (50, 10, 60, 70, 50)
count = 0 
for i in tuple1:
    if i == 50 :
        count +=1
        
print(count)

'''

'''
#Exercise 10: Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 45)

if len(set(tuple1)) ==1 :
    print(True)
else :
    print(False)

'''

#Python Set Exercise
#Exercise 1: Add a list of elements to a set
'''
#Given a Python list, Write a program to add all its elements into a given set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

for i in sample_list:
    sample_set.add(i)
print(sample_set)

'''


'''
#Exercise 2: Return a new set of identical items from two
#sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

new_set = set()
new_set = set1.intersection(set2)
print(new_set)
'''


'''
#Exercise 3: Get Only unique items from two sets
#Write a Python program to return a new set with unique items from both sets by
#removing duplicates

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

new_set = set1
for i in set2 :
    new_set.add(i)
print(new_set)

'''



'''
#Exercise 4: Update the first set with items that don’t exist in
#the second set

#Given two Python sets, write a Python program to update the first set with items
#that exist only in the first set and not in the second set.

set1 = {10, 20, 30}
set2 = {20, 40, 50}

new_set = set1.difference(set2)
print(new_set)
'''

'''
#Exercise 5: Remove items from the set at once
#Write a Python program to remove items 10, 20, 30 from the following set at once.

set1 = {10, 20, 30, 40, 50}
res = set()
for i in set1 :
    if i == 20 or i == 10 or i == 30 :
        continue 
    else :
        res.add(i)
print(res)

#Sol_2
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10,20,30})
print(set1)

'''


'''
#Exercise 6: Return a set of elements present in Set A or B,
#but not both

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

a = set1.difference(set2)
b = set2.difference(set1)
for i in b :
    a.add(i)
print(a)
'''


'''
#Exercise 7: Check if two sets have any elements in common.
#If yes, display the common elements

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

a = set1.intersection(set2)
if len(a) > 0 :
    print(a)
'''

'''
#Exercise 8: Update set1 by adding items from set2, except
#common items

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
a = set1.intersection(set2)

for i in set2:
    if i not in a :
        set1.add(i)
        
set1.difference_update(a)
print(set1)
 
'''

'''
#Exercise 9: Remove items from set1 that are not common to
#both set1 and set2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

a = set1.difference(set2)
set1.difference_update(a)
print(set1)
'''


'''
#Exercise 1: Convert two lists into a dictionary

#Below are the two lists. Write a Python program to convert them into a dictionary
#in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)
'''




'''
#Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

for i , j in dict2.items():
    dict1[i] = j 
    
print(dict1)

'''

'''
#Exercise 3: Print the value of key ‘history’ from the
#below dict

sampleDict = {
 "class": {
 "student": {
 "name": "Mike",
 "marks": {
 "physics": 70,
 "history": 80
  }
  }
 }
}


print(sampleDict["class"]["student"]["marks"]["history"])

'''

'''
#Exercise 4: Initialize dictionary with default values

#In Python, we can initialize the keys with the same values.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
d = {}
for i in employees:
    d[i] = defaults
print(d)
'''

'''
#Exercise 5: Create a dictionary by extracting the keys
#from a given dictionary

#Write a Python program to create a new dictionary by extracting the mentioned
#keys from the below dictionary

sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

d = {}
for i in keys:
    d[i] = sample_dict[i]
print(d)

'''

'''
#Exercise 6: Delete a list of keys from a dictionary

sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]

for i in keys:
    del sample_dict[i]
    
print(sample_dict)
'''

'''
#Exercise 7: Check if a value exists in a dictionary
#We know how to check if the key exists in a dictionary. Sometimes it is required
#to check if the given value is present.
#Write a Python program to check if value 200 exists in the following dictionary

ok = False 
sample_dict = {'a': 100, 'b': 200, 'c': 300}
for i , j in sample_dict.items():
    if j == 200 :
        ok = True 
        break
if ok :
    print("200 is present in dict")
else :
    print("No")

#Sol_2
print(200 in sample_dict.values())

'''

'''
#Exercise 8: Rename key of a dictionary
#Write a program to rename a key city to a location in the following dictionary.

sample_dict = {
 "name": "Kelly",
 "age":25,
 "salary": 8000,
 "city": "New york"
}

x = sample_dict["city"]
del sample_dict["city"]
sample_dict["location"] = x 
print(sample_dict)

'''

'''
#Exercise 9: Get the key of a minimum value from the
#following dictionary

sample_dict = {
 'Physics': 82,
 'Math': 65,
 'history': 75
}
mn = 1000
res = ""
for i in sample_dict:
    if sample_dict[i] < mn :
        res = i
        mn = sample_dict[i]
print(res)
'''
    
'''
#Exercise 10: Change value of a key in a nested
#dictionary

#Write a Python program to change Brad’s salary to 8500 in the following
#dictionary.

sample_dict = {
 'emp1': {'name': 'Jhon', 'salary': 7500},
 'emp2': {'name': 'Emma', 'salary': 8000},
 'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']["salary"] = 8500
#print(sample_dict)

for i in sample_dict:
    print(sample_dict[i])

'''











