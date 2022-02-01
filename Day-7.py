'''
# direct recursion 
def recurse():
    print ('hello world') 
    recurse() 

# indirect recursion 
def fun2():
    fun1()
def fun1 ():
    fun2() 


def fun1():
    print('Hello Function 2') 
    fun2() 

def fun2():
    print('Hello Function 1') 
    fun1() 

fun1() #RecursionError: maximum recursion depth exceeded while calling a Python object



def rec(n):     # n = 1
    #base case 
    if n == 1 :
        return 1 
    # recursive case
    else:
        return (n+rec(n-1))

print(rec(4)) 
# 4 + rec(3)  
#     3 + rec(2) 
#         2 + rec(1) 
#              1 

# Power (x,n) = x * Power (x , n-1) 

# Power(2 , 3) = 2 * power (2 , 2 ) 
#              =     2 * power (2 , 1) 
               #=        2 * power (2 , 0)
               #                1


# 6! = 1*2*3*4*5*6 = 720 
# while loop
def fact(n):  # n = 5
    ans=1     #1
    while(n>0):
        ans=ans*n  # 5*4*3*2*1
        n-=1 # 0
    return ans
print(fact(6)) 

#for loop
num=6
factorial =1
for i in range(1,num+1):
    factorial = factorial *i
print('The factorial of', num, 'is', factorial)


###Factorial recursive###
#base case        n == 1
#recursive case   n * fact(n-1) 

def fact(n): # n = 1
    if n==1 or n==0:
        return 1 
    else:
        return (n*fact(n-1))

print(fact(3))
# 3 * fact (2)
#     2 * fact(1)
#           1
'''
def printFun(test): #2
    if test<1:
        return 
    else:
        print(test, end= ' ')  # 3 2 1  
        printFun(test-1)       # printFun(3) 
        print(test , end=' ')  # 1 2 3
        return 

test = 3 
printFun(test) 
#3 2 1 1 2 3 

#printFun(3) 
 

