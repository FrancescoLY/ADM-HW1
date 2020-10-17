# Practice > Python > Introduction > Say "Hello, World!" With Python

if __name__ == '__main__':
    print("Hello, World!")
    
    
# Practice > Python > Introduction > Python If-Else

#!/bin/python

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
    if (n%2==1):
        print("Weird")
    else:
        if (n>=2 and n<=5):
            print("Not Weird")
        elif (n<=20):
            print("Weird")
        else:
            print("Not Weird")
            
            
# Practice > Python > Introduction > Arithmetic Operators

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

    print(a+b)
    print(a-b)
    print(a*b)
    
    
# Practice > Python > Introduction > Python: Division

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(a//b)
print(a/b)


# Practice > Python > Introduction > Loops

if __name__ == '__main__':
    n = int(raw_input())

    for i in range(n):
        print(i*i)
        
        
# Practice > Python > Introduction > Write a function

def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%4==0):
        if (year%100==0 and year%400!=0):
            return leap
        else:
            leap= True
    
    return leap

  
# Practice > Python > Introduction > Print Function

from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print(i, end="")
        
        
# Practice > Python > Basic Data Types > List Comprehensions

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range (z+1) if a+b+c!=n])
    
    
# Practice > Python > Basic Data Types > Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    a = max(arr)
    while(a==max(arr)):
        arr.remove(a)            
    
    #print(arr)
    print(max(arr))
    
    
# Practice > Python > Basic Data Types > Nested Lists

l = []
s = []
n = []

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        s.append(score)
        l.append([name,score])
    
    a=min(s)

    while(a==min(s)):
        s.remove(a)

    c=min(s)

    for b in l:
        if (b[1]==c):
            n.append(b[0])
    
    n.sort()

    for d in n:
        print(d)
        

# Practice > Python > Basic Data Types > Finding the percentage

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    l = student_marks[query_name]
    a=0
    for b in l:
        a+=b
    
    print("{:.2f}".format(a/len(l)))

    
# Practice > Python > Basic Data Types > Lists

if __name__ == '__main__':
    N = int(raw_input())
    a=[]
    for i in range(N):
        l=raw_input().split()
        if (l[0]=="insert"):
            a.insert(int(l[1]),int(l[2]))
        elif (l[0]=="print"):
            print(a)
        elif (l[0]=="append"):
            a.append(int(l[1]))
        elif (l[0]=="remove"):
            a.remove(int(l[1]))
        elif (l[0]=="sort"):
            a.sort()
        elif (l[0]=="pop"):
            a.pop()
        elif (l[0]=="reverse"):
            a.reverse()


# Practice > Python > Basic Data Types > Tuples

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

    def create_tuple(l):
        if (len(l)>1):
            a=create_tuple(l[1:len(l)])
            return (l[0],) + a
        else:
            return (l[0],)

    print(hash(create_tuple(integer_list)))

