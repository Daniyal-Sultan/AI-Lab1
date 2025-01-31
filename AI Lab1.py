# #Q1

# name = input("Enter Your Name: ")
# age = input("Enter Your Age: ")

# print("Welcome ", name, "! Your age is ", age)

# #Q2
# number = input("Enter Number: ")
# if '.' in number:
#     floatnum = float(number)
#     print("This is a float.\n", floatnum)
# else:
#     intnum = int(number)
#     print("This is an integer.\n", intnum)


# #Q3
# list1 = {'a','b','c','d','e'}
# list1.add('f')
# list1.remove('e')

# for i in list1:
#     print(str(i).upper())

#Q4
# SampleTup = {"a","b","c","d"}
# El1 = SampleTup[1]
# El2 = SampleTup[2]
# print(El1, "\n", El2)

#Q5
# Dictionary = {"Std1": "A", "Std2": "B", "Std3": "C", "Std4": "D", "Std5": "A+"}
# print(Dictionary)

#Q6
# input1 = input("Enter all the numbers for your first list in one go: ")
# list1 = []
# for char in input1:
#     list1.add(input1[char:1])

# print(list)

#Q7
# def EvenOrOdd(n):
#     if n%2==0:
#         return "even."

#     return "odd."

# def PosOrNeg(n):
#     if n > 0:
#         print("Number is positive and",EvenOrOdd(n))
#     elif n < 0:
#         print("Number is negative and",EvenOrOdd(n) )
#     else:
#         print("Number is 0 and even by default.")
#     return 0

# NumCheck = input("Enter Number: ")
# IntNum = int(NumCheck)
# PosOrNeg(IntNum)

#Q8

# for num in range (50):
#     if num%3==0 and num%5== 0:
#         print("FizzBuzz")
#     elif num%5==0:
#         print("Buzz")
#     elif num%3==0:
#         print("Fizz")
#     else:
#         print(num)

#Q9
# def FactCalc(FactNum, sum):
#     if FactNum>0:
#         for i in range(1, FactNum):
#             sum = sum * i
#         print("Factorial:",sum)
#     else:
#         print("Error. Number is either zero or negative.")
#     return 0

# Fact = int(input("Enter Number for Factorial Calculation: "))
# s = Fact
# FactCalc(Fact,s)

#Q10
# def PrimeCheck(n):
#     if n == 2 or n == 3 or n == 5:
#         return 1
#     if n == 4:
#         return 0
#     for i in range(2,int(n/2)):
#         if n%i==0:
#             return 0
#     return 1

# num = int(input("Enter num: "))
# if PrimeCheck(num) == 1:
#     print(num,"is prime.")
# else:
#     print(num,"is not prime.")

#Q11

# def SquareList(nums):
#     list2 = [num * num for num in nums]
#     return list2

# list1 = [1,2,3,4]
# print(SquareList(list1))

#Q12

dict1 = {"a":1, "b":2,"c":4}
dict2 = {"d":5, "c":50, "e":6}

dict1.update(dict2)
print("Merged Dictionary: ",dict1)

#Q13

# def RefinedList(SampList):
#     newList = []
#     for num in SampList:
#         if num not in newList:
#             newList.append(num)
#     return newList

# l1 = [1,2,3,4,4,5,6,5]
# print(RefinedList(l1))

#Q14

# def PalindromeCheck(st):
#     if st == st[::-1]:
#         return "This is a palindrome."
#     else:
#         return "This is not a palindrome."

# string = "racecar"
# print(PalindromeCheck(string))

#Q15
# def FiboSeq(num):
#     sum1 = 1
#     sum2 = 1
#     print(0)
#     print(1)
#     print(1)
#     for i in range(2,num-1):
#         finalsum = sum1+sum2
#         sum1 = sum2
#         sum2 = finalsum
#         print(finalsum)

# n = int(input("Enter range n for generating Fibo sequence: "))

# if n == 0:
#     print(0)
# elif n == 1:
#     print("0,1")
# elif n == 2:
#     print ("0,1,1")
# else:
#     FiboSeq(n)


#Q16

# print("Enter a number one by one to calculate the average. Press X to stop.")
# inputnum = input("Number 1: ")
# if inputnum!="X" or inputnum!=float(inputnum) or inputnum!=int(inputnum):
#         print("Error try again.")
# sum = 0
# count = 0
# validity = False
# while inputnum!="X":
#     sum = sum + float(inputnum)
#     count+=1
#     validity = False
#     while validity==False:
#         inputnum = input(f"Number {count+1}: ")
#         if inputnum!="X" or inputnum!=float(inputnum) or inputnum!=int(inputnum):
#             print("Error try again.")
#         else:
#              validity = True

# print("Average=",sum/count)

#Q17

# for i in range(11):
#     for j in range(11):
#         print(f"{i} * {j} = {i*j}")

#Q18
# database = {"User1": "Pass1", "User2":"Pass2", "User3":"Pass3"}

# user = input("Enter username: ")

# if user in database:
#     password = input("Enter password: ")
#     if password == database[user]:
#         print("Login successful.")
#     else:
#         print("Invalid password.")
# else:
#     print("User does not exist.")

#Q19

# def WordFreq(words):
#     WCount = {}
#     for word in words:
#         if word in WCount:
#             WCount[word]+=1
#         else:
#             WCount[word]=1
#     return WCount

# UInput = input("Enter a sequence of words: ")
# WList = UInput.split()
# Freq = WordFreq(WList)
# print(Freq)

#Q20

# def TempConvert(num, typ):
#     if typ=="F":
#         return ((num - 32)* (5/9))
#     else:
#         return ((num * 9/5)+32)

# Temp = int(input("Enter value of temperature: "))
# validity = False

# while validity == False:
#     TypeOfTemp = input("Enter type of temperature (C/F): ")
#     if TypeOfTemp == "C" or TypeOfTemp == "F":
#         validity = True
#     else:
#         print("Try again.")

# print("Converted Temperature: ",TempConvert(Temp, TypeOfTemp))