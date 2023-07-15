# -*- coding: utf-8 -*-
"""
Created on Sat Jul  15 17:38:13 2023

@author: chanon.h
"""

# The Goal for this code are want to play mini game take sticks from the pile with computer.

# SET All Sticks in pile and comfirm quatity of sticks.
st_all = int(input('How many sticks (N) in the pile: '))
print("There are ",st_all," sticks in the pile.")

# SET User name.
user_name = str(input('What is your name : '))
print("\n")

# SET and IMPORT random fucntion
import random
random_number = random.randint(1, 2)

# Check condition and calculation.(Human Player)
while st_all > 0 :
    
    st_take = int(input(user_name + ",how many sticks you will take (1 or 2):"))
    
    if st_take >= 3 :
        print("No you cannot take more than 2 sticks!")
        print()
        
    elif st_take <= 0 :
        print("No you cannot take less than 1 skick!")
        print()
    
    elif (st_all - st_take) < 0 :
        print("Threr are no enough sticks to take.")
        print("\n")
    
    elif (st_all - st_take) > 0 :
        st_all = st_all - st_take
        print("There are ",st_all," sticks in the pile.")
        print("\n")
        
    else :
        st_all = st_all - st_take
        print(user_name + ", take the last stick")
        print("\n")
        print("I, smart computer, win")
    
 # Check condition and calculation.(Computer Player)     
    if st_take >= 3 :
        print()
        
    elif st_take <= 0 :
        print()
    
    elif st_all > 0 :
        st_pc_take = random_number
        while st_pc_take > st_all :
           st_pc_take = random_number 
            
        if (st_all - st_pc_take) > 0 :
            print("I, smart computer, take : " + str(st_pc_take))
            st_all = st_all - st_pc_take
            print("There are " + str(st_all) + " sticks in the pile.")
            print("\n")
            
        else :
            st_all = st_all - st_pc_take
            print("I, smart computer, takes the last stick.\n")
            print(user_name + " win (I, smart computer, am sad T_T)")
            
        

        
    
        
        