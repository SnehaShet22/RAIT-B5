#________STRING_________


'STRING' "STRING"

print('hello word')
print("hello word")

var = 'hello'
print(var) #hello # while printing variable dont use quotation marks
print("var") #var 

#    0 1 2 3 4 5 6 7 8 9 10111213
#a ='H e l l o   ,   W o r l d ! '
#                    -6-5-4-3-2-1
a = 'Hello , World!'

# INDEXING START FROM 0 
# SPACES HAVE INDEX TOO

print(a[5]) 

b = 'Aakankshya Sahoo'
print (b[13])
print (b[-3])

#len() function

print (len(b)) # also calculates empty space 

text = 'SPACES HAVE INDEX TOO'
print ('space' in text) #true/false ? #false becase space is in lowercase 
print ('SPACE' in text) #True because it is present in string
print ('EIN' in text) #False 
print ('E IN' in text) # True 


# NOT operator
print ('EIN' not in text) #True


# string slicing 

#    0 1 2 3 4 5 6 7 8 9 10111213
#a ='H e l l o   ,   W o r l d ! '
#                    -6-5-4-3-2-1
a = 'Hello , World!'
print(a[1:5]) # ello  [start : end : increment][0 : len(string) : 1]

print(a[:9]) # a[0:9]  #Hello , W  from start to end 

print(a[-6:-1]) # World  

print (a[:]) # whole string 
 

# BECAUSE OUR STRING IS IMMUTABLE WE CANNOT CHANGE OUR STRING
# BUT WE CAN MODIFY IT 

a = 'Hello , World!'
print(a.upper()) # HELLO , WORLD!

print(a.lower()) #hello , world! 
print(a.capitalize()) #Hello , world! 

#strip()  removes whitespaces or any character from start or end of string 

a = '       Hello , World!        ' 
print(a) 
print(a.strip()) 

a = ' Hello,World!' 
print(a) 
print(a.strip('!'))  # Hello***** ,**** World! 

# split() 

a = 'Hello,World!' 
print(a.split(","))  #['Hello', 'World!']

a = 'Hello,World!' 
print(a.split(","))  

a = 'Hello,World!' 
a = list(a)  #['H', 'e', 'l', 'l', 'o', ',', 'W', 'o', 'r', 'l', 'd', '!']
print(a) 

a = 'Hello,World!' 
print(a.split("o"))  # ['Hell' , ',W' ,'rld!' ]

'Hell      ,W        rld!' 

print(a.split("l"))

['He' ,'' ,'o,Wor' ,'d!']


b = 'SPACES HAVE INDEX TOO' 
print(a.split("E")) 

['SPAC','S HAV',' IND','X TOO']  


a = 'Sneha'
b = 'Shet' 
print ( a +' ' + b )  #Sneha Shet 

#format() 

age = 40 
print('My name is Anaya and my age is',age,'Its nice to meet you')

text = 'My name is Anaya and my age is {} Its nice to meet you'
print(text.format(age)) 

text = f'My name is Anaya and my age is {age} Its nice to meet you'
print(text) 


a = 'Hello,World!' 
a = a.replace(',','lalala')
print(a) 

a = 'Hello,World!' 
a = a.replace(',','') # to remove replace character with empty string 
print(a) 


#_____LIST______
                 #   0            1        2         3
my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple'] 
print(type(my_fav_fruits)) #<class 'list'> 
print(my_fav_fruits) 

print(len(my_fav_fruits)) #4

# you can add all kinds of data in list 
my_list = ['Kiwi' , 0 , 1 , 0.005 , True , False , [1 , 2 ,5],('Kiwi' , 0 , 1 , 0.005 , True , False ),{'p','k'}]

my_tuple=  ('Kiwi' , 0 , 1 , 0.005 , True , False , [1 , 2 ,5],('Kiwi' , 0 , 1 , 0.005 , True , False ),{'p','k'})
# use list constructor to convert any data type to list
my_list = list(my_tuple) 

my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple',  [1 , 2 ,5] ] 
print(my_fav_fruits[1]) # 'Apple'

print(my_fav_fruits[4][2]) # 5 
print(my_fav_fruits[-1][-1])  #5 

          #  0      1   2     3       4      5         6                       7                        8 
my_list = ['Kiwi' , 0 , 1 , 0.005 , True , False , [1 , 2 ,5],('kiwi' , 0 , 1 , 58 , True , False ),['hanna','sion'] ]

print(my_list[-1][-2]) #hanna
print(my_list[8][0])  #hanna

print(my_list[-1][0]) #hanna 

#slicing
print(my_list[1:6]) 

if 'kiwi' in my_list:
    print(True) 
else:
    print(False)   #False

# replacing element in list 

my_list[7] = 'string' 
print(my_list)      #['Kiwi', 0, 1, 0.005, True, False, [1, 2, 5], 'string', ['hanna', 'sion']] 


my_list[6:] = 'blueberry' # ['Kiwi', 0, 1, 0.005, True, False, 'b', 'l', 'u', 'e', 'b', 'e', 'r', 'r', 'y']
print(my_list) 

my_list[6:] = ['blueberry'] # ['Kiwi', 0, 1, 0.005, True, False, 'blueberry']
print(my_list) 


# insert(index , obj)   to add object at particular position
my_list.insert(4 ,'False') 
print(my_list)  #['Kiwi', 0, 1, 0.005, 'False', True, False, 'blueberry']

# remove takes object as an input
my_list.remove('False') #['Kiwi', 0, 1, 0.005, True, False, 'blueberry']

print(my_list)


# pop takes index value as an input
my_list.pop(5)  # ['Kiwi', 0, 1, 0.005, True, 'blueberry']
print(my_list)


# add elements at the end of list 
# .append(obj)

my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple'] 
my_fav_fruits.append('blueberry') 
print(my_fav_fruits)      # ['Strawberry', 'Apple', 'Kiwi', 'Apple', 'blueberry']


my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple'] 
my_fav_fruits.append(['blueberry','blackberry']) 
print(my_fav_fruits)    #['Strawberry', 'Apple', 'Kiwi', 'Apple', ['blueberry', 'blackberry']]


# extend function

my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple'] 
my_fav_fruits.extend(['blueberry','blackberry']) 
print(my_fav_fruits)   #['Strawberry', 'Apple', 'Kiwi', 'Apple', 'blueberry', 'blackberry']


print(my_fav_fruits.count('Apple')) #2 

print(my_fav_fruits.count('kiwi'))   # 0 if that element not in list 


print(my_fav_fruits.index('Apple')) # 1  return index of 1st time apple occured

my_fav_fruits.append(('blueberry','blackberry')) 
print(my_fav_fruits)  #['Strawberry', 'Apple', 'Kiwi', 'Apple', 'blueberry', 'blackberry', ('blueberry', 'blackberry')]

print(my_fav_fruits.index(('blueberry','blackberry')))



my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple'] 
my_fav_fruits.reverse()
print(my_fav_fruits)  #['Apple', 'Kiwi', 'Apple', 'Strawberry']  

my_fav_fruits.sort() 
print(my_fav_fruits) #['Apple', 'Apple', 'Kiwi', 'Strawberry'] 

my_fav_fruits.sort(reverse=True)  
print(my_fav_fruits)  #['Strawberry', 'Kiwi', 'Apple', 'Apple']


my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple'] 
my_fav_fruits.clear()
print(my_fav_fruits)  #[]  



my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple'] 
fruit_list = my_fav_fruits   # both are pointing to same list

print(my_fav_fruits) #['Strawberry', 'Apple', 'Kiwi', 'Apple']
print(fruit_list)    #['Strawberry', 'Apple', 'Kiwi', 'Apple']

my_fav_fruits[1] = 'Papaya' 

print(my_fav_fruits) #['Strawberry', 'Papaya', 'Kiwi', 'Apple']
print(fruit_list)    #['Strawberry', 'Papaya', 'Kiwi', 'Apple']  fruit list also changed 


print(id(fruit_list))    #2080487371136
print(id(my_fav_fruits)) #2080487371136 





my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple'] 
fruit_list = my_fav_fruits.copy()  # ['Strawberry', 'Apple' , 'Kiwi' , 'Apple'] 

my_fav_fruits[1] = 'Papaya'  
print(my_fav_fruits)  #['Strawberry', 'Papaya', 'Kiwi', 'Apple']
print(fruit_list)     # ['Strawberry', 'Apple', 'Kiwi', 'Apple'] 

print(id(fruit_list))    #1681855620224
print(id(my_fav_fruits)) # 1681855572480


#                    0           1         2         3         4 
my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple', (1 , 2 , 3)]  

my_fav_fruits[2:] 


list_1 = [1,2,3,4,5,6] 

print(max(list_1), min(list_1)) 
#         6            1 

del list_1[2] 
print(list_1)  # [1, 2, 4, 5, 6]


#When we use del keyword , we have to be careful since we can delete whole list with del keyword


# pop () example 
my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple', (1 , 2 , 3)]  
my_fav_fruits.pop() # remove last element

print(my_fav_fruits)

my_fav_fruits = ['Strawberry', 'Apple' , 'Kiwi' , 'Apple']  
my_fav_fruits.pop(1) # remove index element

print(my_fav_fruits) #['Strawberry', 'Kiwi', 'Apple'] 