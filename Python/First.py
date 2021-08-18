## Task1
a, b, c = 1, [1,2,3],'first'
print(a,b,c)

var1 = 10+5j
var2 = 2
print("var1 " , var1, "var2",var2)
(var1, var2) = (var2,var1)
print("After \n var1 " , var1, "var2",var2)

variable1 = 10
variable2 = 20
print("before swap \n variable1", variable1,"\n variable2", variable2)
temp = variable1
variable1 = variable2
variable2 = temp
print("after swap \n variable1", variable1,"\n variable2", variable2)

x , y = 30,40
print("before swap \n x", x,"\n y", y)
(x,y) = (y,x)
print("after swap \n x", x,"\n y", y)


#version2
input_var = eval(raw_input("enter number of your choice"))
print(input_var)

#version3
input_var = eval(input("enter number of your choice"))
print(input_var)

#5
input1 = eval(input("please enter number of your choice between 1-10"))
input2 = eval(input("please enter another number of your choice between 1-10 for addition"))
if(input1>10 or input2>10):
    print("number entered by you is not in range of 1- 10")
else:
    z = input1 +input2
    result = z+30
    print("result: ",result)

#6
ch = eval(input("enter value of your choice"))
print(type(ch))

#7
UpperCamel = "This is Upper Camel Case "
lowerCamel = 20
snake_case = "This is snake Case "
UPPER = "This is Upper Case "

#8
a =10
print(type(a))
a='hello'
print(type(a))
# yes the data type will be changed , since in python the a is first pointing to memory loaction of integere value ,
#  which got switched to string memeory location after assigning the a to string data type
