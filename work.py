
import enum
import math
import os
import re

import sys
#import numpy as np
import array as arr
from collections import deque

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from collections import deque
import statistics
#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#




'''Python program to print DFS traversal for complete graph'''
from collections import defaultdict
 
# this class represents a directed graph using adjacency list representation
 
 
products = ['crackers', 'pretzels','apples']
productPrices = [3.99,3.29,3.68]
productSold = ['crackers','crackers','apples','pretzels']
soldPrice=[3.99,3.98,6.86,3.29]

def checkpriceerros(products, productPrices, productSold, soldPrice):
    res = {}
    masterlist = dict(zip(products,productPrices))
    soldlist = res = dict(zip(productSold,soldPrice))
    counter = 0
    for item in soldlist.items():
        if item not in masterlist.items():
            counter += 1
    return counter


print(checkpriceerros(products, productPrices, productSold, soldPrice))


"""
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())

from timeit import timeit
from functools import reduce

from collections import deque

"""
def bitwiseAnd(N, K):
    # Write your code here
    #result = []
    maximum = 0
    for i in range(1, N):
        #for j in range(i+1,N):
            bitwise_and = i&(i+1)
            print(bitwise_and)
            if maximum < bitwise_and and bitwise_and < K:
                #if bitwise_and > maximum:
                    maximum = bitwise_and
                    #result.append(bitwiseand)
    #result.sort(reverse=True)
    #return max(result)
    return maximum

def countanagrams(words, phrases):
    anagrams = {}
    visitedarray = [False]*len(words)
    for i in range(len(words)):
        count = 1
        for j in range(i+1, len(words)):
            if visitedarray[j] == False:
                if len(words[j]) == len(words[i]):
                    if set(words[j]) == set(words[i]):
                        count += 1
                        visitedarray[j] = True
        if count > 1:
            anagrams[words[i]] = count

    print(anagrams)

    listoflistofphrases = []
    for phrase in phrases:
        lister = phrase.split()
        listoflistofphrases.append(lister)
    
    result = [0]*len(phrases)
    for item, freq in anagrams.items():
        for i in range(len(listoflistofphrases)):
            count = 0
            for word in listoflistofphrases[i]:
                if len(word)  == len(item):
                    if set(word) == set(item):
                        count += 1
            if count > 0:
                combination = freq**count
                result[i] += combination
    
    return result

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
    def addEdge(self, u, v):
        self.graph[u].add(v)
    def bfs_custom(self, start):
        visited = [False]*len(self.graph)
        result = deque()
        for val in range(len(self.graph)):
            result.append(0)
        
        #print(result)
        queue = deque()
        queue.append(start)
        visited[start-1] = True
        
        while queue:
            s = queue.popleft()

            for item in self.graph[s]:
                
                if visited[item-1] == False:
                    if item is not None:
                        result[item-1] = result[s-1] + 6
                    visited[item-1] = True
                    queue.append(item)
        return result
    
        
def bfs(n, m, edges, s):
    # Write your code here
    graph = Graph()
    
    reachablenodes = set()    
    for item in edges:
        reachablenodes.add(item[0])
        reachablenodes.add(item[1])
        graph.addEdge(item[0], item[1]) ####
        graph.addEdge(item[1], item[0]) ####
        
    isolatednodes = set()    
    for i in range(1, n+1):
        if i not in reachablenodes:
            isolatednodes.add(i)
    
    print(isolatednodes)
    for i in isolatednodes:
        graph.addEdge(i, -1)
    #result = deque()
    result = graph.bfs_custom(s)
    for i in isolatednodes:
        result[i-1] = -1
    print(f"result before deleting start is {result}")    
    del result[s-1] #if result was a list, we would have done result.pop(s-1)
    finalresults = []
    for x in result:
        if x == 0:
            finalresults.append(-1)
        else:
            finalresults.append(x)
    finalresults = [x if x != 0 else -1  for x in result]
    return finalresults

        


if __name__ == '__main__':
    #print(countanagrams(['it','good','stew','has','west', 'stil', 'list', 'sewt'], ['stil west has good stew','good stew']))
    #print(countanagrams(['the','bats','tabs','in','cat','act'], ['cat the bats','in the act','act tabs in']))
    result = bfs(10, 6, [[3,1],[10,1],[10,1],[3,1],[1,8],[5,2]], 3)
    print(result)