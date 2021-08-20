#1
list1 = ['hello', 1, 1+2j,2.0,2,3,4,5,6,7]
print(list1)

#2
list2 = [1,2,3,4,5]
print(list2[:], '\n', list2[:5],'\n', list2[0:3],'\n',list2[-1::1],'\n',list2[4::-2])

#3
list3 =[1,2,3,4,5]
result=0
mulres=1
for x in list3:
    result = result + x
    mulres = mulres * x
print("sum results is: \n", result)
print("Multiplication results is: \n", mulres)  

#4
largeSmall = [10,20,70,700]
largeNum = smallNum = largeSmall[0]
for i in range(len(largeSmall)):
    if(smallNum > largeSmall[i]):
        smallNum = largeSmall[i]
    if(largeNum < largeSmall[i]):
        largeNum = largeSmall[i]
print("Small Number in List is : \n", smallNum)
print("Large Number in List is : \n", largeNum)

#5
list_mix = [2,90,79,66,87,57,201]
list_odd =[]
for x in list_mix:
    if(x % 2 !=0):
        list_odd.append(x)
print("list after removing all even numbers: ", list_odd)

#6
squares = list()
for i in range(1,31):
    squares.append(i**2)
print("square of first 5 numbers are:  ", squares[:5])
print("square of first 5 numbers are:  ", squares[-5:])

#7
list1 = [1,3,5,7,9,10]
list2 = [2,4,6,8]
list1[-1:] = list2
print("final List : ", list1)

#8 
dic1 = {1:10,2:20}
dic2 ={3:30,4:40}
dic_merger = dict()
dic_merger.update(dic1)
dic_merger.update(dic2)
print("Merged dictionary is:", dic_merger)

#9
n= 10
new_dic =dict()
for i in range(1,n):
    new_dic[i] = i*i
print(new_dic)

#10
number = input("enter numbers of your choice")
print(type(number))
list1 = number.split(",")
#result_tuple = tuple(map(int, number.split(",")))
result_tuple = tuple(number.split(","))
print("resultant list : ", list1)
print("resultant tuple is : ", result_tuple)