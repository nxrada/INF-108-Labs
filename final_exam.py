#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Nicholas Kammerer
# INF 108 Final
# 08 December 2022


# In[65]:


def is_metric():
    user_input = input("Are inputs in metric or imperial? Enter: [M/I]")
    
    if (user_input == "M" or user_input == "m"):
        return True
    elif(user_input == "I" or user_input == "i"):
        return False
    else: 
        is_metric()
        


# In[72]:


def metric_bmi():
    weight = float(input("\nInput your weight in kilograms (kg): "))
    height = float(input("Input your height in centimeters (cm): "))
    
    height = height/100 # height in meters

    bmi = weight/(height ** 2)
    
    return round(bmi, 2)


# In[67]:


def imperial_bmi():
    weight = int(input("\nInput your weight in pounds (lbs): "))
    height = input("Input your height in feet,inches (ft,in): ")
    
    height = height.split(",")
    inches = int(height[0]) * 12
    inches = inches + int(height[1])

    bmi = (weight/(inches ** 2)) * 703
    
    return round(bmi, 2)
    


# In[85]:


def disclaimer():
    text = "BMI calculators do not diagnose body fatness or the health of individuals.\nIf you want to interpret the results, please consult the following webpage created by the CDC: \n\thttps://www.cdc.gov/healthyweight/assessing/bmi/index.html"
    
    return text


# In[79]:


def bmi_chart(bmi):
    chart = '''
           BMI          |  Weight Status  
         ---------------|------------------
           < 18.5       |  Underweight     
         ---------------|------------------  
           18.5 - 24.9  |  Healthy Weight
         ---------------|------------------
           25.0 - 29.9  |  Overwegiht
         ---------------|------------------
           > 30.0       |  Obese           
           
            '''
    print(F"\n\tYour BMI was calculated to be: {bmi}.\n")
    print("Reference table provided by the CDC:")
    print(chart)


# In[80]:


def bmi_calculator():
    # Greet user
    print("Welcome to BMI Calculator.")
    
    # Determine metric or imperial
    metric = is_metric()
    
    # Calculate BMI in metric or imperial. 
    if (metric):
        bmi_chart(metric_bmi())
    else:
        bmi_chart(imperial_bmi())
    
    # Print disclaimer text. 
    print(disclaimer())


# In[88]:


# Execute BMI program. 
bmi_calculator()

