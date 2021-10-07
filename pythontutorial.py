'''a="codegnan"
print(a[::1])
# print(a[::2])
print(a[1:5:2])
print(a[1:5:3])
print(a[::3])
print(a[::-1])
print(a[::-2])
print(a[1:5:-1])'''#not possible -ve and positive
#string.functions()
'''a="codegnan"
#contenttext function
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())
print(a.islower())
print(a.isupper())
print(a.startswith('c'))
print(a.endswith('n'))'''
#conversions
'''a="codegnan"
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.isalnum())'''
'''
a='          coDEGnan'
print(a.swapcase())
print(a.index('G'))
print(a.count('n'))
#print(a.index('z'))#not fount:value error
print(a.find('n'))
print(a.index('n'))

print(a)
print(a.strip())
print(a.lstrip())'''
'''a="          codegnan           "
print(a)
#print(a.strip())
print(a.lstrip())
print(a.rstrip())
print(a.replace('n','25'))
print(a)#ans:codegnan only original string not change
a="codegnan"
print(len(a))
print(max(a))#max ascii value of alphabet in str
print(min(a))#it gives minimum alphabet
#combine strings concatenation
''''''c="codegnan"
print(c+2)# type error
print(c*2)'''# type error
'''b='saketh'*2#sakethsaketh
print(b)
print('-'*50)# -----............
print('-'**10)#not supported'''
'''print(max('murali'))
print(min('murali'))
#container
a=[1,4,0,2,5,-1]
print(a)
print(len(a))
#indexing
print(a[5])
#print(a[7])#index error
print(a[4])
b=[1,4,0,2,[1,3,4,5],5,[1,2,3,4,5],-1]
print(b[4][3])
#strings have indexing
print(a[1:8])
c="murali"
print(c[::-1])
#lists are mutable'''
'''a=[1,5,0,[1,4,5,2,6],0,5,6]
a[3][2]='tajhotel'
print(a)
b=[1,2,3,[3,4,5,6],"code",3]
b[4]='p'
print(b)
b[4][2]='p'
print(b)'''#string does not support item assignment
'''a=[1,5,0,[1,4,5,2,6],0,5,6]
print(a.append(26))
print(a)
a.extend('78')
print(a)
a.extend([1,2,3])
print(a)'''
'''a=[1,5,0,[1,4,5,2,6],0,5,6]
a.insert(a[3][3],'p')
print(a)'''
'''a=[1,5,0,[1,4,5]]
b=[1,2,3,4]
#a.append(b)
print(a)
b.extend(a)
print(b)
print(len(b))'''
'''a=[1,4,5,6,[5,7,8,9]]
b=[5,7,8,9]
b.extend(a)
print(b)
print(len(b))
s=[1,4,5,6,7,9,10]
#s.remove(8)#value error
print(s)
s.pop(3)# it takes index position also
s.pop()
print(s)
s.pop(1)
print(s)'''
'''s=[1,4,5,6,7,9,10]
s.clear()
print(s)# empty list
del s
print(s)'''#name error: so  s is not defined
'''s=[8,4,76,6,17,9]
e=s.copy()
print(e)
print(e.index(9))
print(e.index(17))
e.sort()
print(e)
#print(e.sort())# none it will not store any value
e.reverse()
print(e)#none
print(e[::-1])
e.sort(reverse=True) # sort will have reverse=False by default
print(e)'''
'''d=['p','e','q','a']
d.sort()
print(d)
d.sort(reverse=True)
print(d'''
#merging of two lists
'''c=[1,2,4]
d=c+[5,6]
print(d)
e=c+4 # not possible
print(e)'''
'''c=[1,4,5,6,7]
d=c[1]+25
print(d)'''
#tuples
'''a='saketh'
a='saketh','codegnan'
print(type(a))
a=(10,12,3,4,7,23)
print(type(a))
a[-1]=7 #tuples does not support item assignment
print(a)''' '''
a=(1,3,4,[3,4,5])
a[3][1]="murali" #lists inside the tules can be modify the data
print(a)'''
'''a=(1,5,5,7,4,8,['police',5,8,6])
#a.index(6) #Value Error: tuple.index(x): x not in tuple
print(a.count(5))
print(a.index(4))
a.clear(6)# attribute error no clear() for tuple
print(a)'''
'''a=(1,4,5,6)
b=(7,8,9,10)
c=(1,4,b,26)#packed tuple
print(c)
print(len(c))
c=(1,4,*b,26)#unpacked tuple
print(c)
print(len(c))'''
'''d=1
c=d+25
print(c)'''
'''d=24,
c=d+4
print(c)'''# only concatenate tuple not possible
#type error
'''a={1,4,7,8,2,0,1,3}
print(a)
print(type(a)) #we cannot add lists inside a sets,we can add tuples
b={1,4,[1,4]}
print(b)#TypeError: unhashable type: 'list'
#sets are mutable'''
'''c={1,2,3,(2,3),5}
print(c)
c.add(25)
print(c)
c.add('o')
print(c)
c.add(0)#random order it will add
print(c)'''
'''a={1,2,3,4}
a.update(('codegnan',23,5,7))
print(a)
a.update((2,4,5,6))
print(a)
a.remove(4)
#a.remove(22)#KeyError: 22 it throw an error
print(a)
a.discard('codegnan')
print(a)
a.discard(22)#it doesnot throw an error
print(a)'''
'''a={1,2,3,4}
a.clear()
print(a)
a={1,2,3,4,5}
a.pop()# it takes index when we given position in lists omly
print(a)# in sets pop operation from starting position
a.pop()
print(a)
a.add(15)
print(a)
del a
print(a)#a is not defined
a.insert(2,5)'''# no attribute of insert
'''c=[1,2,3,4]
c.insert(3,7)# position,value
print(c)
c.append([1,3,4,5])# it takes as a packed list
c.extend([1,2,3,4])#un packed list
print(c)'''
'''a={}
print(type(a))'''# class dict
#sets are mutable
'''a={1,2,3,4,5}
c=a.copy()
print(c)
c={3,4,5,6}
d={1,5,9,10,12,15}
print(d)
e=c.union(d)# | union
print(e)
c=c|d
print(c)'''
'''c={1,2,3,4,5}
d={1,5,9,10,12,15}
e=c.intersection(d)
print(e)
e=c&d #intersection
print(e)
print(c)
c.intersection_update(d)# now c=intersection c&d
print(c)'''
#difference b/w two sets
'''c={1,2,3,4,5}
d={3,4,5,6}
print(d.difference(c))
e=d-c
print(e)
d.difference_update(c)
print(d)
d.update([16,17])
print(d)
b={1,2,3,4}
b.update([2,3,4])
#b.update({0,'murali','happy','sweet'})
b.update(('happy','sweet'))
print(b)'''
#symmetric difference '^' for usuage
'''c={1,5,9,10,12,15} # it taken out the common elements and combine the elements both in c&d
d={3,5,6,8}
c=c^d # sym diff:^
print(c)
c.symmetric_difference_update(d)
print(c)
print(c.isdisjoint(d))
print(c.issubset(d))
print(d)
d.remove(8)
print(d)
print(c.issuperset(d))
#{}-dictionary
a={}
print(type(a))'''# keys in the dictionary are unique not duplication
'''d={1:1,2:2,3:3,4:4}
print(d)
print(d[1])
print(d.get(1))
print(d.get(0))#none'''
'''s=set({1:'sno',2:25,3:29})
print(s)
#s=dict({1,2,3,4})
#print(s) #cannot convert dictionary update sequence element #0 to a sequence
#s[2]="sweet" # set does not support item assigniment
print(s)
a=set((1,2,3,4))
print(a)
s=dict({1:'apple',2:'red',3:'lemon'})
print(s)
s[3]='sweet'
print(s)
s[1]=2
print(s)
e=s.copy()
print(e)
e.pop(2)
print(e)'''
'''m=[1,2,3,4,5]
m.pop(4)#pop takes index as argument in lists
print(m)
m={3,4,5,6,7}
print(m.pop())'''
'''s=dict({1:6,8:9,9:'murali',6:8})
print(min(s))#1
print(max(s))#9
s[4]='mood'
print(s)#{1: 6, 8: 9, 9: 'murali', 6: 8, 4: 'mood'}
print(s[1])#6
e=s.copy()
print(e)#{1: 6, 8: 9, 9: 'murali', 6: 8, 4: 'mood'}
e.pop(6)
print(e)#{1: 6, 8: 9, 9: 'murali', 4: 'mood'}
print(e.get(8))#9
a=e.popitem()
print(a)   #(4, 'mood')
e.clear()
print(e)   #{}'''

# here pop() takes no arguments
'''s={1:2,4:8,5:8}
print(s.pop(5))
print(s)
print(s.popitem())# it display (key,value)
s.clear()
print(s)
a=[]
a.extend([4])
print(a)
a.clear()
print(a)
b={1,2,3,4}
b.clear()
print(b)
a=(1,2,3,4)
#a.clear()# tuples doesnot have clear()
print(a)
e={1:'a',2:'s',4:'i',5:'c'}
e.update((1,2,3,4))# cannot convert dictionary update sequence element #0 to a sequence
print(e)
e.clear()
e'''
'''e={1:'a',2:'s',4:'i',5:'c'}
e.update({1:2,13:4,5:9})
print(e)
print(e.keys())# list of keys
print(e.values())
print(e.items())#tuples in side the lists
a=[1,4,5,6]
b=dict.fromkeys(a)#{1: None, 4: None, 5: None, 6: None}
print(b)'''
#operations are the constructs
#arithmetic operations
'''[1,2,3,4]==[1,2,3,4]# True
print()
[1,2,3,4]==[1,4,3,2]# False
(1,2,3,4)==(1,2,3,4)#True
(1,2,3,4)==(1,3,4,2)#False'''
#identity operators
#=,+=,-=,*=,/=,**=
#is,isnot
'''a= 5 is 5
print(a)
print(5==5)
a=[1,2,4,5]is[1,2,4,5]#two lists may change so identity not True for=== it is true
print(a)
(1,2,3)==(1,2,3) True
a=(1,2,3)is(1,2,3) #True
print(a)'''
'''b='saketh' is "saketh"#True
print(b)
a= 'murali'is not"murali"#False
print(a)'''
#membership operator
#in ,notin
'''s='dog' in'dogbreed'
print(s)#True
b="codegnan"in("mur","codegnan")#True
print(b)'''
#bitwise operator

#| bitwise or
#& bitwise and
# ^ bitwise xoR
'''b=(5&3)
print(b) #1
c=(5^7) #2
print(c)
m=5<<3
print(m)
print(5<<7)#left shiftoperator
print(4<<8)'''
#logical operator
#and,or,not
'''a=5+3==8 and 25>21
print(a)#true
b=5+3>10 or"mural"in"muralikrish"#true
print(b)
print(not 25)#False
print(not 0)#true
print(not None)#True
print(5 & 3)#True
print(4 and 3)#3
print(5 or 3)#5
print([] and 25)#[]
print(False and  True)'''#false
'''print([1]and 25)#25
print([1]or 25)#[1]
print([] or 25)#25
print([] and {})#[]
print([] or {})#{}
a,b=15,34
print(a,b,sep=" ")
a,b=23,34
print("you have entered",a,b,"values")'''
#python operators
#arithetic operators(+,-,*,/,%,**,)
#assignment operators(=,+=,-=,*=,/=,//=,**=)
#comparison operators(==,!=,<,>,>=,<=)
#logical(and ,or,not)
#identity operator(is,is not)
#membership operator(in,not in)
#condition statement:
#elif condition
''' if(text expression):
       statement block1
    elif(text exp2):
        statement block2'''

'''num=int(input("enter the no:"))
if(num==0):
    print("the value is equal to zero")
elif(num>0):
    print("the value is +ve")'''
'''control statement:
while(condition):
    statement block
    statement block2'''
'''"def pyramid():
    n=int(input("enter the number:"))
    for i in range(0,n):
        for j in range(0,i+1):
            print("*" ,end=" ")
        print('\n')    
print(pyramid())"'''
#for loop iterating over list,tuple,dictionary, astring
#with the for loop we can execute a set of statements,once for each item in a list,tuple,set, e  
'''syntax:
for loop-control_var in sequence:
    statementblock'''
#point("formatitted string")%(variable list)
#%d,%i,%f int,float-->float
#%s str,%c char
'''a,b=12,25
print("a=%d,b=%f"%(a,b))
print("the values are:",(a,b))
print("value of a is:%d,b is:%f"%(a,b))
name="code"
print("hello %s" %(name))#%c means for single char,%s for multiple
print("hello %s" %name[0])
print("hello %s"%name[1:5:2])
print("hello %15s"%name)'''#hello              code
'''a="murali"
b="lux"
c="girl"
print("format spring with replacement fieds".format(a))#format spring with replacement fieds
print("code={0}".format(a))
print("number={}".format(a))#number=murali,(here we use tuples only and follows index order {})
print("number1={}".format(a,b,c))#displays only a value  for key
print("type1={0},type2={1},type3={2}".format(a,b,c))#type1=murali,type2=lux,type3=girl(here a=0,b=1,c=2 position of tuple)
#repetition control instructions(loops)
#for,while
syntax:
    for val in sequence:
        statements...
        statements...
        statements...
  '''
"""a=[1,4,7,8,9]
d=0
for i in a:
    
    d=d+i
print("the sum is%i"%(d))#the sum is29
print("the sum is :",(d))#the sum is : 29
print("the sum is :",d)#the sum is : 29"""
'''a={'name':'murali','age':21}
print(a.values())
print(a.keys())
print(a.items())'''
#while loop:as long as condition is True,it executes untill test expressions true

'''while(test-expression):
    statements....
    statements...'''
'''n=int(input("enter the values:"))
#to intialize the variable storing the sum and counter
i=0
s=0
while i<=n:
    s=s+i
    i=i+1
    print(s)
'''
'''#break statements
num=(1,2,3,4,5,6)
#declaring the tuple
num_sum=0
count=0
for x in num:
    num_sum+=x
    count+=1
    if count==5:
        break
print("sum of first",count,"integer is:",num_sum)'''
#continue statements
'''a=[]
for x in range(7):
    if(x==3 or x==7):
        continue
    a.append(x)
print(a)'''
#pass statement:it is used for syntactically error
'''x=0
while x<10:
    x+=1
    if x>=5:
        pass
        print("x:",x,end=",")'''#x: 5,x: 6,x: 7,x: 8,x: 9,x: 10,
'''num=[1,2,3,-5,-2,-3]
for i in num:
    if(i>0):
        pass
    else:
        print(i)'''
#assert:it is used to check whether the particular condition is fulfilled or not
#syntax:
#checkfor less than 0 we get assertion errror which is called exception basically we use assertion=exception
'''x=int(input("enter a number >0:"))
assert x>0,'wrong input entered'#syntax:assert condition," "
print("you entered:",x)''' '''
x=int(input("enter a number greater than 0:"))
try:
    assert x>0
    print("u have entered:",x)
except AssertionError:          #AssertionError: here error must be defined
    print("u have enter wrong  I/p")'''
#Function:
'''syntax:
def function_name(parameters):
   '''# function docstring'''
'''    statements(s)
function_name=identifier'''
'''def sum(a,b):
   ''' ''' docstring ''''''
    c=a+b
    print("sum=",c)#call the function
sum(10,25)
sum(1.5,10.75)'''
#return statement:
#it is used in side a function  to  return some 'value 'to callig function
#syntax:
'''def sum(a,b):
 '''   '''this function finds sum''''''
    c=a+b
    return c
x=sum(10,15)
print('the sum is :',x)
y=sum(18,18)
print('sum is %d'%y)'''
#try-except block:
#try block:enclose in it that you  anticipation will cause an exception
'''a=int(input("enter the number:"))
try:
    assert a>0,"number you should be greater than 0"
    print(a)
except AssertionError:
    print("check the num you have entered")
finally:
    print("happy gandijayanthi")
    print("october",1+1)'''
'''try:
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("denominator is zero")
except ValueError:
    print("unable to convert string to float(int)")
finally:
    print("it's done")#incase 2 or more exception please specify atleast one exception error
'''
'''def murali(a,b):
    c=a+b
    return c
print(murali(10,12))'''
#positional arguments
'''def add(a,b):
    return a+b
print(add(4,8))
#default arguments
def it(a,b="wonders"):
    return a+b
print(it("15"))'''
'''#keyword arguments
def python(course,price):
    print("course is %s"%(course))#here we can use  return,but it returns only one value to the calling function
    print("price is %.1f"%price)
print(python('datascience',30000))
print(python(price=25000,course='datascience'))'''
#variable arguments means many arguments
'''def addition(a,*b):
    d=0
    for i in b:
        d=d+i
        print(d+a)
addition(1,2,3,4,5,6)'''#a=store ist arg ,*b= next remaining   
'''a=int(input("enter the numbers:"))
b=[int(x) for x in input("enter the number:").split(',')]
print(b)
print(type(b))#list''' '''
a=int(input("enter the number:"))
b=[int(x) for x in input("enter the numbers:").split(",")]
def add(a,*b):
    d=0
    for i in b:
        d=d+i
    return d+a
print(add(a,*b))''''''
c=(1,4,(5,6,6))
b=(5,6,6)
print(c)
d=(1,2,4,5,*b)#unpacking tuples
print(d)'''
#keyword variable length arguments(**)
'''def char(name='sweet',marks=75):
    print(name,marks)
char('murali',95)
char()
d={'name':'bhavya','marks':100}
char(*d)#keys
char(**d)#values'''

'''def type(a,**b):
    print(type(b))
    for c,d in b.item():
        print("key={},value={}".format(c,d))
type(1,name='venkat',place='gudivada',sal=20000) '''
#global variables are the one that are defined and declare above a function
'''a='python'
def myfunction():
    b='webdevelopment'
    c=a+b
    print(c)
    print(b)
myfunction()
print(a)
print(b)#name error:b is not defined'''
'''a='murali'
def function():
    b='python'
    global a    #we make a as global here and assign a for carryout variable outside
    a='datascience'
    c=a+b
    print(c)#datasciencepython
    print(a)#datascience
function()
print(a)    #datascience
print(b)#NameError: name 'b' is not defined'''
#list comprehension
#list=[express for item in sequence (optional for and/or if )]
#toget squares of first 10
'''for i in range(11):
    print(i**2,end=",")''' '''
a=[i**2 for i in range(1,12)]
print(a,end='')'''
#to create a function to find total and average
'''a=[int(x)for x in input('enter the values:').split(',')]
def sanda(a):
    n=len(a)
    d=0
    for i in a :
        d=d+i
        avg=d/n
        return d,avg
x,y=sanda(a)
print(x)
print(y)'''
#set comprehension
'''a={x for x in range (1,10) if x%2==0}
print(a)'''
#dictionary comprehension
'''a={x:x for x in range(1,101) if  x%2==0}
print(a)'''
#conversion of list comprehension into tuple,set
'''b=tuple({x for x in range (1,10) if x%2==0})
print(b)#(8, 2, 4, 6)''' '''
b=tuple([(x,x**2,x**3) for x in range(10)])
print(b)'''
#generators
#generators are iterators ,akind of iterable you can iterate over once generators donot store all the values in memory
#eg:
'''mygenerator=(x*x for x in range(3))# we can get output by using for loop  and yield statement
for i in mygenerator:
    print(i,end=",")
print(mygenerator)'''#<generator object <genexpr> at 0x00000148BF493B30>
'''mygenerator=[x*x for x in range(3)]
print(mygenerator)'''#[0, 1, 4]
'''a=(x*x for x in range(11))#<generator object <genexpr> at 0x000001A9FBFC3B30>
print(a)'''
'''a=(x*x for x in range(11))
print(next(a))#0
print(next(a))#1
print(next(a))#4
print(next(a))#9
print(next(a))#16
print(next(a))#25
print(next(a))#36  '''    #so we can use next method to display tuple comprehension
'''def a():
    return 'a','b','c'
print(a())'''
#yield is used for generator for itrate valuews for more return
'''def a():
    yield  'a'
    yield  'b'
    yield  'c'
print(a())'''  #<generator object a at 0x000002BCA74F3B30>
'''def a():
    yield  'a'
    yield  'b'
    yield  'c'
dog=a()
for i in (dog):         #assigning for fetching the variable for bacause it is iterator
    print(i)'''
'''def a():
    yield 'a'
    yield 'b'
    yield 'c'
d=a()
print(next(d))#a
print(next(d))#b
print(next(d))#c   
print(next(d))#StopIteration'''
#function inside another function
'''def a():
    def b():
        return 'hello everybody yaa'
    print(b())
    r=b()+" welcome to the party yaa"
    return r 
print(a())'''
#function as a parameter to anotherfunction
'''def a():
    return 34
def b():
    print( a() ,'sweet' )   
b()'''
'''def a(d):
    return 'hello good morning'+str(d)
def b(e):
    return str(e)+'good luck'
print(a(b(25)))         #hello good morning25good luck
print(b(a(' sweet')))'''  #hello good morning sweetgood luck
#function can return another function
'''def hello():
    def message():
        return 'carry on'
    return message()+'dont cry with your emotions'
print(hello())'''#carry ondont cry with your emotions
# function can call itself is called recursive function
#factorial ,fibonacci
'''n=int(input("enter the number:"))
def a(n):
    a=0
    b=1
    if n==0:
        return 0
    elif n==1 :
        return 1
    else:
        for i in range(0,n):
            c=a+b
            print(c)
            a=b
            b=c
a(n)'''
'''n=int(input("enter a number"))
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(n)) '''
'''n=int(input("enter the value:"))
def fact(n):
    if n==0:
        return 1
    else:
        return fact(n-1)*n
print(fact(n))  '''   '''
a=dir(__builtins__)
print(type(a))'''         #list
'''print(25+24)
print(abs(-5) )  #5    
#print(abs('police'))  #type error  
print(bool())  #false  
print(bool(1))#true
print(bool('b'))#true
print(bool([]))#false
print(min([1,2,3,4,5]))#1
print(max([1,2,3,4,5]))#5
print(int(5-3))#2
print(float("%.5f"%6.000987))#6.00099
a=str(5)#5
print(type(a))#<class 'str'>
print(complex(5))#5+0j
print(chr(65))#A
print(ord('A'))#65
print(chr(110000))#𚶰
print(ord('b'))#98
print(list((1,2,3,'sai','raje')))#[1, 2, 3, 'sai', 'raje']
b=[1, 2, 3, 'sai', 'raje']
print(tuple(b))#[1, 2, 3, 'sai', 'raje']
print(set(b))#{1, 2, 3, 'raje', 'sai'}
#print(dict(b))#cannot convert
print(dict({1:5,5:9}))#{1: 5, 5: 9}'''  '''
a={1,2,3,4}
a.add(5)
a.update([1,2,3,6,8,9])
print(a)#   {1, 2, 3, 4, 5, 6, 8, 9}
b=frozenset(a)#frozenset({1, 2, 3, 4})
b.update((1,2,3))'''#AttributeError
#round
'''print(round(2.6))#3
print(round(3.6))#4
print(round(3.2))#3
print(4**3)#64
print(pow(6,3))#216
print(4^2)#6
print(bin(4))#0b100
print(sum(range(0,7)))#21
print(sum((2,4,5)))#11
print(sum({2,4,5}))#11
print(sum([2,4,5]))#11
print(25+26)
print("25+25")#25+25
#print(eval(25+25))#eval() arg 1 must be a string, bytes or code object
print(eval('24+25'))#49
print(eval('5/4'))#1.25'''
'''a=[1,2,4,5,2,7]
a.sort()
print(a)'''        '''
print(sorted([14,3,4,56,6,98]))#[3, 4, 6, 14, 56, 98] applicable only for lists
a=(divmod(6,2))
print(a)'''
'''a=[1,3,45,1,0]
b=[5,7,3,9]
c=zip(a,b)
print(c)#<zip object at 0x0000024D712AF7C0>
print(list(c))#[(1, 5), (3, 7), (45, 3), (1, 9)]#we can give tuple ,list,set for zip

a='murali','hot'
print(type(a))#tuple
#enumerate
print(enumerate(a))#<enumerate object at 0x000002259B311880>
print(list(enumerate(a)))#[(0, 'murali'), (1, 'hot')]
c=[8,9,6,4]
print(list(enumerate(c)))#[(0, 8), (1, 9), (2, 6), (3, 4)]
b='x','y','z',0,5,6,8
print(list(enumerate(b)))'''#[(0, 'x'), (1, 'y'), (2, 'z'), (3, 0), (4, 5), (5, 6), (6, 8)]
#we convert list into iterator
'''a=(1,3,4,7)
b=[1,3,4,7]
v=iter(a)
print(next(v))#1
w=iter(b)
print(next(w))#1
print(next(w))#3
print(list(v))#[1, 3, 4, 7]
print(tuple(w))#(1,3,4,7)'''
#function to complete  the logic 3*x+1
'''def f(x):
    y=3*x+1
    return y
print(f(8))'''    '''
#anonymous function:lamda function
a=lambda x:x**2
print(a(2))
print(type(a))#<calss function>
a=lambda s:s.upper()
print(a('lambdas'))'''#LAMBDAS 
'''b=lambda x:x.strip().upper()
print(b("         art of murali  "))'''#ART OF MURALI
'''c=lambda x,y:x if x>y else y
a,b=[int(n ) for n in input("enter two numbers").split(' ')]
print(c(a,b))'''
#lambda expression with multiple i/ps :
#social media registration
'''a,b='rgv','interview'
fullname=lambda a,b:a.strip().upper()+b.strip().capitalize()
print(fullname(a,b))'''#LavadaLalith
#filter function(builtsin function):it is used to remove unwanted data
'''a=[int(x) for x in input("enter the values:").split(" ")]
b=filter(lambda x:x%2==0,a)#syntax:filter(function/none,iterable)
print(list(b))'''#[2, 6, 2]
#remove the missing data
'''states=["","telangana","andhrapradesh","tamilnadu","",""]
new=filter(None,states)#['telangana', 'andhrapradesh', 'tamilnadu']   it removes gaps
print(list(new))'''
#map function map():syntax:map(function,*iterable)
#it tried to map from one function to another
#mapfunction():it gives corresponding sequence with original sequence,
#it applicable for all elements inside iterators
'''a=[1,4,7,9]
#b=[7,8,4,5,2]
c=list(map(lambda x:x//2,a))
print((c))'''   
'''a=[1,4,7,9]
b=[7,8,4,5,2]
c=list(map(lambda e,d:d*e,a,b))#[7, 32, 28, 45]
print(c)'''
'''a=list(map(float,input("enter the values:").split()))
print(a)'''        #[2.0, 4.0, 5.0, 6.0, 7.0]
'''a,*b=map(int,input("enter the values:").split())
print(a,*b)#2 5 6 7 8 9
a,*b=map(int,input("enter the values:").split())
print(a,b)#2 [5,6,7,8,9]'''
'''a,b=map(int,input("enter the values:").split())
print(a,b)#ValueError: too many values to unpack (expected 2)'''
'''a=dir(__builtins__)
print(a)'''
#modules:it is a file containing python code
#can define functions,classes,variables
#the file name is the module name with suffix .py extended
#to use module we just created,by using  imported statement:
#import the modulensmed ,and call the function()
'''print(__name__)#__main__
import mygreet       #filename:mygreet
a=mygreet.da(25000)  #da()
print(a)
from  mygreet import*
b=mygreet.hra(55000)
print(b)   '''   #13750.0
'''from mygreet import*
basic=float(input("enter the basic salary:"))
gross=basic+da(basic)+hra(basic)
netsalary=gross-pf(basic)-itex(gross)
print("gross salary is:",gross)
print("net salary is.",netsalary)'''
#print(help('modules')) it displays list of all modules
#print(help("mygreet"))#it dispaly module name ,functions names,file location
'''import math as m
b=m.sqrt(5)
print(b)#2.2360
print(m.log(10))#2.30
from math import*
print(pi)#3.14
print(sin(60))
import math
b=math.sin(180)
print(b)'''#-0.8011 in radians only
'''import math as m
print(m.ceil(4.2))#5 it always display integar
print(m.ceil(3.00009))#4
print(m.trunc(5.5))#5
print(round(4.8764,3))#4.876
print(round(4.256,2))#4.26 last two 56>50 so overall 6
print(m.floor(4.2))#4 downvalue
print(m.trunc(2.9))#2 floor=trunc always return integer values
print(m.fabs(-6))     #6.0
print(m.fmod(5,2))#1.0
print(m.remainder(5,2))    #1.0
print(divmod(5,2))     #(2,1) quotient,remainder
print(m.modf(4.5))#(0.5,4.0)
print(m.fmod(5,3))#remainder=2.0
print(m.hypot(3,4))#5.0'''
#sys module will check for system specification parameters
#os module
'''import sys
a=sys.path
print(a)#C:\\Users\\Murali\\Desktop\\free'
for i in sys.path:
    print(i)     '''       #C:\Users\Murali\Desktop\free
'''import sys
print(sys.version)'''#3.8.2rc2 (tags/v3.8.2rc2:777ba07, Feb 18 2020, 09:11:15) [MSC v.1916 64 bit (AMD64)]
#displayhook
'''x='saketh'
def display(x):
    print("software life")
    print(x)
display(x)
import sys
sys.displayhook=display(x)
print(displayhook)'''
#os module(operating system module)
'''import os
print(os.path)#<module 'ntpath' from 'C:\\Users\\Murali\\AppData\\Local\\Programs\\Python\\Python38\\lib\\ntpath.py'>
#path is shows like(\\ or /)
a=os.listdir()
print(a)          #['mygreet.py', 'pythontutorial.py', '__pycache__']
print(os.listdir())
#print(os.listdir('lib'))
#print(os.listdir('doc'))
#a=os.remove("C:\\Users\\Murali\\Desktop\\free\\sweet.py")
#print(a)    #FileNotFoundError
print(os.listdir())
print(dir())#all os files ['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'os']
print(dir('os'))
print(dir(os))#packages'''
#datetime modules
#date time module contains 4 important classes by the names 'datetime','date','time','timedelta'
#datetime class has four attributes year,month,day
#time delta class is useful to handle the duration
#time class has attributes hour,minutes,second,microsecond,tzinfo
#print(dir(__builtins__))#all builtin modules,error,functions
'''import time
print(time.time())''' #1633405791.3322072
'''import time
a=time.time()
for i in range(101):
    print(i)
end=time.time()
print(end-a)          #0.38074493408203125
print("{} seconds for the execution ".format(end-a))'''#0.38074493408203125
'''import time
a=time.time()
for i in range(100):
    print(i)
time.sleep(10)
b=time.time()
print(b-a)'''
'''import time
a=time.time()
t=time.localtime(a) #time module has monay=0,tuesday=1
print(t)
d=t.tm_mday
m=t.tm_mon
y=t.tm_year
print("today is %d-%d-%d"%(d,m,y))# 5-10-2021
h=t.tm_hour
m=t.tm_min
print(" current time is %d-%d"%(h,m))#10-9'''
'''import time
a=time.time()
f=time.ctime(a)
print(f)  '''       #Tue Oct  5 10:14:10 2021
'''from datetime import*
a=datetime.now()
print(a)   #2021-10-05 10:17:29.471474
y=a.year
m=a.month
d=a.day
h=a.hour
mi=a.minute
print("today is {}-{}-{}-{}-{}".format(y,m,d,h,mi)) '''  #today is 2021-10-5-10-24
'''from datetime import*
d=datetime.today()
print(d)  #2021-10-05 10:30:52.686486
e=date.today()
print(e)''' #2021-10-05
'''from datetime import*
print(date(2020,5,19)) #we have to given year-month-day 2020-05-19
f=time.today()
print(f)       #AttributeError
a=time.today()
print(a) '''       #AttributeError

'''from  datetime import*
d=date(2020,6,7)
print(d)'''
#formating date and time (strftime)
'''from datetime import*
d=date(2020,8,19)
s=d.strftime("%d-%b-%y")#19-Aug-20
print(s)
n=d.strftime("%D-%B-%Y") #308/19/20-August-2020
print(n)
e=d.strftime("today is %a")
print(e) #time is Wed
f=d.strftime("today is %A")
print(f)''' #today is Wednesday
#strptime(string point of time)    #datetime.date(string,format)   format=%d %b %y
'''from datetime import*
value="26 december 1993"
s=datetime.strptime(value,"%d %B %Y")
print(s)    #1993-12-26 00:00:00
murali="26-dec-2021"
b=datetime.strptime(murali,"%d-%b-%Y")   #%b means short form of month name
print(b) '''         #2021-12-26 00:00:00
#checkcases
'''d,m,y=[int(x) for x in input("enter the date:").split("-")]
print(d,m,y)
from datetime import*
g=date(y,m,d)
print(g) '''  #2021-10-05         datetime module sunday=0,but timemodule monday=0
#calendermodule
'''from calender import*
y=int(input("enter the year"))
if isleaf(y):
    print("y is leafyear")'''
#leaf year
'''def leaf(y):
    return y%4==0 and(y%100!=0 or y%400==0)
print(leaf(2020) )''' #true  
#print(help('keyword'))
#python is a case sensitive
'''a=True
print(type(a)) #<class 'bool'>
a=False
print(type(a))   #<class 'bool'>
print(bool(0))#false   
print(str(2))#2
print(complex(1))#1+0j
print(int('8'))#8
#indexing
a=True
#print(len(a))#TypeError: object of type 'bool' has no len()
#strings are immutable
print(float(25))#25.0'''
#list methods:append(),clear(),remove(),copy(),count(),extend(),index(),insert,pop(),reverse(): sorting in ascending order


                        #calender module#
'''from datetime import*
value=("25 november 1991")
a= datetime.strptime(value,"%d %B %Y")#1991-11-25 00:00:00
print(a)

g=date(1991,11,25)#1991-11-25
print(g)
print(g.strftime("%d %b %y"))#25 Nov 91
print(g.strftime("%w %b %Y"))''' #1 Nov 1991
'''from calender import*
y=int(input("enter the year"))
if isleaf(y):
    print(y, " is leaf year")'''
           #random module
'''import random
c=random.random #shows values between (0,1)


a=random.randint(10,30)
print(a)'''   # mustbe given this range of integers
'''import random
for i in range(3):
    print(random.randint(1000,4000))#strting ,ending also includes
    print(random.randrange(1000,6000))'''
  #FILES#:keyfunction for working with files in python is the open()
#the open() function takes two parameters: filename and mode
#ther are (modes) for opening file
#1) "r"-read-default value.opens file for reading,error if the file doesnot exist
#2) "a"-append-opens a file for appending creates the file if it doesnot exist
#3)"w"-write-opens a file for writing creates file if it doesnot exist
#4)"x"-create-creates the specified file returns error if file already exists
#5by default,when only the filename is passed openfunction opens the file in read
#5)''' all program files are text files'''
#6)'''all images,videos,music,executable files are binary files
# file I/O operations
# opens file ,read/write data into it,close
#syntax:-a=open('text.txt','w')# (filename,mode->"r" is default mode)
'''a=open('text.txt','w')
d=['chistopher','murali','hari','bhavya',45]
#a.write(d) 
#print(a) #TypeError: write() argument must be str, not list
a.write(str(d))
a.close()'''
#you need to close() the file for 'w' mode) a.close()
'''a=open('text.txt','w')
d=['suma','valanya','bhavya','sweet']
a.writelines(d)  #a.write():it delete previous data and stores current data only
a.close()'''   #sumavalanyabhavyasweet
#wrielines used for when we give any container like list,tuple,sets, but container 
#has only strings both for a.write,a.writelines()
'''a=open('text.txt','x')#create-creates the specified file returns error if file already exists
a.write('good mornging my dears')
a.close()'''   #FileExistsError: [Errno 17] File exists: 'text.txt'
'''a=open('sweet.txt','x')
a.write('how are you friends')
a.close()'''
'''a=open('sweet.txt','a')
a.write(' how are you')
a.close()'''
'''d=open('sweet.txt','r')# r for read operation only for existed files
#d.write('hai ra suri!')#io.UnsupportedOperation: not writable
print(d.read())'''#how are you friendshow are you

                 #file reading is comon for all +,modes #
#'r+' opens a file for readinf/writing,placing the pointer at the beginning of 
#'w+' opens a file for wrting and reading ,previous content is removed
#'a+' opens a file for appending and reading
'''a=open("text.txt",'r+')
a.write('eagarly waiting for it') #text at beginning
a.close()'''#eagarly waiting for it', 'hari', 'bhavya', 45]   
'''a=open('tenet.txt','w+')
a.write('hello guys')
print(a.read())#cannot execute here o/p we can read use.read() for'w+'
a.close()'''
'''a=open('tenet.txt','a+')#hello guysall are doing good 
print(a.read())#cannot execute here o/p we can read use.read() for'a+'
a.write('all are doing good ')
a.close()'''
'''with open('tenet.txt') as f:
    print(f.read())''' #hello guysall are doing good
'''import sys
arguments=len(sys.argv)
if sys.argv[1]=='hello':
    print("u have selected for halo arg")
elif sys.argv[2] =='__version':
    print('my version is just 3.0')
print(arguments)
print(sys.argv)'''
#sys module getopt module incommand line used for pass multiple arguments
#getopt module goes a bit further and extends a separation
#by parameter validation
'''import getopt,sys
argv=sys.argv[1:]
try:
    opt,args=getopt.getopt(argv,'hm:d',['help','mylife'])
    print(opt)
    print(args)
except getopt.getoptError:
    print("something went wrong")'''
#using formatting string(often called fstring) filter:
a,b,c=25,2,7
print(a,b,c)
print("the values of a is %d,b is %d, c is %d"%(a,b,c))#the values of a is 25,b is 2, c is 7
print("{}".format(a))#25
print(f"{a}")# fstring not allowed empty expressions
#print(f'{}')# empty expressions not allowed
temp='geeks 34 for 56543'
print(temp.isdigit())#False
print(temp.isalnum())#false because some spaces
a='1435hfy'
print(a.isalnum())#True


















