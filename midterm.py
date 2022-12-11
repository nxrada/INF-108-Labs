#!/usr/bin/env python
# coding: utf-8

# In[1]:


#
# QUESTION 01
#

x = 72198.7654 # Assign float to be rounded.

round(x, 2) # Round float using builtin method. 


# In[2]:


#
# QUESTION 02
#

x = 72198.7654 # Assign float to be rounded.

round(x, -2) # Round float using builtin method. 


# In[3]:


#
# QUESTION 03
#

x = 12  # Assign float to be converted. 

str(float(x))  # Convert to float and then to string. 


# In[4]:


#
# QUESTION 04
#

x = 12.252  # Assign float to be converted. 

int(x)  # Convert to int. 


# In[6]:


#
# QUESTION 05
#

x = False  # Assign bool datatype to x. 

type(x) # Test x data type. 


# In[7]:


#
# QUESTION 06
#
solar_bodies = ("Mars", "Venus", "Jupiter", "Earth", "Sirius", "Orion", "Sun")  # Assign values to tuple.

type(solar_bodies)  # Test solar_bodies data type. 


# In[11]:


#
# QUESTION 07
#

orbital_bodies = ["Mars","Venus","Jupiter","Earth","Sirius","Orion","Sun"]  # Create list.


# In[31]:


#
# QUESTION 08
#

def lower(listy):  # Define method
    new_listy = [item.lower() for item in listy]  # Create new list with lowered case. 
    return new_listy  # Return lowered list. 

lower(orbital_bodies)  # Execute function. 


# In[33]:


#
# QUESTION 09
#

orbital_bodies.sort()  # Sorts lists by ascending order. 

print(orbital_bodies)  # Prints sorted list. 


# In[43]:


#
# QUESTION 10
#

planets = []  # Create empty list planets
stars = []  # Create empty list stars

planets = [orbital_bodies[0], orbital_bodies[1], orbital_bodies[2],
           orbital_bodies[6]]  # Fill list by indexing planets.

stars = [orbital_bodies[3], orbital_bodies[4], orbital_bodies[5]]  # Fill list by indexing stars. 

print(planets, stars)  # Print filled lists. 


# In[61]:


#
# QUESTION 11
#

fav_star = input("What is your favorite star? Available choices: Orion, Sirius, Sun.")  # Accept input.


# In[64]:


#
# QUESTION 12
#

def test(t_val, listy):  # Function to test if value is in list.
    return t_val in listy  

test(fav_star, stars)  # Function being executed. 


# In[66]:


#
# QUESTION 13
#

print(F"You've selected {fav_star} as your favorite star.")  # Print F function. 


# In[67]:


#
# QUESTION 14
#

#  If fav_star is in list, return a nice saying, else return you don't know.
if (fav_star == "Orion"):  
    print("Nice! Orion is cool!")
elif (fav_star == "Sirius"):
    print("Awesome! I love Sirius!")
elif (fav_star == "Sun"):
    print("The Sun! She keeps us warm <3.")
else:
    print("Sorry... I don't know that star.")


# In[ ]:


#
# QUESTION 15
#

#  If fav_star is in list, return a nice saying, else return you don't know.
if (fav_star == "Orion"):  
    print("Nice! Orion is cool!")
elif (fav_star == "Sirius"):
    print("Awesome! I love Sirius!")
elif (fav_star == "Sun"):
    print("The Sun! She keeps us warm <3.")
else:
    print("Sorry... I don't know that star.")


# In[72]:


#
# QUESTION 16
#

fast_food = {  # Create nested dictionary. 
    "Wendys":{
        "name":"Wendys",
        "address":"123 Main Street",
        "favorite_food":"burger",
        "price":"cheap"
        },
    "McDonalds":{
        "name":"McDonalds",
        "address":"199 Main Street",
        "favorite_food":"fries",
        "price":"cheap"
        },
    "Burger_King":{
        "name":"Burger King",
        "address":"188 Main Street",
        "favorite_food":"chicken nuggets",
        "price":"expensive"
        }
}


# In[82]:


#
# QUESTION 17
#

print("One of my favorite restaurants is " + fast_food[Wendys[0].value()]


# In[ ]:


#
# QUESTION 18
#

print("I have been to these fast-food restaruants:


# In[88]:


#
# QUESTION 19
#

fast_food.update(last_visit="date")
fast_food


# In[74]:


#
# QUESTION 20
#

quote = "Nothing great was ever achieved without enthusiasm."

quote.split()

