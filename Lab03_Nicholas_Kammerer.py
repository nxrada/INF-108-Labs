#!/usr/bin/env python
# coding: utf-8

# In[4]:


active_program = ["1. Pick a language.", "2. Read the doctumentation.", "3. Write your first program.", "4. Learn git.", "5. Publish your program using git.", "6. Write some more programs", "7. Upload them using git.", "8. Get hired as a FAANG software engineer."]

print(active_program)
#1.1. "1. Pick a language.", "2. Read the doctumentation.", "3. Write your first program.", "4. Learn git.", "5. Publish your program using git.", "6. Write some more programs", "7. Upload them using git.", "8. Get hired as a FAANG software engineer."2


# In[ ]:


print(active_program[0])
#1.2. Pick a language


# In[5]:


print (active_program[:3])
#1.3. ['1. Pick a language.', '2. Read the doctumentation.', 
#     '3. Write your first program.']


# In[6]:


print(active_program[3:8])
#1.4. ['4. Learn git.', '5. Publish your program using git.', '6. Write some more programs', 
#     '7. Upload them using git.', '8. Get hired as a FAANG software engineer.']


# In[7]:


active_program.append("9. Look at tutorials.")
active_program.append("10. Watch movies about programmers.")


print(active_program)
#1.5. ['1. Pick a language.', '2. Read the doctumentation.', '3. Write your first program.', '4. Learn git.', 
#     '5. Publish your program using git.', '6. Write some more programs', '7. Upload them using git.', 
#    ' 8. Get hired as a FAANG software engineer.', '9. Look at tutorials.', '10. Watch movies about programmers.'


# In[8]:


active_program.insert(0, "1/2. Desire to learn.")
active_program.insert(1, "3/4. Commitment to learning.")

print(active_program)
#1.6. ['1/2. Desire to learn.', '3/4. Commitment to learning.', '1. Pick a language.', '2. Read the doctumentation.', '3. Write your first program.', '4. Learn git.', '5. Publish your program using git.', '6. Write some more programs', '7. Upload them using git.', '8. Get hired as a FAANG software engineer.', '9. Look at tutorials.', '10. Watch movies about programmers.']


# In[9]:


active_program[9] = "9. Watch tutorials online."

print(active_program)
#1.7. ['1/2. Desire to learn.', '3/4. Commitment to learning.', '1. Pick a language.', '2. Read the doctumentation.', '3. Write your first program.', '4. Learn git.', '5. Publish your program using git.', '6. Write some more programs', '7. Upload them using git.', '9. Watch tutorials online.', '10. Watch movies about programmers.']


# In[11]:


del(active_program[10])

print(active_program)

#1.8. ['1/2. Desire to learn.', '3/4. Commitment to learning.', '1. Pick a language.', '2. Read the doctumentation.', '3. Write your first program.', '4. Learn git.', '5. Publish your program using git.', '6. Write some more programs', '7. Upload them using git.', '9. Watch tutorials online.']


# In[14]:


del(active_program[0])

print(active_program)

#1.9. '3/4. Commitment to learning.', '1. Pick a language.', '2. Read the doctumentation.', '3. Write your first program.', '4. Learn git.', '5. Publish your program using git.', '6. Write some more programs', '7. Upload them using git.', '9. Watch tutorials online.'


# In[17]:


print(active_program[0])

#1.10. 1. Pick a language.


# In[18]:


print(active_program)

#1.11. ['1. Pick a language.', '2. Read the doctumentation.', '3. Write your first program.', '4. Learn git.', '5. Publish your program using git.', '6. Write some more programs', '7. Upload them using git.', '9. Watch tutorials online.']


# In[19]:


print(active_program[0:3])

#1.12.['1. Pick a language.', '2. Read the doctumentation.', '3. Write your first program.']


# In[23]:


new_list = active_program[0:]

print(new_list)

#1.13. ['1. Pick a language.', '2. Read the doctumentation.', '3. Write your first program.', '4. Learn git.', '5. Publish your program using git.', '6. Write some more programs', '7. Upload them using git.', '9. Watch tutorials online.']


# In[24]:


del(new_list[0:1])
new_list.remove("9. Watch tutorials online.")
new_list.remove("7. Upload them using git.")

new_list
#1.14. ['2. Read the doctumentation.',
#      '3. Write your first program.',
#      '4. Learn git.',
#      '5. Publish your program using git.',
#      '6. Write some more programs']


# In[26]:


print("commitment to learning" in new_list)


#1.15. False


# In[45]:


id = [100, 108, 124, 131, 171, 197]
topic = ["Information in the 21 Century","Programming for Problem Solving","Cybersecurity Basics", "Intro to Data Analytics", "eSports & Digital Gaming Ecosystem", "Mini Special Topic in Informatics"]

#2.1.


# In[28]:


id.sort()

#2.2.


# In[29]:


topic.sort()
#2.3.


# In[36]:


id.sort(reverse=True)
#2.4.


# In[37]:


topic.sort(reverse=True)

#2.5.


# In[44]:


topic.sort()
topic
#2.6. The list cannot be unsorted as the data type containing the list was overwritten
#     by the sort funciton. 


# In[56]:


print("Course ID\tCourse topic")
for i in range(len(id)):
    print(str(id[i]) + "\t\t" + topic[i])

#2.7. 
# Course ID    Course topic
# 100          Information in the 21 Century
# 108          Programming for Problem Solving
# 124          Cybersecurity Basics
# 131          Intro to Data Analytics
# 171          eSports & Digital Gaming Ecosystem
# 197          Mini Special Topic in Informatics


# In[47]:


id_tuple = (100, 108, 124, 131, 171, 197)
topic_tuple = ("Information in the 21 Century","Programming for Problem Solving","Cybersecurity Basics", "Intro to Data Analytics", "eSports & Digital Gaming Ecosystem", "Mini Special Topic in Informatics")

#3a.


# In[50]:


for i in range(len(id_tuple)):
    print(F"Welcome to CINF {id_tuple[i]}!")

#3b. Welcome to CINF 100!
#    Welcome to CINF 108!
#    Welcome to CINF 124!
#    Welcome to CINF 131!
#    Welcome to CINF 171!
#    Welcome to CINF 197!


# In[51]:


id_tuple.append(200)
topic_tuple.append("Research Methods for Informatics")

#3c. This code throws an error, as tuples are immutable and therefora cannot be added to.


# In[52]:


del(id_tuple[5])
del(topic_tuple[5])

#3d. "TypeError: 'tuple' object doesn't support item deletion." 
# Tuples are immutable, and therefore cannot be changed. 


# In[55]:


print("Course ID\tCourse topic")
for i in range(len(id_tuple)):
    print(F"{id_tuple[i]}\t\t{topic_tuple[i]}")
    
#3e. 
# Course ID    Course topic
# 100          Information in the 21 Century
# 108          Programming for Problem Solving
# 124          Cybersecurity Basics
# 131          Intro to Data Analytics
# 171          eSports & Digital Gaming Ecosystem
# 197          Mini Special Topic in Informatics


# In[57]:


Faculty1 = {}

Faculty1

#4.1.


# In[64]:


Faculty2 = {
    "name",
    "last_name",
    "job_title",
    "email",
}

#4.2.


# In[95]:


Faculty3 = {
    "name":"Jennifer",
    "last_name":"Goodall",
    "job_title":"Vice Dean",
    "email":"jgoodall@albany.edu",
}

#4.3.


# In[96]:


Faculty1.update(name="Martha")
Faculty1.update(last_name="Avila")
Faculty1.update(job_title="Informatics Lecturer")
Faculty1.update(email="mavilamaravilla@albany.edu")

#4.4.


# In[97]:


Faculty2 = {
    "name":"Robert",
    "last_name":"Griffin",
    "job_title":"Dean of the CEHC",
    "email":"rpgriffin@albany.edu",
}

#4.5.


# In[100]:


Faculty1.update(office="tbd")
    
#4.6.


# In[101]:


Faculty1.update(office="ETEC 350")

#4.7.


# In[102]:


del(Faculty1["office"])

#4.8.


# In[103]:


print(Faculty1["last_name"])

#4.9. Avila


# In[98]:


def dean_info():
    fn = Faculty2["name"]
    ln = Faculty2["last_name"]
    title = Faculty2["job_title"]
    email = Faculty2["email"]
    print(F"The {title} is {fn} {ln}. Their email is {email}.")

dean_info()
#4.10. The Dean of the CEHC is Robert Griffin. Their email is rpgriffin@albany.edu.


# In[107]:


print(Faculty1)
Faculty2.keys()
Faculty3.values()
Faculty1.items()

for i in enumerate(Faculty1.items()):
    print (i)
#4.11.


# In[109]:


Faculty2.get("name")

#4.12. 'Robert'


# In[110]:


Faculty1.update(alma_mater=["Universidad de las Americas-Puebla", "University of Bologna"])


#5a.


# In[115]:


Faculty2.update(alma_mater=None)
Faculty2["alma_mater"] = ["University of Massachusetts, Amherst", "Virginia Tech"]

#5b.


# In[118]:


faculty3_alma_mater = ["Tufts University", "University at Albany"]
Faculty3.update(alma_mater="faculty3_alma_mater[]")

#5c. 


# In[ ]:




