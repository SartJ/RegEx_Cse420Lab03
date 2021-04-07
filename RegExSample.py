# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:30:05 2021

@author: sartaj
"""
import re


print('''
Please copy paste the input at once and as it is in the 
lab question with similar pattern of line breaks.

Example:-
3
[a-c]{3}cab+(da)*f
db*a[^def]{2}gh
def[k-p]*p+
5
defkmnpmpp
acbcabbf
pqrstdd
dbaabggh
dbbbbamkgh

Input:
''')
data= input()  

data2= data.splitlines()    #a list with each line in each index

# print(data2)

pattern_list = [] # here will store the lines which are the RE patterns

matcher_list = [] # here will store the lines which has to be matched 

num1 = int(data2[0])    # separating the number of patterns
num2 =int(data2[num1 + 1])  # separating the number of matchers

# print(num1,num2)

# This loop builds the pattern_list
for i in range(num1):
    # print('sup', i)
    pattern_list.append(data2[i+1])

# print(pattern_list)

# This loop builds the matcher_list
for i in range(num2):
    matcher_list.append(data2[num1+i+2])
    
# print(matcher_list)

#This does the matching and prints the outputs:-
for i in matcher_list:
    
    chk = 0
    for j in pattern_list:
        pattern = re.compile(r'{}'.format(j))
        # matches = pattern.finditer(j)
        
        result = re.match(pattern, i)
        if result:
            print("YES,", pattern_list.index(j)+1)
            chk = 1
            
            
    if chk == 0:
        print("No,",0)
            
            
   
