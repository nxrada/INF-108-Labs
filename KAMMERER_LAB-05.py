#!/usr/bin/env python
# coding: utf-8

# In[19]:


# LAB 05 

# ONE
def pass_check():
    password = input("Please enter your password.")
    aevans_pass = "angelina23"
    error = "Error: incorrect password. Call 1-800-TECH-SUPPORT or \
    attempt to log in after 30 minutes."

    if (password == aevans_pass):
        print("Welcome Angelina Evans.")
    else: 
        print(error)


pass_check()


# In[45]:


# TWO

def leapyear():
    year = 2164
    leap_year = False
    divisible_by_hundred = int(year)%100==0        
    divisible_by_four = int(year)%4==0  
    divisible_by_fh = int(year)%400==0
    if (divisible_by_four == False):   
        leap_year = False
    elif (divisible_by_hundred == False):
        leap_year = True
    elif (divisible_by_fh == False):
        leap_year = False
    else:
        leap_year = True
    
    if (leap_year):
        print(F"{year} is a leap year!")
    else:
        print(F"{year} is not a leap year.")
    
leapyear()


# In[15]:


# THREE

def letter_grade(grade):
    
    error_statement = "Grade out of bounds."
    letter = ""
    
    if (grade < 0 or grade > 100):
        print(error_statement)
    else:
        if (grade >= 94):
            letter = "A"
            return letter
        if (grade >= 89):
            letter = "A-"
            return letter
        if (grade >= 85):
            letter = "B+"
            return letter
        if (grade >= 82):
            letter = "B"
            return letter
        if (grade >= 79):
            letter = "B-"
            return letter
        if (grade >= 76):
            letter = "C+"
            return letter
        if (grade >= 73):
            letter = "C"
            return letter
        if (grade >= 70):
            letter = "C-"
            return letter
        if (grade >= 67):
            letter = "D+"
            return letter
        if (grade >= 64):
            letter = "D"
            return letter
        if (grade >= 60):
            letter = "D-"
            return letter
        if (grade <= 59):
            letter = "E"
            return letter
grade = int(input("Input grade (0-100)."))

print("Your letter grade is " + str(letter_grade(grade)) + ".")


# In[17]:


# FOUR

# First letter of first name in upper case
# First letter of last name in upper case

import random as r

def generate_id(fn, ln):
    rand = r.randrange(100000, 999999)

    fn.title()
    ln.title()
    
    uid = fn[0]+ln[0]+str(rand)
    return uid


first = input("Enter first name.")
# first = ""  # Alternative input method.
last = input("Enter last name.")
# last = ""  # Alterative input method. 

print(F"User ID: {generate_id(first, last)}")


# In[79]:


# FIVE
# Count Vowels - Enter a string and the program 
#     counts the number of vowels in the text. 
# For added complexity have it report a sum of each vowel found.

def eval_word():
    print("This program evaluates words.\n")
    word = input("Enter word to be evaluated.")
    vowels = ["a", "e", "i", "o", "u"]
    
    # List data structure to save information about vowels. 
    v_count = [0, 0, 0, 0, 0, 0]
    
    # Counts vowels.
    for i in range(len(word)):
        item = word[i]
        if item in vowels:
            if item == vowels[0]:
                v_count[0] = v_count[0]+1
            elif item == vowels[1]:
                v_count[1] = v_count[1]+1
            elif item == vowels[2]:
                v_count[2] = v_count[2]+1
            elif item == vowels[3]:
                v_count[3] = v_count[3]+1
            elif item == vowels[4]:
                v_count[4] = v_count[4]+1
            else:
                continue
            
    # Counts consonants. 
    for i in range(len(word)):
        item = word[i]
        if item not in vowels:
            v_count[5] = v_count[5]+1
    
    # Prints function output.
    print("\nWord Analysis:")
    print(F"Length\t\t {str(len(word))}")
    for i in range(len(vowels)):
        print(F"{vowels[i]}\t\t {v_count[i]}")
    print(F"Consonants\t {v_count[5]}")
    

eval_word()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




