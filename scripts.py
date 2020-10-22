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


# Practice > Python > Collections > collections.Counter()

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

a = raw_input()
b = Counter(map(int,raw_input().split()))
c = int(raw_input())
e = 0

for i in range(c):
    d = map(int,raw_input().split())
    if (b[d[0]]>0):
        e += d[1]
        b[d[0]]-=1

print(e)


# Practice > Python > Collections > DefaultDict Tutorial

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

a = map(int,raw_input().split())
d = defaultdict(list)

for i in range(1,a[0]+1):
    b = raw_input()
    d[b].append(str(i))

for j in range(a[1]):
    c = raw_input()
    if d[c]==[]:
        print('-1')
    else:
        e=''
        for i in d[c]:
            e+=i
            e+=' '
        print(e)
        
        
# Practice > Python > Collections > Collections.namedtuple()

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple
n = int(input())
Student = namedtuple('Student',input())
t = 0
for i in range(n):
    l = input().split()
    s1 = Student(l[0],l[1],l[2],l[3])
    t += int(s1.MARKS)

#print("{:.2f}".format(t/n))
print(round(t/n,2))


# Practice > Python > Collections > Collections.OrderedDict()

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict
a = OrderedDict()
n = int(raw_input())

for i in range(n):
    b = raw_input().split()
    pname = b[0]
    for j in range(1,len(b)-1):
        pname += ' '
        pname += b[j]
    if pname in a:
        a[pname]+=int(b[len(b)-1])
    else:
        a[pname]=int(b[len(b)-1])

for i in a:
    print(i+' '+str(a[i]))
    
    
# Practice > Python > Collections > Word Order

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

a = OrderedDict()
n = int(raw_input())

for i in range(n):
    b = raw_input()
    if b in a:
        a[b]+=1
    else:
        a[b]=1

print(len(a.keys()))

c = ''
for i in a:
    c+=' '
    c+=str(a[i])

print(c[1:])


# Practice > Python > Collections > Collections.deque()

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

d = deque()
n = int(raw_input())

for i in range(n):
    a = raw_input().split()
    if a[0]=='pop':
        d.pop()
    elif a[0]=='popleft':
        d.popleft()
    elif a[0]=='append':
        d.append(a[1])
    elif a[0]=='appendleft':
        d.appendleft(a[1])

c = ''
for i in d:
    c+=' '
    c+=i

print(c[1:])


# Practice > Python > Collections > Company Logo

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
from collections import OrderedDict

s = raw_input()
c = Counter(s)
d = OrderedDict()

def leastt(l):
    a=l[0]
    for b in l[1:]:
        if b<a:
            a=b
    return a

for i in c:
    if c[i] in d:
        d[c[i]].append(i)
    else:
        d[c[i]] = [i]

k = d.keys()
k.sort()
a = 3
b = 1

#print(d)

while a > 0:
    j = len(k)-b
    if len(d[k[j]])==1:
        print(d[k[j]][0]+' '+str(k[j]))
        a-=1
        b+=1
    else:
        print(leastt(d[k[j]])+' '+str(k[j]))
        d[k[j]].remove(leastt(d[k[j]]))
        a-=1
        
        
# Practice > Python > Collections > Piling Up!

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

n = int(raw_input())

for i in range(n):
    a=raw_input()
    d=deque(map(int,raw_input().split()))
    l=[]
    f = 0
    while len(d)!=0:
        if len(l)==0:
            if d[0]>d[len(d)-1]:
                l.append(d.popleft())
            else:
                l.append(d.pop())
        else:
            if max(d[0],d[len(d)-1])>l[len(l)-1]:
                f = 1
                break
            else:
                if d[0]>d[len(d)-1]:
                    l.append(d.popleft())
                else:
                    l.append(d.pop())
    if f==1:
        print('No')
    else:
        print('Yes')

        
# Practice > Python > Date and Time > Calendar Module

# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

l=map(int,raw_input().split())
n = calendar.weekday(l[2], l[0], l[1])

if (n==0):
    print('MONDAY')
elif (n==1):
    print('TUESDAY')
elif (n==2):
    print('WEDNESDAY')
elif (n==3):
    print('THURSDAY')
elif (n==4):
    print('FRIDAY')
elif (n==5):
    print('SATURDAY')
elif (n==6):
    print('SUNDAY')

    
# Practice > Python > Date and Time > Time Delta

# Enter your code here. Read input from STDIN. Print output to STDOUT

import datetime
n = int(raw_input())

def monnum(s):
    if (s=='Jan'):
        return 1
    elif (s=='Feb'):
        return 2
    elif (s=='Mar'):
        return 3
    elif (s=='Apr'):
        return 4
    elif (s=='May'):
        return 5
    elif (s=='Jun'):
        return 6
    elif (s=='Jul'):
        return 7
    elif (s=='Aug'):
        return 8
    elif (s=='Sep'):
        return 9
    elif (s=='Oct'):
        return 10
    elif (s=='Nov'):
        return 11
    elif (s=='Dec'):
        return 12

for i in range(n):
    l1=raw_input().split()
    c1=[l1[1], monnum(l1[2]), l1[3]]
    c1.extend(l1[4].split(':'))
    d1 = map(int,c1)
    l2=raw_input().split()
    c2=[l2[1], monnum(l2[2]), l2[3]]
    c2.extend(l2[4].split(':'))
    d2 = map(int,c2)
    a=datetime.datetime(d1[2],d1[1],d1[0],d1[3],d1[4],d1[5])
    b=datetime.datetime(d2[2],d2[1],d2[0],d2[3],d2[4],d2[5])
    t1=a-b
    t2=0
    if l1[5][0]=='-':
        t2+=int(l1[5][1:3])*3600
        t2+=int(l1[5][3:5])*60
    elif l1[5][0]=='+':
        t2-=int(l1[5][1:3])*3600
        t2-=int(l1[5][3:5])*60
    if l2[5][0]=='-':
        t2-=int(l2[5][1:3])*3600
        t2-=int(l2[5][3:5])*60
    elif l2[5][0]=='+':
        t2+=int(l2[5][1:3])*3600
        t2+=int(l2[5][3:5])*60
    print(abs(t1.days*86400+t1.seconds+t2))
    
    
# Practice > Python > Errors and Exceptions > Exceptions

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

for i in range(n):
    s = raw_input().split()
    try:
        a = int(s[0])
        b = int(s[1])
    except ValueError as e:
        print "Error Code:", e
        continue
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print "Error Code:",e
        
        
# Practice > Python > Built-Ins > ginortS

# Enter your code here. Read input from STDIN. Print output to STDOUT

s = raw_input()

ll = []
for i in s:
    if i.islower():
        ll.append(i)
ll.sort()
lls=''
for i in ll:
    lls+=i

ul = []
for i in s:
    if i.isupper():
        ul.append(i)
ul.sort()
uls=''
for i in ul:
    uls+=i

od = []
for i in s:
    if i.isdigit() and int(i)%2==1:
        od.append(i)
od.sort()
ods=''
for i in od:
    ods+=i

ed = []
for i in s:
    if i.isdigit() and int(i)%2==0:
        ed.append(i)
ed.sort()
eds=''
for i in ed:
    eds+=i

print(lls+uls+ods+eds)


# Practice > Python > Built-Ins > Athlete Sort

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

a = map(int,raw_input().split())
l=[]
d=OrderedDict()

for i in range(a[0]):
    c=raw_input().split()
    l.append(c)

k = int(raw_input())

for i in l:
    if i[k] not in d:
        d[i[k]]=[i]
    else:
        d[i[k]].append(i)

b = map(int,d.keys())
b.sort()

#print(b)

for i in b:
    for j in d[str(i)]:
        s = ''
        for m in j:
            s+=' '
            s+=m
        print(s[1:])
        
        
# Practice > Python > Built-Ins > Zipped!

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = raw_input().split()
n = int(a[1])
l = []

for i in range(n):
    l.append(raw_input().split())

b = zip(*l)
#print(b)

for e in b:
    c = 0.0
    for i in range(n):
        c+=float(e[i])
    print(round(c/n,1))
    
    
# Practice > Python > Python Functionals > Map and Lambda Function

cube = lambda x:x*x*x # complete the lambda function 

def fibonacci(n):
    if n==0:
        return []
    if n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        f = fibonacci(n-1)
        #print(f)
        f.append(f[len(f)-1]+f[len(f)-2])
        return f
    # return a list of fibonacci numbers
    
    
# Practice > Python > Regex and Parsing > Detect Floating Point Number

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(raw_input())

for i in range(n):
    f=0
    s = raw_input()
    if bool(re.match(r"[+-]?[0-9]*[.][0-9]+",s))==False:
        f=1
    else:
        if bool(re.match(r"[+-]?[0-9]*[.][0-9]+[.]",s))==True:
            f=1
        else:
            try:
                float(s)
            except:
                f=1
    if (f==0):
        print(True)
    else:
        print(False)
        
        
# Practice > Python > Regex and Parsing > Re.split()

#regex_pattern = r"[[0-9]+[.,]]*[0-9]+"	# Do not delete 'r'.
regex_pattern = r"[.,]"


# Practice > Python > Regex and Parsing > Group(), Groups() & Groupdict()

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
s = raw_input()
c = ''

for i in s:
    if (i.isalnum()):
        if bool(re.search(i*2,s))==True:
            c=i
            break
            #print('ok')

#print(c)

if (c==''):
    print(-1)
else:
    print(c)
    
    
# Practice > Python > Regex and Parsing > Re.findall() & Re.finditer()

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
s = raw_input()

#b = r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou]+[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([AEIOUaeiou]+[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])*'

a = re.finditer(r'[AEIOUaeiou]{2,}',s)
#print(a)

s2=' '+s+' '
r= 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'

f=0
for e in a:
    i=e.start()+1
    j=e.end()+1
    #print(i,j)
    if s2[i-1] in r and s2[j] in r:
        f=1
        print(s2[i:j])

if (f==0):
    print(-1)
    
    
# Practice > Python > Regex and Parsing > Re.start() & Re.end()

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
s = raw_input()
k = raw_input()
f=0
i=0

while len(s)>=len(k):
    c = re.search(k,s)
    if bool(c)==True:
        b = c.start()
        print((b+i,c.end()+i-1))
        s=s[b+1:]
        f=1
        i+=b+1
    else:
        break

if (f==0):
    print((-1,-1))
    
    
# Practice > Python > Regex and Parsing > Regex Substitution
    
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(raw_input())
def func(match):
    if s[match.start()-1]==' ' and s[match.end()]==' ':
        if (match.group())=='&&':
            return 'and'
        else:
            return 'or'
    else:
        return match.group()


for i in range(n):
    s=raw_input()
    print re.sub(r'(&&)|(\|\|)', func, s)
    
    
# Practice > Python > Regex and Parsing > Validating Roman Numerals

m='(M{1,3})'
a='(CM|(D(C){1,3})|((C){1,3}(D)?))'
b='(XC|(L(X){1,3})|((X){1,3}(L)?))'
c='(IX|(V(I){1,3})|((I){1,3}(V)?))'

r1='('+m+'?'+a+'?'+b+'?'+c+')'
r2='('+m+'?'+a+'?'+b+c+'?'+')'
r3='('+m+'?'+a+b+'?'+c+'?'+')'
r4='('+m+a+'?'+b+'?'+c+'?'+')'

regex_pattern = r""+'('+r1+'|'+r2+'|'+r3+'|'+r4+')'+'\Z'    # Do not delete 'r'.

'''
m='(M{1,3})'
a='(D{0,1}C{1,4})'
b='(L{0,1}X{1,4})'
c='(V{0,1}I{1,4})'

r1='('+m+'?'+a+'?'+b+'?'+c+')'
r2='('+m+'?'+a+'?'+b+c+'?'+')'
r3='('+m+'?'+a+b+'?'+c+'?'+')'
r4='('+m+a+'?'+b+'?'+c+'?'+')'
regex_pattern = r""+r1+'|'+r2+'|'+r3+'|'+r4    # Do not delete 'r'.
'''


# Practice > Python > Regex and Parsing > Validating phone numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(raw_input())

for i in range(n):
    s = raw_input()
    if bool(re.match(r'[789][0-9]{9}\Z',s))==True:
        print('YES')
    else:
        print('NO')
        
        
# Practice > Python > Regex and Parsing > Validating and Parsing Email Addresses

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import email.utils

n = int(raw_input())
for i in range(n):
    s = raw_input()
    e = email.utils.parseaddr(s)
    if bool(re.match(r'[a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}\Z',e[1]))==True:
        print(email.utils.formataddr(e))
        
        
# Practice > Python > Regex and Parsing > Hex Color Code

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(raw_input())
f=0
for i in range(n):
    s = raw_input()
    if ('}' in s):
        f=0
    if f==1:
        a = re.finditer(r'(#[a-fA-F0-9]{6})|(#[a-fA-F0-9]{3})',s)
        for e in a:
            print(e.group())
    if ('{' in s):
        f=1
        
        
# Practice > Python > Regex and Parsing > HTML Parser - Part 1

# Enter your code here. Read input from STDIN. Print output to STDOUT

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for e in attrs:
            print '-> ' + e[0] + ' > ' + str(e[1])
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for e in attrs:
            print '-> ' + e[0] + ' > ' + str(e[1])

parser = MyHTMLParser()

n = int(raw_input())

for i in range(n):
    s = raw_input()
    parser.feed(s)
    
    
# Practice > Python > Regex and Parsing > HTML Parser - Part 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        a = data.split('\n')
        if len(a)>1:
            print('>>> Multi-line Comment')
            for e in data.split('\n'):
                print(e)
        else:
            print('>>> Single-line Comment')
            print(data)
    def handle_data(self, data):
        a = data.split('\n')
        if (a!=['','']):
            print('>>> Data')
            for e in a:
                print(e)

parser = MyHTMLParser()

n = int(raw_input())

for i in range(n):
    s = raw_input()
    parser.feed(s+'\n')
    
    
# Practice > Python > Regex and Parsing > Detect HTML Tags, Attributes and Attribute Values

# Enter your code here. Read input from STDIN. Print output to STDOUT

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for e in attrs:
            print '-> ' + e[0] + ' > ' + str(e[1])
    def handle_startendtag(self, tag, attrs):
        print tag
        for e in attrs:
            print '-> ' + e[0] + ' > ' + str(e[1])

parser = MyHTMLParser()

n = int(raw_input())

for i in range(n):
    s = raw_input()
    parser.feed(s)
    
    
# Practice > Python > Regex and Parsing > Validating UID 

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(raw_input())

for i in range(n):
    s = raw_input()
    if (bool(re.match(r'[a-zA-Z0-9]{10}',s))==False):
        print('Invalid')
        #print(1)
        continue
    if len(re.findall(r'[A-Z]',s))<2:
        print('Invalid')
        #print(2)
        continue
    if len(re.findall(r'[0-9]',s))<3:
        print('Invalid')
        continue
    f = 0
    for c in s:
        if len(re.findall(c,s))>1:
            f = 1
            break;
    if (f==1):
        print('Invalid')
        continue
    print('Valid')
    
    
# Practice > Python > Regex and Parsing > Validating Credit Card Numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(raw_input())

for i in range(n):
    s = raw_input()
    if bool(re.match(r'([456][0-9]{15}\Z)|([456][0-9]{3}(-[0-9]{4}){3}\Z)',s))==False :
        print('Invalid')
        continue
    l = s.split('-')
    s2=''
    a = '(0000)|(1111)|(2222)|(3333)|(4444)|'
    b = '(5555)|(6666)|(7777)|(8888)|(9999)'
    for e in l:
        s2+=e
    if bool(re.search(r''+a+b,s2))==True :
        print('Invalid')
        continue
    print('Valid')
    
    
# Practice > Python > Regex and Parsing > Matrix Script

#!/bin/python

import math
import os
import random
import re
import sys




first_multiple_input = raw_input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in xrange(n):
    matrix_item = raw_input()
    matrix.append(matrix_item)

#print(matrix)

s = ''
for i in range(m):
    for j in matrix:
        s+=j[i]

#print(s)

c = len(s)

a=0
while a<c and s[a]in'!@#$%& ':
    a+=1

b=c
#b=max(c-1,a)
#while b>0 and s[b]in'!@#$%& ':
while b-1>=a and s[b-1]in'!@#$%& ':
    b-=1

s1=s[0:a]
s3=s[b:c]
s2=s[a:b]

s4=''
l = re.findall(r'[a-zA-Z0-9]+',s2)
for i in l:
    s4+=i
    s4+=' '

print(s1+s4[0:(len(s4)-1)]+s3)


# Practice > Python > XML > XML 1 - Find the Score

def get_attr_number(node):
    a=len(node.attrib)
    for child in node:
        if len(child)==0:
            a+=len(child.attrib)
        else:
            a+=get_attr_number(child)
    return a
    # your code goes here


# Practice > Python > XML > XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if len(elem)==0:
        maxdepth = max(maxdepth,level+1)
    else:
        for child in elem:
            depth(child, level+1)

    # your code goes here

    
# Practice > Python > Closures and Decorators > Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        l2=[]
        for i in l:
            l2.append(int(i[(len(i)-10):]))
        l2.sort()
        for i in l2:
            print('+91 '+str(i)[0:5]+' '+str(i)[5:10])
        # complete the function
    return fun


# Practice > Python > Closures and Decorators > Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        d = []
        #print(people)
        for i in people:
            d.append(int(i[2]))
        d.sort()
        #print(d)
        b=[]
        while len(d)>0:
            a=min(d)
            for i in people:
                if int(i[2])==a:
                    if i[3]=='M':
                        b.append('Mr. '+i[0]+' '+i[1])
                    elif i[3]=='F':
                        b.append('Ms. '+i[0]+' '+i[1])
                    #b.append(str(i))
                    d.remove(a)
                    people.remove(i)
                    break
        return b
        # complete the function
    return inner
