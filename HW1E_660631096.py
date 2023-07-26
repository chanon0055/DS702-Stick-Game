# -*- coding: utf-8 -*-
"""
Created on Sat Jul  15 17:38:13 2023

@author: chanon.h
"""
# Import function from library.
import random

# Create function to Setup sticks in pile and player name.
def setup_stp_pname():
    global st_all, user_name
    st_all = int(input('How many sticks (N) in the pile: '))
    print("There are ",st_all," sticks in the pile.")
    user_name = str(input('What is your name : '))
    print("\n")

# Crate Function condition and calculation.(Human Player)
def player_turn():
    global st_take, st_all
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
    

            
# Crate Function condition and calculation.(AI Mode)
def com_ai_mode_turn():
    global st_all, magic_number, check_magic_num, st_ai_take
    random_number = random.randint(1, 2)
    magic_number = (st_all-1)%3
    if st_take not in [1,2] :
        print()    
    elif magic_number != 0 :
            st_ai_take = 2
            check_magic_num = ((st_all-st_ai_take)-1)%3
            if check_magic_num != 0:
                st_ai_take = 1
            else:
                st_ai_take = 2
            st_all = st_all - st_ai_take
            print("I take " + str(st_ai_take) +" sticks There are " + str(st_all) + " sticks in the pile.")
            print("\n")
    elif magic_number == 0 and st_all > 1:
            st_ai_take = random_number
            st_all = st_all - st_ai_take
            print("I take " + str(st_ai_take) +" sticks There are " + str(st_all) + " sticks in the pile.")
            print("\n")
    else :
            st_all = st_all - st_ai_take
            print("AI, takes the last stick.")
            print(user_name + " win (AI sad T_T)")
            
st_take = 1
setup_stp_pname()
while st_all > 0:
    com_ai_mode_turn()
    if st_all > 0:
        player_turn()

    
