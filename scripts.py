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


# Practice > Python > Strings > sWAP cASE

def swap_case(s):
    a=""
    for i in s:
        if i.isupper():
            a+=i.lower()
        else:
            a+=i.upper()
    return a


# Practice > Python > Strings > String Split and Join

def split_and_join(line):
    return "-".join(line.split())


# Practice > Python > Strings > What's Your Name?

def print_full_name(a, b):
    print "Hello "+a+" "+b+"! You just delved into python."
    

# Practice > Python > Strings > Mutations

def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]


# Practice > Python > Strings > Find a string

def count_substring(string, sub_string):
    a=0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)]==sub_string):
            a+=1
    return a


# Practice > Python > Strings > String Validators

if __name__ == '__main__':
    s = raw_input()

    def anyalnum(string):
        for i in string:
            if i.isalnum():
                return True
        return False
    print(anyalnum(s))

    def anyalpha(string):
        for i in string:
            if i.isalpha():
                return True
        return False
    print(anyalpha(s))

    def anydigit(string):
        for i in string:
            if i.isdigit():
                return True
        return False
    print(anydigit(s))

    def anylower(string):
        for i in string:
            if i.islower():
                return True
        return False
    print(anylower(s))

    def anyupper(string):
        for i in string:
            if i.isupper():
                return True
        return False
    print(anyupper(s))


# Practice > Python > Strings > Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# Practice > Python > Strings > Text Wrap

def wrap(string, max_width):
    a = ''
    for i in range(len(string)):
        if (i%max_width==0 and i!=0):
            a+='\n'
            a+=string[i]
        else:
            a+=string[i]
    return a


# Practice > Python > Strings > Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
a='.|.'
b=raw_input().split()
n=int(b[0])
m=int(b[1])

for i in range(1,(n//2)+1):
    s='-'*((m-3*(i*2-1))/2)
    print(s+a*(i*2-1)+s)

s='-'*((m-7)/2)
print(s+'WELCOME'+s)

for i in range((n//2)+2,n+1):
    j=n-i+1
    s='-'*((m-3*(j*2-1))/2)
    print(s+a*(j*2-1)+s)

    
# Practice > Python > Strings > String Formatting

def print_formatted(number):
    # your code goes here

    def binaryy(n):
        a=""
        while (n!=0):
            if (n%2==0):
                a = '0'+a
            else:
                a = '1'+a
            n=n//2
        return a

    def blen(n):
        return len(binaryy(n))

    def octall(n):
        a=""
        while (n!=0):
            if (n%8==0):
                a = '0'+a
            else:
                a = str(n%8)+a
            n=n//8
        return a

    def hexx(n):
        a=""
        while (n!=0):
            if (n%16==0):
                a = '0'+a
            elif (n%16==10):
                a = 'A'+a
            elif (n%16==11):
                a = 'B'+a
            elif (n%16==12):
                a = 'C'+a
            elif (n%16==13):
                a = 'D'+a
            elif (n%16==14):
                a = 'E'+a
            elif (n%16==15):
                a = 'F'+a
            else:
                a = str(n%16)+a
            n=n//16
        return a

    for i in range(1,number+1):
        s=""
        s+=(blen(number)-len(str(i)))*" "+str(i)
        s+=(1+blen(number)-len(octall(i)))*" "+octall(i)
        s+=(1+blen(number)-len(hexx(i)))*" "+hexx(i)
        s+=(1+blen(number)-blen(i))*" "+binaryy(i)
        print(s)

    return 


# Practice > Python > Strings > Alphabet Rangoli

def print_rangoli(size):
    # your code goes here
    
    def build_rangoli(n):
        if n==1:
            return ['a']
        else:
            l=build_rangoli(n-1)
            b=[]
            b.append(chr(n+96))
            for e in l:
                b.append(chr(n+96)+"-"+e+"-"+chr(n+96))
            b.append(chr(n+96))
            return b

    for i in build_rangoli(size):
        c=(size*4-3-len(i))/2
        print("-"*c+i+"-"*c)
    
    return


# Practice > Python > Strings > Capitalize!

# Complete the solve function below.
def solve(s):
    b=''
    if s[0].islower():
        b+=s[0].upper()
    else:
        b+=s[0]
    for i in range(1,len(s)):
        if s[i-1]==' ' and s[i].islower():
            b+=s[i].upper()
        else:
            b+=s[i]
            
    return b


# Practice > Python > Strings > The Minion Game

def minion_game(string):
    # your code goes here

    def kevin(s):
        a=0
        for i in range(len(s)):
            if s[i] in 'AEIOU':
                a+=(len(s)-i)
        return a

    def stuart(s):
        a=0
        for i in range(len(s)):
            if s[i] not in 'AEIOU':
                a+=(len(s)-i)
        return a

    if (kevin(string)==stuart(string)):
        print("Draw")
    elif kevin(string)>stuart(string):
        print("Kevin "+str(kevin(string)))
    else:
        print("Stuart "+str(stuart(string)))
    return


# Practice > Python > Strings > Merge the Tools!

def merge_the_tools(string, k):
    # your code goes here

    def uniquee(s):
        a=""
        for c in s:
            if c not in a:
                a+=c
        return a

    l=[]
    for i in range(len(string)/k):
        l.append(string[i*k:(i+1)*k])
    for e in l:
        print(uniquee(e))
    
    return


# Practice > Python > Sets > Introduction to Sets

def average(array):
    a = set(array)
    return sum(a)/len(a)
    # your code goes here
    
    
# Practice > Python > Sets > No Idea!

# Enter your code here. Read input from STDIN. Print output to STDOUT
c = raw_input()
l = raw_input().split()
a = set(raw_input().split())
b = set(raw_input().split())

h = 0

for e in l:
    if e in a:
        h += 1
    if e in b:
        h -= 1

print(h)


# Practice > Python > Sets > Symmetric Difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = raw_input()
ml = raw_input()
ml2 = ml.split()
ms = set(ml2)
n = raw_input()
nl = raw_input()
nl2 = nl.split()
ns = set(nl2)

r = ms.union(ns).difference(ms.intersection(ns))

rl=[]
for e in r:
    rl.append(e)

rl2=list(map(int, rl))
rl2.sort()

for e in rl2:
    print(e)
    
    
# Practice > Python > Sets > Set .add()

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
s = set()

for i in range(n):
    a = raw_input()
    s.add(a)

print(len(s))


# Practice > Python > Sets > Set .discard(), .remove() & .pop()

n = input()
s = set(map(int, raw_input().split()))

#s = set(map(int,l))
#print(s)
N = int(raw_input())
for i in range(N):
    a = raw_input().split() 
    if len(a)>1:
        b = a[1]
    if a[0]=='pop' and len(s)>0:
        s.pop()
    elif a[0]=='discard':
        #print(int(b))
        s.discard(int(b))
    elif a[0]=='remove' and int(b) in s:
        #print(int(b))
        s.remove(int(b))
    #print(a[0],s)

print(sum(s))


# Practice > Python > Sets > Set .union() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = raw_input()
eng = set(raw_input().split())
f = raw_input()
fre = set(raw_input().split())

print(len(eng | fre))


# Practice > Python > Sets > Set .intersection() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()
eng = set(raw_input().split())
f = raw_input()
fre = set(raw_input().split())

print(len(eng & fre))


# Practice > Python > Sets > Set .difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()
eng = set(raw_input().split())
f = raw_input()
fre = set(raw_input().split())

print(len(eng - fre))


# Practice > Python > Sets > Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = raw_input()
eng = set(raw_input().split())
f = raw_input()
fre = set(raw_input().split())

print(len(eng ^ fre))


# Practice > Python > Sets > Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = raw_input()
l1 = raw_input().split()
s1 = set(map(int,l1))
b = int(raw_input())

for i in range(b):
    c = raw_input()
    com = c.split()[0]
    l2 = raw_input().split()
    s2 = set(map(int,l2))
    if (com=='intersection_update'):
        s1 &= s2
    elif (com=='symmetric_difference_update'):
        s1 ^= s2
    elif (com=='difference_update'):
        s1 -= s2
    elif (com=='update'):
        s1 |= s2

print(sum(s1))


# Practice > Python > Sets > The Captain's Room

# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
k = raw_input()
l = raw_input().split()
s = set(enumerate(map(int,l)))

a = set()
b = set()
for i in s:
    if i[1] in a:
        b |= {i[1]}
    else:
        a |= {i[1]}

print((a-b).pop())
"""

k = raw_input()
l = raw_input().split()

a = set()
b = set()
for i in l:
    if i in a:
        b |= {i}
    else:
        a |= {i}

print((a-b).pop())


# Practice > Python > Sets > Check Subset

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())

for i in range(t):

    sc = set()
    a = int(raw_input())
    la = raw_input().split()
    sa = set(la)
    a = int(raw_input())
    lb = raw_input().split()
    sb = set(lb)
    
    for c in sa:
        if c not in sb:
            sc |= {c}
    
    if len(sc)==0:
        print(True)
    else:
        print(False)
        
        
# Practice > Python > Sets > Check Strict Superset

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = 0
l1 = raw_input().split()
s1 = set(l1)
n = int(raw_input())

for i in range(n):
    l2 = raw_input().split()
    s2 = set(l2)
    for i in s2:
        if i not in s1:
            a+=1
            break
    if len(s2)==len(s1):
        a+=1

if a==0:
    print(True)
else:
    print(False)
