# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:04:24 2023

@author: chanon.h
"""

# The Goal for this code are want to check Sticks in pile.

# SET All Sticks in pile and comfirm quatity of sticks.
st_all = int(input('How many sticks (N) in the pile: '))
print("There are ",st_all," sticks in the pile.")

# SET User name.
user_name = str(input('What is your name : '))
print("\n")

# SET intial time for success calculation.
time = 0

# Check condition and calculation.
while st_all > 0 :
    
    st_take = int(input(user_name + ",how many sticks you will take (1 or 2):"))
    
    if st_take >= 3 :
        print("No you cannot take more than 2 sticks!")
            
    elif st_take <= 0 :
        print("No you cannot take less than 1 skick!")
    
    elif (st_all - st_take) < 0 :
        print("Threr are no enough sticks to take.")
    
    elif (st_all - st_take) > 0 :
        st_all = st_all - st_take
        print("There are ",st_all," sticks in the pile.")
        time += 1
        
    else :
        st_all = st_all - st_take
        time += 1
        print("OK.There is no stick left in the pile.You spent " + str(time) +" times.")