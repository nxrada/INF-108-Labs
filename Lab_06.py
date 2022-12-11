#!/usr/bin/env python
# coding: utf-8

# In[12]:


# ONE 
def c_to_f(cel):
    float(cel)
    far = (cel*(9/5))+32
    return round(float(far), 2)

def f_to_c(far):
    float(far)
    cel = (far-32)*5/9
    return round(float(cel), 2)

print(f_to_c(32))

print(c_to_f(0)) 


# In[1]:


# Two

def g_to_oz(g):
    float(g)
    oz = g/28.35
    return round(float(oz), 2)

def oz_to_g(oz):
    float(oz)
    g = oz*28.35
    return round(float(g), 2)

print(g_to_oz(28))

print(oz_to_g(1))


# In[ ]:


# Three

def ml_to_floz(ml):
    float(ml)
    floz = ml/29.574
    return round(float(floz), 2)

def floz_to_ml(floz):
    float(floz)
    ml = floz*29.574
    return round(float(ml), 2)

print(ml_to_floz(8))

print(floz_to_ml(16))


# In[35]:


# Four
def temp_conv():
    choice = input("Please enter 'F' if you want to convert from fahrenheit to centigrade. Enter 'C' if you want to convert from centigrade to fahrenheit.")
    if (choice == "C"):
        cel = float(input("\bPlease enter the degrees in celsius: "))
        print(F"\n{cel}° centigrade is equivalent to {c_to_f(cel)}° fahrenheit.")
    elif (choice == "F"):
        far = float(input("\nPlease enter the degrees in fahrenheit:"))
        print(F"\n{far}° fahrenheit is equivalent to {f_to_c(far)}° centigrade.")
        
    else:
        print("\nIncorrect input.\n")
        temp_conv()
        
temp_conv()


# In[73]:


##### Bonus
import math as m
def cone_volume():
    r = float(input("\nInput cone radius: "))
    h = float(input("\nInput cone height: "))
    v = round(m.pi*r*r*(h/3), 2)
    print(F"\nVolume of a given cone with radius '{r}' and height '{h}': {v}.")
    
    
def cone_sa():
    # A = pi * r (r + sqrt(h^2+r^2))
    r = float(input("\nInput cone radius: "))
    h = float(input("\nInput cone height: "))
    a = round(m.pi*r*(r+m.sqrt(m.pow(h,2)+m.pow(r,2))), 2)
    print(F"\nSurface Area of a given cone with radius '{r}' and height '{h}': {a}.")

def cone_fx():
    choice = input("Please enter 'V' to find the volume of a given cone. \
Enter 'S' to find the surface area.")
    if (choice == "V"):
        cone_volume()
    elif (choice == "S"):
        cone_sa()
    else:
        print("\nIncorrect input.\n")
        cone_fx()

        
cone_fx()

