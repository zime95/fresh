#LISTS
##lst={8,10,6,2,4} #list
#We need (5-1) to comparison
##swapped=True
##while swapped:
##    swapped=False
##    for i in range (len(lst)-1):
##        if lst[i]>lst[i+1]:
##            swapped=True
##            lst[i],lst[i+1]=lst[i+1],lst[]
#INCOMPLETE
################################################################################

#TUPLES CANNOT BE EDITED (STATIC TYPE)
##tuple1=(1,2,4,8)
##tuple2=1.,.5,.25,.125
##tupleExp=(1,10,100,1000)
##print(tuple1)
##print(tuple2)
##print(tupleExp[0])  #1
##print(tupleExp[-1]) #1000
##print(tupleExp[1:]) #
##print(tupleExp[:-2])
##print(tuple1+tuple2)
##t1=tuple1+(16,32)
##print(t1)
##print(10 in tupleExp)
##print(-10 not in tupleExp)

##for el in tupleExp:
##    print(el)
##else:
##    print("else: ",el)
################################################################################

#DICTIONARIES
##dct={'dog':'chien','cat':'chat','horse':'cheval'}#Dictionary
##phones={'boss':555223,'John':112233}

##print(dct)

##print(dct['cat'])#chat
##print(phones['John'])

#Comparison of sorts
##words=['cat','lion','horse']
##for word in words:
##    if word in dct:
##        print(word,"->",dct[word])
##    else:
##        print("Not in dictionary: ",word)

#To see elements
##for key in dct.keys():
##    print(key,"->",dct[key])

#Adding to the Dictionary
##dct['lion']='lion'
##dct['cat']='kedi'
##del dct['horse'] #To Delete from Dictionary

#Honestly, not sure myself :(
##for en,fr in dct.items():
##    print(en,"->",fr)

#Only Printing the Values from the Dictionary
##for fr in dct.values():
##    print(fr)

#Sorting the Dictionary and Displaying it
##for en,fr in sorted(dct.items()):
##    print(en,"->",fr)
################################################################################

#2D LIST
##number_grid=[[1,2,3],[4,5,6],[7,8,9]]
##print(number_grid[2][0])
##
##for i in range(1):
##    for j in range(3):
##        print(number_grid[i][j])
################################################################################

#NOT SURE EXACTLY
##global var
##var=3
##def myFunction(mylist):
##    print (mylist)
##    var=2
##    print (var)
##L=(0,1)
##print (myFunction(L))
################################################################################

#IMPORTS AND MATH FUNCTIONS
##from math import ceil, floor, trunc, factorial

##x=1.4
##y=2.6
##z=5
#FLOOR
##print(floor(x), floor(y))#the smallest number
##print(floor(-x), floor(-y))
#CEIL
##print(ceil(x), ceil(y)) #the largest number
##print(ceil(-x), ceil(-y))
#TRUNCATE
##print(trunc(x), trunc(y))
##print(trunc(-x), trunc(-y)) #the value of x truncated to an integer
################################################################################

#MORE MATH FUN :D
##from random import randint, choice, sample

#GENERATING RANDOM NUMBERS
##for i in range(10):
##    print(randint(1,10),end=",")

##list1=[1,2,3,4,5,6,7,8,9,10]
##print()
##print(choice(list1))
##print(sample(list1,3))
################################################################################

#COMPUTER SYSTEM FUN:D
##from platform import processor, machine, system, version

##print(processor())
##print(machine())
##print(system())
################################################################################

##import module
##print(module.counter)

################################################################################

##print("I like to be a module")
##print(__name__)#double underscore
##
##counter=0;
##if __name__=="__main__":
##    print("I prefer to be a module")
##else:
##    print("I like to be a module")

################################################################################

##try:
##    x= int(input())
##    y=1/x
##    print(y)
##except ZeroDivisionError:
##    print("Cannot divide by zero - sorry")
##except ValueError:
##    print("You have to enter an integer value")
##except:
##    print("Oh, dear!")
##print("THE END")
################################################################################

##string='abcdefghi'
##text="students the"
##fnd=text.find('the')
##L=['Omega','Alpha','Gamma']
##L2=sorted(L,reverse=True)
##print(L2)
##
##while fnd!=-1:
##    print(fnd)
##    fnd=text.find('the', fnd+1)
##
##print(string.capitalize())
##print('z' in string)
##print("AaBbCcYyZz".index('a'))
##
##if "epsilon".endswith('on'):
##    print('Yes')
##else:
##    print('No')
##
##for x in range(len(string)):
##    print(string[x],end=" ")

################################################################################

##class MyClass:
##    x=5
##
##p1=MyClass()
##print(p1.x)

################################################################################

#CLASSES AND STUFF
##class Person:
##    def __init__(self,name,age):
##        self.name=name
##        self.age=age
##
##    def myfunct(self):
##        print("Hello my name is "+self.name)
##    def checkAge(self):
##        if self.age>=18:
##            print(self.name,"you can apply for a driving license.")
##        else:
##            print("GTFO",self.name)
##
##p1=Person("John",36)
##p1.myfunct()
##p1.checkAge()
##p2=Person("Trishen",11)
##p2.myfunct()
##p2.checkAge()
##
###################################################################################3

#Class Star EXAMPLE
##class Star:
##    def __init__(self,name,galaxy):
##        self.name=name
##        self.galaxy=galaxy
##
##    def __str__(self):
##        return self.name + " in " + self.galaxy
##
##sun = Star("Sun","Milky Way")
##print(sun)

################################################################################

#INHERITANCE - TRISHEN
##class Person:
##    def __init__(self,first,last,age):
##        self.firstname = first
##        self.lastname = last
##        self.age = age
##
##    def Age(self):
##        Dob= 2019 - self.age
##        return self.firstname + " " + self.lastname + " and you are " + str(Dob)
##
##    def name(self):
##        return self.firstname + " " + self.lastname
##
##class Employee(Person):
##    def __init__(self,first,last,staffnum):
##        Person.__init__(self,first,last)
##        self.staffnumber = staffnum
##
##    def GetEmployee(self):
##        return self.Name() + ", " + self.staffnumber
##
##p1 = Person("Trishen","Chetty",1996)
####print(p1.name())
##print(p1.Age())

#OR

#INHERITANCE - TRISTIN
##class Person:
##    def __init__(self,first,last,age):
##        self.firstname = first
##        self.lastname = last
##        self.age = age
##
##    def Age(self):
##        return self.firstname + " " + self.lastname + " and you are " + str(2019-self.age)
##
##    def name(self):
##        return self.firstname + " " + self.lastname
##
##class Employee(Person):
##    def __init__(self,first,last,staffnum):
##        Person.__init__(self,first,last)
##        self.staffnumber = staffnum
##
##    def GetEmployee(self):
##        return self.Name() + ", " + self.staffnumber
##
##p1 = Person("Tristin","Padayachee",1996)
####print(p1.name())
##print(p1.Age())

################################################################################

##from os import strerror
##try:
##    ccnt = lcnt = 0
##    s = open('text.txt','rt')
##    line = s.readline()
##    while line != '':
##        lcnt += 1
##        for ch in line:
##            print(ch,end='')
##            ccnt += 1
##        line = s.readline()
##    s.close()
##    print("\nCharacters in file: ", ccnt)
##    print("Lines in file: ", lcnt)
##except IOError as e:
##    print("I/O error occured: ", strerror(e.errno))

################################################################################

##from os import strerror
##
##try:
##    fo = open('nexttext.txt','wt')
##    for i in range(10):
##        s = "line #" + str(i+1) + "\n"
##        for ch in s:
##            fo.write(ch)
##    fo.close()
##except IOError as e:
##    print("I/O Error Occurred",strerror(e.errno))

################################################################################

#STACK
stack = []

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)
print(pop())
print(pop())
print(pop())
print(stack)
