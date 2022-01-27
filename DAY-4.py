#LOOPS 
# IF ELIF ELSE 
'''
a = 33 
b = 200

if b > a: 
    print ('b is greater than a') 
else:
    print ('b is smaller than a')  



a = 33 
b = 33

if b > a: 
    print ('b is greater than a') 
else:
    print ('b is smaller than a')  


a = 33 
b = 33

if b > a: 
    print ('b is greater than a')
elif b == a:
    print ('b is equal to a')  
else:
    print ('b is smaller than a')   


#shortcut if only one statement in if or elif or else block
a = 33 
b = 330

if b > a:print ('b is greater than a') 
elif b == a:print ('b is equal to a')  
else:print ('b is smaller than a')   


# AND will print True only if ALL conditions are true otherwise FALSE
a = 200 
b = 33
c = 500
a , b , c = 200 , 33 , 500 
#    t        f 
if a > b and a > c:
    print('a is greatest number')  
else:
    print('a is not greatest number')  



# OR will print True if ATLEAST ONE condition is true otherwise FALSE
a = 200 
b = 33
c = 500
a , b , c = 200 , 33 , 500 
#    t        f 
if a > b or a > c:
    print('a is greatest number')  
else:
    print('a is not greatest number')  


# nested if 

x = 41 

if x > 10:
    print('Above 10')
    if x > 20:
        print('and also above 20!')
    else:
        print('but not above 20....')


x = 20 
if x > 20:
    pass 

def engine():
    pass 

a = 33 
b = 330

if b > a:print ('b is greater than a') 
elif b == a:print ('b is equal to a')  
else:print ('b is smaller than a')   

print('b') if b > a else print ('=') if b == a else print ('a')   

#  While loop 

i = 1 
while i < 6:   
    print(i)   # 1 2 3 4 5
    i += 1  # i=i+1  2 3 4 5 6
print('done printing') 

l = ['a','b',1,2,3]  # l[0] , l[1]
i = 0 
while i < len(l): # 5
    print (l[i]) # a b 1 2 3
    i +=1 # 1 2 3 4 5

l = ['apple','pomogranate'] 
i = 0 
while i < 5 :
    print (l)
    i = i+1

# break and continue 

i = 1
while i < 6 :
    print(i) # 1 2 3 
    if i==3:
        break
    i += 1   # 2 3 

i = 1
while i < 6 :
    if i==3:
        break
    print(i) # 1 2 
    i += 1   # 2 3 

# continue 

i = 0 
while i < 6:
    i = i+1  # 1 2 3 4 5 6
    if i==3:
        continue
    print (i)  # 1 2 4 5 6 

i=0
while i < 6:   
    print(i)  
    i += 1 
print('i no longer less than 6') 

# for loop 
#                                           i

fruits = ['apple','pomogranate','kiwi','pineapple'] 
for fruit in fruits:
    print (fruit) 


fruits = ['apple','pomogranate','kiwi','pineapple'] 
i = 1
for i in range(0 , i+1):
    print(fruits[i]) 


for i in 'banana':
    print(i)

fruits = ['apple','pomogranate','kiwi','pineapple'] 
for fruit in fruits:
    if fruit == 'kiwi':
        break
    print(fruit)
    
fruits = ['apple','pomogranate','kiwi','pineapple'] 
for fruit in fruits:
    if fruit == 'kiwi':
        continue
    print(fruit)


# range() 

for i in range(2 , 6):
    print(i)  #2 3 4 5 

# (start , end , increment)
# (0 , user , 1) 

for i in range(0, 16 , 5):
    print(i)  # 0 5 10 15

#                     i 
fruits = ['apple','pomogranate','kiwi','pineapple']
#           j
colors = ['red','pink','green','yellow']

for i in fruits: # apple
    for j in colors : #red pink
        print(i , j) 
# apple red 
# apple pink 

# print all numbers from 1 to 10 (10 inclusive) 

i=1
while(i<11): # i<=10
	print(i)
	i=i+1

for i in range(1 ,11):
    print(i)
  
# print even numbers till n , n is input of user 

n = int(input('enter a number')) 
# n included
# 0 2 4 6 8 10 
for i in range(0 ,n+1 , 2):
    print(i) 

for i in range(0,n+1):
    if (i%2==0):
        print(i)

for i in range(0,n+1):
        print(i)
        i = i+2 

n = int(input())
for i in range (0,n,2):
    print(i)      

n = int(input()) 
i = 0 
while i <= n:
    print(i)
    i = i + 2 

# odd numbers
n = int(input())
for i in range (1,n,2):
    print(i)      

n = int(input()) 
i = 1
while i <= n:
    print(i)
    i = i + 2 



# sum of even numbers from 0 to n , n is input by user.

n = int(input()) 
sum = 0
for i in range (0 , n+1 , 2):
    sum = sum + i 
print(sum) 


n=int(input('Enter no: '))
i = 0
sum=0
while i <=n: # Using while  
    sum=sum+i
    i += 2
print(sum)


# sum of 1st n odd numbers 
# 5  1+3+5+7+9 = 25 
#2   1 + 3 = 4 

n = int(input()) 
print(n**2) 

n = int(input('Enter a number')) # 5
sum=0                          #0
for i in range(1, n+n, 2): # 1 10 2
    sum=sum+i               # 1+3+5+7+9
print(sum)


# sum of 1st n even numbers 
#5 = 0+2+4+6+8= 20

n = int(input('Enter a number')) # 5
sum=0
for i in range(0, n+n, 2): #(0 , 10 , 2)
    sum=sum+i              # 0+2+4+6+8
print(sum)
'''
n=int(input("Enter n value:"))#5
print((n-1)*n) 

# the fizz buzz problem  
# take input from user
#if number divisible by 3 print FIZZ
#if number divisible by 5 print BUZZ
#if number divisible by 3 and 5 print FIZZBUZZ


# take input from user
# reverse that number
# 24354   o/p# 45342
# dont use string 