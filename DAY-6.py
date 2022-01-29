# multiplication of number with another number and not to use * operator 
# multiplication (2 , 5)  10    

            #  2       5

'''
def multiply (num1 , num2):
    product=0                 #5
    for i in range (num1):    # (0,2)-0 1 
        product = product+num2 # 10

    return product

num1 = int(input('enter a number'))
num2 = int(input('enter a number'))
print(multiply(num1 , num2)) 

#Multiplication property of fractions : a/b/c = a×c/b 

def multiply_by_division (num1 , num2):
    prod = num1/(1/num2)
    return int(prod) 

print(multiply_by_division(2,5))

'''
'''
The Modulus Operator Function
Create a function that will work as the modulus operator % without using the modulus operator.
The modulus operator is a way to determine the remainder of a division operation.
Instead of returning the result of the division,
the modulo operation returns the whole number remainder.
Examples
mod(5, 2) ➞ 1
mod(218, 5) ➞ 3
mod(6, 3) ➞ 0 

Don't use the % operator to return the results.






def mod (num1 , num2):
    remainder = num1   #  0
    while remainder>=num2 :  #  3
        remainder=remainder - num2  # 6 - 3 = 3 - 3 = 0
    return remainder 

print(mod(6 , 3)) 


def getRemainder(num, divisor):
    Remain = num - divisor * (num//divisor) 
    return (Remain)
    
print(getRemainder(7, 2))
 

#dividend=quotient * divisor +remainder
# remainder = dividend - (quotient * divisor)
'''

'''
Reverse and Capitalize
Create a function that takes a string of lowercase characters and returns that string reversed and in upper case.
Examples
reverse_capitalize("abc") ➞ "CBA"
reverse_capitalize("hellothere") ➞ "EREHTOLLEH"
reverse_capitalize("input") ➞ "TUPNI"
'''
'''

def reverse_capitalize(str1):
    return  (str1[::-1]).upper()

print(reverse_capitalize("input")) 



str1 = 'hello' 
str1 = str1[::-1]
print(str1) 
'''

'''
In mathematics, an Arithmetic Progression (AP) is a sequence of numbers such that the 
difference between the consecutive terms is constant.

Create a function that takes three arguments:
The first element of the sequence first   a
Constant difference between the elements diff  d
Total numbers in the sequence n   n
Return the first n elements of the sequence with the given common difference diff.
Final result should be a string of numbers, separated by comma and space.
Examples
arithmetic_progression(1, 2, 5) ➞ "1, 3, 5, 7, 9"
arithmetic_progression(1, 0, 5) ➞ "1, 1, 1, 1, 1"
arithmetic_progression(1, -3, 10) ➞ "1, -2, -5, -8, -11, -14, -17, -20, -23, -26"
'''

#(a , d , n)  = (1 , 3 , 5)
# 1  4  7  10  13
'''
def ap(n,diff,freq):
    string=""           # 

    string+=str(n)      #  1

    for i in range(n,freq):#(1,5) 1 2 3 4
        n=n+diff            # 9
        string+=', '+str(n) #   1, 3, 5, 7, 9
    return string
print(ap(1,2,5))


def arithmetic_progression(a,d,n):
    current_value = a
    str1 = ''+str(a)
    for i in range(1,n):
        current_value = current_value + d 
        str1+=', '+str(current_value)
    return str1
 

print(arithmetic_progression(1, 2, 5))

def  AP(a,d,n):
    AP_lst = [a]        # [1]    
    for i in range(n-1):
        a = a+d            # 7
        AP_lst.append(a)   # [1 , 4 , 7 ,] 
    str1 = ', '.join([str(x) for x in AP_lst]) 
    return str1

print(AP(1,3,5)) 
''' 
'''
Create a function that takes a string as an argument and returns a coded 
(h4ck3r 5p34k) version of the string.

Examples
hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"
hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"
hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"
Notes
In order to work properly, the function should replace all 
"a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0, and "s"s with 5.

'''
'''


def hacker_speak(a_str):
    a_str = a_str.replace("a", "4")
    a_str = a_str.replace("e", "3")
    a_str = a_str.replace("i", "1")
    a_str = a_str.replace("o", "0")
    a_str = a_str.replace("s", "5")
    return(a_str)

print(hacker_speak("javascript is cool") )#j4v45cr1pt 15 c00l 


def hacker_speak(txt):
    hack = {'a':'4' , "e":'3','i':'1' , 'o':'0','s':'5'}

    new_str = ''

    for ch in txt:   #become a coder
        if ch in hack:
            new_str=new_str+hack[ch] 
        else:
            new_str += ch  # b3c0m3 4 c0d3r
    return new_str

print(hacker_speak("javascript is cool") )#j4v45cr1pt 15 c00l 

'''
'''
Union and Intersection of Lists
Create a function takes in two lists and returns an intersection list and a union list.
Intersection List: Elements shared by both.
Union List: Elements that exist in first or second list, or both (not exclusive OR).
While the input lists may have duplicate numbers, the returned intersection and union lists should be set-ified - that is, contain no duplicates. Returned lists should be sorted in ascending order.
List 1: [5, 6, 6, 6, 8, 9]
List 2: [3, 3, 4, 4, 5, 5, 8]
Intersection: [5, 8]
# 5 and 8 are the only 2 numbers that exist in both lists.
Union: [3, 4, 5, 6, 8, 9]
# Each number exists in at least one list.
Examples

intersection_union([1, 2, 3, 4, 4], [4, 5, 9]) ➞ [[4], [1, 2, 3, 4, 5, 9]]

intersection_union([1, 2, 3], [4, 5, 6]) ➞ [[], [1, 2, 3, 4, 5, 6]]

intersection_union([1, 1], [1, 1, 1, 1]) ➞ [[1], [1]]

Notes
Order of output should be: [Intersection], [Union].
Remember both output lists should be in ascending order.
Each input list will have at least one element.
If both lists are disjoint (share nothing in common), return an empty list [] for the intersection. 

[] []

intersection = [] 
union         = [] 

return    [intersection , union ]



'''
'''
def intersection_union(lst1 , lst2):
    union = set(lst1).union(set(lst2))
    intersection = set(lst1).intersection(set(lst2))

    return [sorted(intersection) , sorted(union)]

print(intersection_union([1, 2, 3, 4, 4], [4, 5, 9])) 

'''
#union 
lst1 = [1, 2, 3, 4, 4]
lst2=[4, 5, 9]
temp=[]
for i in lst1:
    if i not in temp:
        temp.append(i)
for i in lst2:
    if i not in temp:
        temp.append(i)
print(temp) 

intersection = [] 
for i in lst1:
    if i in lst2 and i not in intersection:
        intersection.append(i)

print(intersection)

intersection = [value for value in lst1 if value in lst2]


'''
find product (num1 , num2 , num3)
if num == 7 ignore it and ignore all numbers on left of it

(4 , 5 , 1) = 20   num1*num2*num3
(7 , 2 , 3) = 6    num2*num3
(5 , 7 , 4) = 4    num3
(4 , 5 , 7) = -1   -1
'''
def product(n1,n2,n3):
    if(n1==7):
        n1=1
        return n1*n2*n3
    if(n2==7):
        return n3
    if(n3==7):
        return -1
    return n1*n2*n3
print(product(7 ,7 ,7))


def multi_num (num1 , num2 , num3):
    new_multi = num1*num2*num3
    if num3 == 7:
        new_multi = -1
    elif num2 == 7:
        new_multi = num3
    elif num1 == 7:
        new_multi = num3*num2
    return new_multi

print(multi_num(7,7,7))


''' 
generate a list of 15 leap year 
find leap year 
year is divisible by 400
year is divisible by 4 and not divisible by 100 

find_leap_year(given_year)  # 2000 [2000,2004,2008]
'''


