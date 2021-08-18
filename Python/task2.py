
#1
number = int(input("please enter number of your choice:\n"))
if ((number%3)==0) and  ((number%5)==0):
    print("Consultadd - Python Training")
elif(number%3 ==0):
    print("Consultadd")
elif(number%5==0):
    print("Python Training")

#2
print("1 : Addition \n 2 : Subtraction \n 3 : Division \n 4 : Multiplication \n 5 : Average \n")
choice = int(input("please enter your choice to perform any of  the above operation:"))
num1 = int(input("please enter first number:"))
num2 = int(input("please enter second number:"))
while choice in range(1,6):
    if(choice ==1):
        result = float(num1+num2)
        print("The sume of enetered number is ", result)
        break;
    
    elif(choice ==2):
        result = float(num1 - num2)
        print("The sume of enetered number is ", result)
        break;
    elif(choice ==3):
        result = float(num1 / num2)
        print("The sume of enetered number is ", result)
        break;
    elif(choice ==4):
        result = float(num1 * num2)
        print("The sume of enetered number is ", result)
        break;
    elif(choice ==5):
        a1 = int(input("please enter one more number:"))
        a2 = int(input("please enter another number:"))
        result = (num1+num2+a1+a2)/ 4
        print("The sume of enetered number is ", result)
        break;
if result<0:
    print("NEGATIVE ANSWER")

#3
a,b,c = 10,20,30
avg = ((a+b+c)/3)
print("avg = ", avg)
if((avg > a) and (avg > b) and (avg > c)):
    print("average is higher than a, b and c")
elif(avg>a) and (avg>b ):
    print("average is higher than a and b")
elif(avg>a) and (avg>c ):
    print("average is higher than a and c")
elif(avg>b) and (avg>c ):
    print("average is higher than b and c")
elif(avg>a):
    print("average is just higher than a")
elif(avg>b):
    print("average is just higher than b")
elif(avg>c):
    print("average is just higher than c")

# 4
while(True):
    num = int(input("enter number: \n"))
    if(num > 0):
        print("Good Going")
        continue
    else:
        print("It's Over")
        break;


#5

for num in range(2000, 3201):
    if(num % 7) == 0:
        if(num% 5) ==0:
            continue
        else:
            print(num)

#6
x=123
for i in x:
    print(i)

# error 'int' object is not iterable

i =0
while i <5:
    print(i)
    i+= 1
    if i==3:
        break;
    else:
        print("error")
#This code is dislaying number 0 then error 1 error 2 and then it break


count =0
while True:
    print(count)
    count+=1
    if count>=5:
        break;
#This code print value from 0-4.

#7
for i in range(0,6):
    if(i ==3):
        continue
    else:
        print(i)

#8
test = input("enter string to calculate alphabet and digit count \n")
alphacount= digcount =0
for x in test:
    print(x)
    if x.isalpha():
        alphacount+=1
    elif x.isdigit():
        digcount+=1
    else:
        pass
print("Count of alphabet in string is:  ", alphacount)
print("Count of digits in string is:  ", digcount)


#9
lucky_num = 12
user_input = int(input("Guess lucky number \n"))
while(user_input!= lucky_num):
    print("You have Guessed Incorrect Number")
    user_input = int(input("Guess lucky number Again \n"))

#Modified:
lucky_num = 12
user_input = int(input("Guess lucky number \n"))
guess_again = 'y'

while(user_input!= lucky_num and guess_again == 'y'):
    print("You have Guessed Incorrect Number")
    option = str(input("do you wish to guess again ? Respond in 'y' or 'n'."))
    guess_again = option
    if(guess_again == 'y'):
        user_input = int(input("Guess number Again \n"))

#10
lucky_number = 10

counter = 1
while counter <=5:
    user_input = int(input("Guess lucky number : \n"))
    if(user_input == lucky_number):
        print("Good Guess!!")
    else:
        print("Try Again")
    counter+=1
print("Game Over!")

#11
lucky_number = 10

counter = 1
while counter <=5:
    user_input = int(input("Guess lucky number : \n"))
    if(user_input == lucky_number):
        print("Good Guess!!")
        break
    else:
        print("Try Again")
    counter+=1
else:
    print("Sorry but that was not very successful")