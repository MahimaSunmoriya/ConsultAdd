
#1

try:
 #    eval( 'print x>>0 ' )
 exec ('print "hello"')  
except SyntaxError:
    print("invalid Syntax !!! Please correct your Syntax.")

#2
import sys 

fileName = sys.argv[1]
(" File Name You wish to open is: \n", fileName)
while True:
    try:
        fo = open(fileName,"r")
        line = fo.read()
        print(line)
        fo.close()
        break
    except:
            choice=input("file name entered by you does not exist. Do you wish to try again with correct file name. Please enter 'Y' for Yes and 'N' for No.")
            if choice== 'Y':
                fileName= input("Enter the file name you wish to Open: \n")
            else:
                break       

#3   
#Write a program to handle an error if the user entered a number more than four digits it should
#return “The length is too short/long !!! Please provide only four digits”
 
def digitCheck(Number):
    try:
        if(len(str(Number)) != 4):
            raise ValueError("The length is too short/long !!! Please provide only four digits ")
    except:
        print("Please provide only four digits")
        raise

digitCheck(eval(input("please enter number of your choice")))

#4
#Create a login page backend to ask users to enter the username and password. Make sure to
#ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
#should not be more than 3 times.
counts = 0
while counts < 3:
    userName = input("Please enter username to login: ")
    password = input("Enter Password: ")
    re_type = input("retype Password:")
    counts+=1
    if(password == re_type):
        print("Successfull !!!")
        break
    elif(counts<3):
        print("Something went wrong please try again!!!")
    else:
        print("You exahusted all your attempts!!")

#6
#Read doc.txt file using Python File handling concept and return only the even length string from
#the file. Consider the content of doc.txt as given below:
with open("doc.txt","w") as text:
    text.write("Hello I am a File\nWhere you need to written the data String\nWhich is of even\n")
    text.write("Make sure you return the content in same link as  it is present ")
    text.close()
with open("doc.txt") as text:
    Result = ""
    for i in text:
        read = i.split()
        for j in read:
            if(len(j)% 2 == 0):
                Result = Result + " " + j

print(Result)
            
