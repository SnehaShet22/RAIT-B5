# the fizz buzz problem  
# take input from user
#if number divisible by 3 print FIZZ
#if number divisible by 5 print BUZZ
#if number divisible by 3 and 5 print FIZZBUZZ

'''
number = int(input('enter a number')) 

if number%3 == 0 and number%5==0:
    print('FizzBuzz') 

elif number%5 == 0:
    print('Buzz') 

elif number%3==0:
    print('Fizz') 

else:
    print(number)


# take input from user
# reverse that number
# 24354   o/p# 45342
# dont use string 

#by coverting into string
number = int(input('enter a number')) 
number = str(number) 
print(number[::-1])  

# direct reversing without conversion 


number = int(input('enter a number')) #24354
reversed_number = 0 

while (number>0):  
    remainder = number%10 # 4  5  3 4  2 
                     #  4534 *10  + 2 
    reversed_number= (reversed_number*10) + remainder
    # 45342
    number = number//10  #0
print(reversed_number)
'''
'''
    ___0___
 10) 2
    - 0
 __________
       2
'''
'''


def attendence ():   # function Defination
    print('Yes Mam') 

attendence() # Function call



def calculate_sum (num1 , num2): # former parameters
    res = num1+num2 
    return res 

data1 = int(input('Enter a number'))
data2 = int(input('Enter a number')) 

result = calculate_sum(data1 , data2) # actual parameters
print(result) 

result = calculate_sum(2, 3) 


def calculatesum(num1,num2):
    res = num1+num2
    return res 

data1= int(input('enter a number'))
data2= int(input('enter a number'))
print(calculatesum(data1 , data2)) 



x = 5
print( 'Hello')    #Hello

def print_lyrics(): 
   print ("I'm a lumberjack, and I'm okay.")
   print ('I sleep all night and I work all day.')

print ('Yo')     #Yo
print_lyrics()   #("I'm a lumberjack, and I'm okay.")
                 #'I sleep all night and I work all day.')
x = x + 2
print (x)        # 7



def printing123 ():
    print('hii im inside function') 
    return (True) 
    print('hii how are you') 

printing123()
print('hii im outside function') 


def calculate_sum (num1 , num2): # former parameters
    res = num1+num2 
    return (res) 

result = calculate_sum(4 , 5) # actual parameters
print(result * 3 ) 


data1 = 4
data2 = 5 
num1 = data1
num2 = data2
result = calculate_sum(num1, num2) 



def my_function(fname):
    print(fname +" References")
    
my_function("Emil")
my_function("Tobias")
my_function("Linus")



def my_function(*kids):
    print("Youngest Child is",kids[2])
    
my_function("Emil",'Tobias','linus') 

#Youngest Child is ('Emil', 'Tobias', 'linus') 


def my_function(child3, child2, child1):
    print("The youngest child is "+ child3)

my_function(child1 ="Emil", child2 ="Tobias", child3 ="Linus")


def my_function(**kid):
    print("my fav kid is "+ kid["child1"])
    
my_function(child1 ="Emil", child2 ="Tobias", child3 ="Linus")



def printname (name = 'Sneha'):
    print(name) 

printname('Shreya')

printname('Brijesh') 

printname() 

'''

import re


def fruits (fruit_list):
    for i in fruit_list:
        print(i) 

tropical='Kiwi'
fruits(tropical) 


# age to days 
# 2 yr = 365+365 = 730 days
# 10 yr = 365*10 = 3650 days 

def age_to_days (year):
    return year * 365 

print(age_to_days(2)) 

'''
 Create a function that takes a list of numbers lst and returns an inverted list.
 
     Examples
     invert_list([1, 2, 3, 4, 5]) ➞ [-1, -2, -3, -4, -5]
 
     invert_list([1, -2, 3, -4, 5]) ➞ [-1, 2, -3, 4, -5]
 
     invert_list([]) ➞ [] 
'''

def invert_list(lst):
    a = [] 
    for elem in lst:
        a.append(-elem) 
    return a 

print(invert_list([0]) ) 

# multiplication of number with another number and not to use * operator 
# multiplication (2 , 2)  4  
