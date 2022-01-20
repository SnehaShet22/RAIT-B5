'''
#
#
void main()
{
    printf('');
}
'''

print('Hello world')  

print("Hello world")  

a=4
b=5
if a>b:
    print('a is greater than b') 
else:
    print('b is greater than a') 


var_name = 6   # assigigned 6 to variable
print(type(var_name)) #<class 'int'>

var_name = 6.58
print(type(var_name)) #<class 'float'>

var_name = 'String'
print(type(var_name)) #<class 'str'>


var_name = '6.58'
print(type(var_name))  #<class 'str'>

var_name='''
udhfb
bsdhbj
hfdjf
'''
print(type(var_name)) 





5
6
'string'

# comments 
# we use '#' for single line comment 
'''
we use triple quotes for
multiline
comment 
'''


string1 = '566' 
# type casting 
integer1 = int(string1)
print(string1)
print(type(string1))
print(integer1) 
print(type(integer1))

# type casting 
# int , float to string 
# int to float or vice versa

'''
string1 = 'Sneha' 
integer1 = int(string1)# invalid literal for int() with base 10: 'Sneha'
''' 

# string to integer,float (we need to maake sure that our string is a number)

string1 = '566' 
z = float(string1)
print(z)# 566.0

# you can get the datatype of variable with 
# type()  function

a = 4 
A = 'Sally' 
print(a) #4
print(A) #Sally

# python is case-sensitive so the above code will create 2 different variables 

no_of_tickets = 5 
no_of_people = 7 
if no_of_tickets>= no_of_people:
    print("you can go inside") 
else:
    print('not enough tickets')

a = 5 
b = 7 
if b>=a:
    print("you can go inside") 
else:
    print('not enough tickets')

noofpeople  = 0 
# camelCase 
noOfPeople = 0 

# PascalCase 
NoOfPeople = 0 

# snake_case 
no_of_people = 0 


print123 = 5 
print(print123) # NOT TO USE RESERVED WORDS

complex1 = 2 + 5j 

print(complex1) #(2+5j) 

x= 5 
y = 5

z = complex(x,y) #(5+5j)
print(z)


x = 5 
y = 10

print(x+y) 
print(x-y) 
print(x*y)
print(x/y) #(10/5)=2  quotient 
print(x//y)  # only print integer value (5//10)=0 

print(x%y) # (10%5)=0 remainder
print(x**y) # x raised to y 

'''
  __2__  # quotient
5) 10
-  10
_______
   0   # remainder
'''

x = 5 
y = 10 

if x==y : 
    print('they are equal') 

if x!=y : 
    print('they are not equal') 

if x > y:
    print('x is greater')  

if x < y :
    print('x is smaller') 

if x >= y:
    print('x is greater or equal')  

if x <= y :
    print('x is smaller or equal') 

'''
AND 
0 0  0
0 1  0
1 0  0
1 1  1

OR
0 0  0
0 1  1
1 0  1
1 1  1 

NOT 
0  1 
1  0
'''

# get input from user 
'''
input_var = input('enter a number :') # by default takes input as string
print(input_var) 

input_var = input('enter a number :') 
input_var = int(input_var) # type casting
print(input_var) 
'''
input_var = int(input('enter a number :')) # by default takes input as string
print(input_var) 