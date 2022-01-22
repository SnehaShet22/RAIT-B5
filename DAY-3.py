
'''
thistuple = ('apple','banana','cherry') 
print(thistuple[1]) 

print(len(thistuple))  


\'''
To create atuple with only one element you need to write comma after an item,otherwise python will not recognise it as a tuple
\''' 

fruit = ('apple') 

print(type(fruit))  #<class 'str'>

number = (10)  
print(type(number)) # <class 'int'>


fruit = ('apple',) 

print(type(fruit))  #<class 'tuple'>

fruit = () 
print(type(fruit)) 

#tuple() 

fruit = ['apple','banana','cherry'] 
print(fruit)
fruit = tuple(fruit ) 
print(fruit) 

# cant change values in tuple 
# but there is a workaround 

#1. covert tuple into list and add elements 
thistuple = ('apple','banana','cherry') 
thislist = list(thistuple) 
thislist.append('pomogranate')
thistuple=tuple(thislist) 

print(thistuple) 

#2. use of + operator
#thistuple = ('apple','banana','cherry') 

#thistuple = thistuple + ('pomogranate')  # can only concatenate tuple (not "str") to tuple

#print(thistuple) 

thistuple = ('apple','banana','cherry') 

thistuple = thistuple + ('pomogranate',)  #('apple', 'banana', 'cherry', 'pomogranate')

print(thistuple) 


# if we want to insert element at particular index 
thistuple = ('apple','banana','cherry') 

thistuple = thistuple[0:1] + ('pomogranate',) +  thistuple[1:] 
print(thistuple)  #('apple', 'pomogranate', 'banana', 'cherry')

fruit = ('apple','banana','cherry') 

(green , yellow , red) = fruit 

print(green) #apple
print(yellow) #banana
print(red) #cherry

\'''
fruit = ('apple','banana','cherry','pomogranate','blueberry','blackberry','raspberry','golden berry') 

(green , yellow , red) = fruit 

print(green) #ValueError: too many values to unpack (expected 3)
print(yellow) 
print(red) 
\''' 

fruit = ('apple','banana','cherry','pomogranate','blueberry','blackberry','raspberry','golden berry') 

(green , yellow , *red) = fruit 

print(green) #apple
print(yellow) # banana
print(red)    #['cherry', 'pomogranate', 'blueberry', 'blackberry', 'raspberry', 'golden berry']


fruit = ('apple','banana','cherry','pomogranate','blueberry','blackberry','raspberry','golden berry') 

(green , *yellow , red , blue ) = fruit 

print(green) # apple
print(yellow) # ['banana', 'cherry', 'pomogranate', 'blueberry', 'blackberry', 'raspberry']
print(red)    #golden berry


fruit = ('apple','banana','cherry') 

mytuple = fruit*2 #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
print(mytuple) 

list1 = ['hi']*4 
print(list1)    #['hi', 'hi', 'hi', 'hi']  

#empty list
fruit = ['apple','banana','cherry'] 
fruit.clear()
print(fruit)  #[]

# empty tuple 
fruit = () 
print(type(fruit)) 

emptytuple = ()

#________set_____________

fruit = {'apple','banana','cherry','apple'} 

print(fruit) #{'apple', 'cherry', 'banana'}

print(len(fruit))# 3

fruit = {'apple'} 
print(type(fruit)) #<class 'set'> 

#{} is not empty set its empty dictionary
thisset = {}
print(type(thisset) ) #<class 'dict'>


thisset = set() #empty set
print(type(thisset))   #<class 'set'>  

set1 = {'abc',34 , True ,54.5} 

fruit = {'apple','banana','cherry','apple'} 

#if 'banana' in fruit :
#    print('banana')

# adding elements in set
#  add() 
fruit = {'apple','banana','cherry','apple'} 
fruit.add('orange')
print(fruit)  #{'orange', 'cherry', 'banana', 'apple'}

# update()
# object in update() does not have to be a set , it can be any iterable tuple , lists or dictionary
fruit = {'apple','banana','cherry','apple'} 
tropical = {'pinapple','papaya','blueberry'} 

fruit.update(tropical) 

print(fruit) #{'apple', 'blueberry', 'banana', 'pinapple', 'papaya', 'cherry'}

print(tropical)   #{'papaya', 'blueberry', 'pinapple'}


fruit = {'apple','banana','cherry','apple'} 
tropical = ['pinapple','papaya','blueberry']

fruit.update(tropical) 

print(fruit) #{'apple', 'blueberry', 'banana', 'pinapple', 'papaya', 'cherry'}

print(tropical)   #{'papaya', 'blueberry', 'pinapple'}


#remove item
# remove will raise error if we provide element which is not present in set
# discard will *not* raise error if we provide element which is not present in set and will return orginal set without changes
#1. remove()

fruit = {'apple','banana','cherry'} 
fruit.remove('banana')
print(fruit) #{'cherry', 'apple'}

#2. discard ()
fruit = {'apple','banana','cherry'} 
fruit.discard('banana')
print(fruit) # {'cherry', 'apple'}


\'''
fruit = {'apple','banana','cherry'} 
fruit.remove('Banana') #KeyError: 'Banana'
print(fruit) 
\'''

fruit = {'apple','banana','cherry'} 
fruit.discard('papaya')
print(fruit) # {'apple', 'cherry', 'banana'}

#pop() 
fruit = {'pomogranate','apple','banana','cherry'} 
x = fruit.pop() 
print(x) 

print(fruit) 

fruit.clear() 
print(fruit) #set() 
print(type(fruit)) #<class 'set'>

fruit = {'pomogranate','apple','banana','cherry'} 
fruit.discard('banana') 

#union() = will return new set , existing set will remain same no changes
set1 = {'a','b','c'}
set2 = {'1','2','3'} 

set3 = set1.union(set2) 
print(set3)
print(set1)
print(set2)
'''
# combining two sets and removing duplicates

#update() 
import this


set1 = {'a','b','c'}
set2 = {'1','2','3'} 

set1.update(set2) #set1 will get updated
print(set1)
print(set2) #no changes in set2


set1 = {'a','b','c'}
set2 = {'1','2','3'} 

set2.update(set1) # set2 gets updated
print(set1) ##no changes in set1
print(set2) 


# keep ONLY duplicates 

x = {'apple','banana','cherry'} 
y = {'google','microsoft','apple'} 
x.intersection_update(y) 

print(x)  #{'apple'}

#intersection
x = {'apple','banana','cherry','google'} 
y = {'google','microsoft','apple'} 
z = x.intersection(y) 

print(z)  #{'apple'} 

# keep all but NOT duplicates
#symmetric difference 

x = {'apple','banana','cherry','google'} 
y = {'google','microsoft','apple'} 
z = x.symmetric_difference(y) 

print(z)   

#symmetric difference update

x = {'apple','banana','cherry','google'} 
y = {'google','microsoft','apple'} 
x.symmetric_difference_update(y) 
print(x)   


#difference 
#returns set that contains items existing only in set x and not in y
# return item in set x which are not in set y
x = {'apple','banana','cherry'} 
y = {'google','microsoft','apple'} 
z = x.difference(y) 

print(z)  #{'cherry', 'banana'}

# elements of y which does not exist in x
x = {'apple','banana','cherry'} 
y = {'google','microsoft','apple'} 
z = y.difference(x) 

print(z)  #{'google', 'microsoft'}


x = {'apple','banana','cherry','google'} 
y = {'google','microsoft','apple'} 
x.difference_update(y) 
print(x)   #{'cherry', 'banana'}

#Returns whether two sets have a intersection or not
# returns true if no elements of x is present in y 

x = {'apple','banana','cherry','google'} 
y = {'google','microsoft','apple'}  
print(x.isdisjoint(y)) #False

#Returns whether another set contains this set or not
# return true if all elements of x are present in set y 
x = {'a','b','c'}
y = {'a','c','x','y','z','p','q','r','b'} 

print(x.issubset(y))# true 


print(y.issuperset(x))# true 

#_____dictionary _______
# no duplicates in key but for values we can have duplicates
thisdictionary = {
    'brand' : 'ford' ,
    'model' : 'ford',
    'year' : 1964 ,
    'year' : 2020 ,
    'colour': ['red','white','blue']
}
print(thisdictionary)#{'brand': 'ford', 'model': 'ford', 'year': 2020, 'colour': ['red', 'white', 'blue']}

print(thisdictionary['brand']) #ford
print(thisdictionary['year']) #2020

print(len(thisdictionary))#3

print(type(thisdictionary))#<class 'dict'>


# ACCESSING DICTIONARY ITEMS 

#1. dictionaryName[key]
thisdictionary = {
    'brand' : 'Ford' ,
    'model' : 'Mustang',
    'year' : 2020 ,
    'colour': ['red','white','blue']
}
print(thisdictionary['brand']) #Ford

#2. get() 

print(thisdictionary.get('model')) #Mustang


#key() 

print(thisdictionary.keys()) #dict_keys(['brand', 'model', 'year', 'colour'])

#values()

print(thisdictionary.values()) #dict_values(['Ford', 'Mustang', 2020, ['red', 'white', 'blue']])

# items() for both key and value

print(thisdictionary.items())
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020), ('colour', ['red', 'white', 'blue'])])


if 'model' in thisdictionary:
    print('yes') 
else:
    print('no')


# change values of list  if the values did not exist , it will just create new key value

thisdictionary['brand'] ='Ford123'
print(thisdictionary)
#{'brand': 'Ford123', 'model': 'Mustang', 'year': 2020, 'colour': ['red', 'white', 'blue']}

thisdictionary.update({'year':2022})
print(thisdictionary)

#{'brand': 'Ford123', 'model': 'Mustang', 'year': 2022, 'colour': ['red', 'white', 'blue']}

thisdictionary.update({'myfavmodel':'Ford'})
print(thisdictionary)
#{'brand': 'Ford123', 'model': 'Mustang', 'year': 2022, 'colour': ['red', 'white', 'blue'], 'myfavmodel': 'Ford'}


thisdictionary['myfavEdition'] ='Ford456'
print(thisdictionary) 

#{'brand': 'Ford123', 'model': 'Mustang', 'year': 2022, 'colour': ['red', 'white', 'blue'], 'myfavmodel': 'Ford', 'myfavEdition': 'Ford456'} 