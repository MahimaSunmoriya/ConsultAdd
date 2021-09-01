#1
teststr = "hello123"
print(teststr[::-1])

#2
def CountCase(string):
    countUpper =0
    countLower = 0
    for x in string:
        if x.isupper():
            countUpper +=1
        elif x.islower():
            countLower +=1
    return countLower,countUpper

l,u=CountCase("HelloThere!!")
print("lower case charcter in 'HelloThere!!' is: ", l,"\nUpper cases charcters in 'HelloThere!!' is: ", u)

#3
def uniqueList(list):
    uniqueList = []
    for x in list:
        if x not in uniqueList:
            uniqueList.append(x)
        else:
            pass
    return uniqueList
testList = [1,1,4,5,5,6,7,7,8,9]
finalList = uniqueList(testList)
print("List of Unique elements are: " ,finalList)

#4
#input_string = input("please enter hypen seprated word \n")
input_string = "hello-there-how-are-you"
listString = list(input_string.split("-"))
listString.sort()
print(listString)
        
#5  
#seq_string = input("please enter any String \n")
seq_string = "hey How is Everything?"
converted_String=seq_string.upper()
print(converted_String)

#6
#number1 = input("please enter  a number for summation \n")
#number2 = input("please enter second number for summation \n")
number1 , number2 = str(100), str(300)
result = int(number1) + int(number2)
print("Addition of entered number is : ", result)

#7
def largestString(str1, str2):
    if(len(str1) > len(str2)):
        print("largets string is: ", str1)
    elif(len(str1)== len(str2)):
        print("both the strings are same: ", str1, '\n', str2)
    else:
        print("largets string is : ", str2)

firstString = "Hey How are you"
secondString ="I am good what."
largestString(firstString,secondString)

#8
def squareValueTuple():
    squareTuple = tuple()
    for i in range(1,21):
        squareTuple = squareTuple + (i**2,)
    print(squareTuple)
squareValueTuple()

squareValueTuples = tuple(map(lambda x: x**2, range(1,21)))
print((squareValueTuple))  ### why I am not getting tuple? Why I am getting object loc

#9
def showNumbers(limit):
    for i in range(0,limit+1):
        if(i%2 == 0):
            print(i," EVEN")
        else:
            print(i," ODD")
showNumbers(7)

#10

result = filter(lambda x: x % 2 == 0, range(1,21))
print(list(result))

#11
result = map(lambda x: x**2,filter(lambda x:x % 2 == 0,range(1,11)))
print(list(result))

#12
def handleZeroDivisionError(a,b):
    try:
        c=a/b
    except ZeroDivisionError:
        c=0
    print("result of division is : " , c)

handleZeroDivisionError(5,0)

#13
from functools import reduce
import operator
nestedList=[[1,2,3],[4,5],[6,7]]
falttenList=reduce(operator.add,nestedList)
finalResult=falttenList[0:7]
for i in finalResult:
    print(i,end="")

#14
def checkThreeDivision(num):
    if (num%3) ==0:
        return True
    else:
        return False
def multipleSeven(num):
    if (num % 7) == 0:
        isdivisible = checkThreeDivision(num)
        if isdivisible == False:
            print("\n The number is multiple of 7 but not divisible by 3 : ", num)
    else:
            print("\n The number is not a multiple of 7 :", num)

multipleSeven(49)
#15
def multiplication(element):
    print(element)
    return element * element
list1 =[1,2,3]
map(multiplication, list1)
result = list(map(multiplication, list1))
print((result))
#16
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

# The output would be 2

def a():
    try:
        f(x,4)
    finally:
        print('after f')
        print('after f?')
a()

# Error and print statements 