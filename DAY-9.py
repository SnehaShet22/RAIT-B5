#MAP 
# returns an iterator 
# map (fun , seq)
# you can pass one or more iterable 
'''
def addition(n):
    return n + n 

numbers = (1,2,3,4) 
result = map(addition , numbers) 
print(result)  #<map object at 0x00000248FAFE6D70> 

print(list(result)) #[2, 4, 6, 8] 

result = map(lambda n : n+n , numbers)   


number1 = [1 , 2 , 3]
number2 = [4 , 5 , 6]

result = map(lambda x , y:x+y , number1 , number2)

for i in result:
    print(i) 

print(list(result)) 


l = ['sat','bat','cat','mat']

test = map(list , l) 
print(list(test))  #[['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]

#list() 

number1 = [1 , 2 , 3] 
squared_numbers = list(map(lambda x : x*x , number1)) #converted to list
print(squared_numbers)
'''
'''
total = 2 
4 * 5 = 20 
 21 
fiveneeded = 0 
oneneeded = 0 
fiveneeded = (rupees to make / 5)  
oneneeded = (rupees to make % 5)

check if fiveneeded <= five you have and oneneeded <= one you have :
print(fiveneeded , oneneeded) 

fiveneeded > five you have:
total =  five you have*5 
oneneeded = rupees to make - total 
'''
                #    28            4        10
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0 

    five_needed = rupees_to_make//5  # 5 
    one_needed = rupees_to_make % 5  # 3

    if five_needed <= no_of_five and one_needed <=no_of_one:
        print(five_needed , one_needed) 
    
    elif five_needed > no_of_five:
        total = no_of_five * 5   # 20
        one_needed = rupees_to_make - total   # 28 - 20 = 8 
        if one_needed<=no_of_one:
            print(no_of_five , one_needed) 
        else:
            print(-1) 
    else:
        print(-1)

make_amount(28 , 4 ,10)  # 5 3 

# 25
 
def change(five,one,price):
    f=price//5
    o=price%5
    sum=0
    coins=0
    if(f<=five and o<=one):
         return f,o   
    else:
        return -1
    
print(change(3,3,13))

'''
Distance in kms must be greater than 0.
Quantity ordered should be minimum 1.

if foodtype == V  , bill+= 120 * quantity , 
if foodtype == N  , bill+= 150 * quantity , 

''' 

def bill(type,quantity,dist):
    if(quantity<1 or dist<1):
        return -1
    bill=0
    if(type=='N'):
        bill+=150*quantity
        
    elif(type=='V'):
        bill+=120*quantity

    if(dist<=3):
        return bill

    elif(dist<=6): 
        bill+=(dist-3)*3 

    else: 
        bill+= ((dist - 6)*6)+9 

    return bill
print(bill('V',2,4))

# 3 = 0 
# 4 = 0 + 1*3 =(4-3)*3 


