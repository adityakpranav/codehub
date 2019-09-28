
# stat: problem with upper pal of 999 -> 1001

 # num  : 999
 # first: 99
 # num1 : 999
 # num2 : 10001
 # num3 : 989

 # num  : 984
 # first: 98
 # num1 : 989
 # num2 : 999
 # num3 : 979
# 989
# 979


import math

def minimum_distance(cmp,*num):
    min = math.inf
    for i in num:
        if abs(cmp-min) >= abs(cmp - i):
            min = i
    return min
    
    
def makePall(num,overlap):
    
    ans = num
    
    if overlap == 1:
    #    overlap = (math.floor(math.log(num,10) if(num>9) else 1)) -1
        num = num//(10)
    #print('num : ',overlap)
    while(num!=0):
        ans = ans*10 + num%10
        num = num//10
    return ans
     


def convert(num):
    
    int_list = str(num)

    mid = (len(int_list)-1)//2
    
    first =  int(''.join(int_list[:mid+1]))
 
    if len(int_list)%2!=0:
        
        num1 = makePall(first,overlap = 1)
        num2 = makePall(first+1,overlap = 1)
        num3 = makePall(first-1,overlap = 1)
        # print('its odd length')
    else:
        num1 = makePall(first,overlap = 0)
                
        if first%10 == 9:
            
            num2 = makePall(first+1,overlap = 1)
            num3 = makePall(first-1,overlap = 0)
            
        if first%10 == 0:
            num2 = makePall(first+1,overlap = 0)
            num3 = makePall((first*10)-1,overlap = 1)
        # print('its even length')
            
            
    print("\n num  : %d\n first: %d\n num1 : %d\n num2 : %d\n num3 : %d"%(int(num),first,num1,num2,num3))
    if int(num) == num1:
        return(minimum_distance(int(num),num2,num3))
    else:
        return(minimum_distance(int(num),num1,num2,num3))
 

op = []
# num_cases = int(input())
# for _ in range(num_cases):
    # op.append(convert(input()))

op.append(convert('999'))
op.append(convert('984'))


for i in op:
    print(i)
