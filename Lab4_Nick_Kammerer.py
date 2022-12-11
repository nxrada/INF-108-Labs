#!/usr/bin/env python
# coding: utf-8

# In[103]:


#  Declaration of lists
mara = {
    "name":"Martha",
    "last_name":"Avila",
    "job_title":"Informatics Lecturer",
    "email":"mavilamaravilla@albany.edu",
    "alma_mater":["Universidad de las Americas-Puebla", "University of Bologna"],
    "office":"TBD"
}
robg = {
    "name":"Robert",
    "last_name":"Griffin",
    "job_title":"Dean of the CEHC",
    "email":"rpgriffin@albany.edu",
    "alma_mater":["University of Massachusetts, Amherst", "Virginia Tech"],
    "office":"TBD"
}
jeng = {
    "name":"Jennifer",
    "last_name":"Goodall",
    "job_title":"Vice Dean",
    "email":"jgoodall@albany.edu",
    "alma_mater":["Tufts University", "University at Albany"],
    "office":"TBD"
}

#  Checks key consistency. 
def check(key1, key2):
    return key1.keys() == key2.keys()

check(mara, robg)
check(robg, jeng)

#  Prints all info in list. 
for username, user_info in users.items():
    print("Username: " + username)
    print("\tProfessor " + " " + str(user_info['last_name'])+ "." +\
            "\n\tTheir office is at " + str(user_info['office']) + "." +\
            "\n\tTheir job title is " + str(user_info['job_title']) + "." +\
            "\n\tTheir email is " + str(user_info['email']) + "." +\
            "\n\tThey studied at the following Universities: " + str(user_info['alma_mater']) + ".")
    
#. Prints office location of all professors. 
for username, user_info in users.items():
    print("The office of Professor " + user_info["last_name"] +\
          " is " + user_info["office"] + ".")
    
#  EXERCISE ONE


# In[104]:


states = ["Alabama","Alaska","Arizona","Arkansas","California", 
          "Colorado", "Connecticut", "Delaware","Florida","Georgia","Hawaii",
          "Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky",
          "Louisiana","Maine","Maryland","Massachussetts","Michigan",
          "Minnesota","Mississippi", "Missouri","Montana","Nebraska","Nevada","New Hampshire",
          "New Jersey","New Mexico","New York","North Carolina","North Dakota",
          "Ohio","Oklahoma","Oregon","Pennslyvania","Rhode Island","South Carolina",
          "South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington",
          "West Virginia","Wisconsin","Wyoming"]

capitals = ["Montgomery","Juneau","Phoenix","Little Rock","Sacramento","Denver","Hartford",
           "Dover","Tallahassee","Atlanta","Honolulu","Boise","Springfield","Indianapolis",
           "Des Moines","Topeka","Frankfort","Baton Rouge","Augusta","Annapolis","Boston",
           "Lansing","Saint Paul","Jackson","Jefferson","Helena","Lincoln","Carson","Concord",
           "Trenton","Santa Fe","Albany","Raleigh","Bismarck","Columbus","Oklahoma","Salem",
           "Harrisburg","Providence","Columbia","Pierre","Nashville","Austin","Salt Lake",
           "Montpelier","Richmond","Olympia","Charleston","Madison","Cheyenne"]

print(list(enumerate(states, 1)))
#  (32, "New York") (32, "Albany")


print(list(enumerate(capitals, 1)))
#  (1, "Alabama") (1, "Montgomery")

#  EXERCISE TWO


# In[88]:


import time
for state in states:
    print(state, end=" state.\n")
    time.sleep(0.04) #  Sleep function delaying code by 2 seconds (2/50 = 0.04 aka 40ms).
for city in capitals:
    print(city, end=" city.\n")
    time.sleep(0.04) #  Sleep function delaying code by 2 seconds (2/50 = 0.04 aka 40ms)

# EXERCISE THREE


# In[98]:


states_and_capitals = dict(zip(states, capitals)) 
print(states_and_capitals, 1)

#  EXERCISE FOUR 


# In[112]:


for state, city in states_and_capitals.items():
    print(F"The city of {city} is the capital of {state} state.")

# EXERCISE FIVE

