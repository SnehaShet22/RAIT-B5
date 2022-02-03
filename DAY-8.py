'''
def check_leap_year (year):
    list1 = []
    while(len(list1)<15):  # len
        if (year%400==0):
            list1.append(year) 
        elif (year % 4 ==0 and year%100 !=0):
            list1.append(year) 
        year+=1
    return list1 

print(check_leap_year(int(input('enter a year'))))



def leap_year(yr):
    list1=[]

    if (yr%400 ==0) or ((yr%100!=0) and (yr%4==0)):
        list1.append(yr)
        print("yes")
    
    else:
        print("no")  
print(leap_year(2016))


def leap_years(given_year):
    count=0
    list_of_leap_years=[]
        
    while(count<15):
        if given_year%4==0 or (given_year%400==0 and given_year%100!=0):
            list_of_leap_years.append(given_year)
            count+=1
        given_year+=1
    return list_of_leap_years

list_of_leap_years=leap_years(2000)
print(list_of_leap_years)


################LAMBDA FUNCTIONS############# 
# for anonymous functions we use lambda keyword 
#syntax 

# lambda arguments  :  expression  

def double (x):
    x = x*2 
    return x 
dog = double   # passed my function to variable
print(dog(5))




def double (x):
    x = x*2 
    return x 
print(double(5))

double = lambda x : x * 2 
print(double(15)) 


x = lambda a , b : a + b 
print(x(50,10)) 

multiply = lambda a , b : a*b 
print(multiply(5,15))  


def myfun(n):
    return lambda a : a*n 

mom = myfun(5)   #mom = lambda a : a*n 
print(mom(63)) 

def myfun(n):
    return lambda a : a*n 

mydoubler = myfun(2) # lambda a : a*2
mytripler = myfun(3) # lambda a : a*3

print(mydoubler(4))
print(mytripler(5)) 


# filter () 
# filter (function , sequence) 
# return an iterator  

def fun(variable):
    letters = {'a','e','i','o','u'} 
    if variable in letters:
        return True
    else:
        return False 
           #[T,  F,  T ,  F, T  , F  F   F   F   T   F]
sequence = ['i','l','o','v','e','p','y','t','h','o','n'] 
          # fun(o)  #ioe
filtered_word = filter(fun , sequence) 

print(filtered_word) #<filter object at 0x000001852E8DC100>
#method 1
for i in filtered_word:
    print(i) 

#method2 

filtered_word = list(filter(fun , sequence) )
print(filtered_word) 
'''

seq = [0,1,2,3,5,8,13] 

result = filter(lambda x : x%2 != 0, seq)
print(list(result)) 

result = filter(lambda x : x%2 == 0, seq)
print(list(result)) 