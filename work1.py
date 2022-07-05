
import math
import os
import random
import re
import sys


#Method that takes an integer and returns an boolean which is true or false
#if its a power of 2 return true, if not return false
from collections import deque



def countoperations(n):
    counter = 0
    length = len(n) - 1
    maxdigit = max(n)
    while n.count(maxdigit) < length:        
        indexofmaxdigit = n.index(maxdigit)
        for i in range(len(n)): 
            if i != indexofmaxdigit:
                n[i] = n[i]+1
        maxdigit = max(n)
        counter += 1

    return counter


#
# Complete the 'degreeOfArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def frequencyarray(arr):
    diction = {}
    for x in arr:
        if x not in diction:
            diction[x] = 1
        else:
            diction[x] += 1
    #degree = max(diction.values())
    return diction

def degreeOfArray(arr):
    # Write your code 
    if arr == []:
        return "Array is empty"
    freqdiction = frequencyarray(arr)
    freqvaluesofdiction = freqdiction.values()
    degree = max(freqvaluesofdiction)
    #create a dictionary with key-value pairs, that have values equal to the degree
    degreedictionary = {}
    for x,y in freqdiction.items():
        if y == degree:
            degreedictionary[x] = y
    
    if len(degreedictionary) == 1: #This means that only one element in the array has a freq == to the degree
        tuplee = list(degreedictionary.items())
        key = tuplee[0][0]
        freq = tuplee[0][1]
        result = []
        index = arr.index(key)        
        while freq > 0:
            result.append(arr[index])            
            if arr[index] == key:
                freq -= 1
            index += 1
        #return len(result)
        return result
    else:
        tuples = list(degreedictionary.items()) #see if a set can work here
        #print(tuples)
        lister = []
        for item in tuples:
            #print(item)
            key = item[0]
            freq = item[1]
            result = []
            index = arr.index(key)
            while freq > 0:
                #print(index)
                result.append(arr[index])            
                if arr[index] == key:
                    freq -= 1
                index += 1
            lister.append(result)
        #print(lister)
        smallest = len(lister[0])
        index = 0
        for i in range(len(lister)):
            if len(lister[i]) < smallest:
                smallest = len(lister[i])
                index = i
        return lister[index]
        #return smallest

print(degreeOfArray([1,2,1,3,2]))
print(degreeOfArray([1,2,2,3,1]))
print(degreeOfArray([4,6,1,6]))
print(degreeOfArray([3,4,5,1,6,3]))