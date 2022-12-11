#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 121981.2298001

str(x)
#  1A. "121981.2298001"


# In[2]:


x = 121981.2298001

int(x)
#  1B. 121981


# In[8]:


x = 121981.2298001

round(x, 3)
#  1C. 121981.23


# In[9]:


x = 121981.2298001

round(x, -3)
#  1D. 122000.0


# In[11]:


x = "I'm learning \'basic\' Python."

print(x)
#2A. I'm learning 'basic' Python.


# In[3]:


x = """FALL 2020\n
\tCHM 120\n
\tCHM 124\n
\tENG 240Z\n
\tMAT 100\n
\tECE 110\n
\tFSP 100\n
\tUNI 110\n
\nSPRING 2021\n
\tMAT 108\n
\tMAT 112\n
\tPSY 101\n
\tSPN 100\n
SUMMER 2021\n
\tCSI 201\n
FALL 2021\n
\tPHI 112\n
\tCSI 210\n
\tCSI 213\n
SPRING 2022
\tART 110\n
\tART 115\n
\tINF 100X\n
\tINF 124x\n
SUMMER 2022\n
\tAFS 213\n
\tHIS 250\n
\tPHI 112\n
FALL 2022\n
\tINF 108\n
\tINF 201\n
\tINF 202\n
\tINF 301\n
"""

print(x)
# 2B. FALL 2020

#       CHM 120

#       CHM 124

#       ENG 240Z

#       MAT 100

#       ECE 110

#       FSP 100

#       UNI 110


#SPRING 2021

#       MAT 108

#       MAT 112

#       PSY 101

#       SPN 100

#SUMMER 2021

#       CSI 201

#FALL 2021

#       PHI 112

#       CSI 210

#       CSI 213

#SPRING 2022
#       ART 110

#       ART 115

#       INF 100X

#       INF 124x

#SUMMER 2022

#       AFS 213

#       HIS 250

#       PHI 112

#FALL 2022

#       INF 108

#       INF 201

#       INF 202

#       INF 301


# In[7]:


x = """FALL 2020\n
\tCHM 120\n
\tCHM 124\n
\tENG 240Z\n
\tMAT 100\n
\tECE 110\n
\tFSP 100\n
\tUNI 110\n
\nSPRING 2021\n
\tMAT 108\n
\tMAT 112\n
\tPSY 101\n
\tSPN 100\n
SUMMER 2021\n
\tCSI 201\n
FALL 2021\n
\tPHI 112\n
\tCSI 210\n
\tCSI 213\n
SPRING 2022
\tART 110\n
\tART 115\n
\tINF 100X\n
\tINF 124x\n
SUMMER 2022\n
\tAFS 213\n
\tHIS 250\n
\tPHI 112\n
FALL 2022\n
\tINF 108\n
\tINF 201\n
\tINF 202\n
\tINF 301\n
"""
print(x.upper())
#2C. FALL 2020
#
#	CHM 120
#
#	CHM 124
#
#	ENG 240Z
#
#	MAT 100
#
#	ECE 110
#
#	FSP 100
#
#	UNI 110
#
#
#SPRING 2021
#
#	MAT 108
#
#	MAT 112
#
#	PSY 101
#
#	SPN 100
#
#SUMMER 2021
#
#	CSI 201
#
#FALL 2021
#
#	PHI 112
#
#	CSI 210
#
#	CSI 213
#
#SPRING 2022
#	ART 110
#
#	ART 115
#
#	INF 100X
#
#	INF 124X
#
#SUMMER 2022
#
#	AFS 213
#
#	HIS 250
#
#	PHI 112
#
#FALL 2022
#
#	INF 108
#
#	INF 201
#
#	INF 202
#
#	INF 301


# In[8]:


x = """FALL 2020\n
\tCHM 120\n
\tCHM 124\n
\tENG 240Z\n
\tMAT 100\n
\tECE 110\n
\tFSP 100\n
\tUNI 110\n
\nSPRING 2021\n
\tMAT 108\n
\tMAT 112\n
\tPSY 101\n
\tSPN 100\n
SUMMER 2021\n
\tCSI 201\n
FALL 2021\n
\tPHI 112\n
\tCSI 210\n
\tCSI 213\n
SPRING 2022
\tART 110\n
\tART 115\n
\tINF 100X\n
\tINF 124x\n
SUMMER 2022\n
\tAFS 213\n
\tHIS 250\n
\tPHI 112\n
FALL 2022\n
\tINF 108\n
\tINF 201\n
\tINF 202\n
\tINF 301\n
"""
print(x.lower())
#2d. fall 2020

#	chm 120

#	chm 124

#   eng 240z

#	mat 100

#	ece 110

#	fsp 100

#	uni 110


#spring 2021

#	mat 108

#	mat 112

#	psy 101

#	spn 100

#summer 2021

#	csi 201

#fall 2021

#	phi 112

#	csi 210

#	csi 213

#spring 2022
#	art 110

#	art 115

#	inf 100x

#	inf 124x

#summer 2022

#	afs 213

#	his 250

#	phi 112

#fall 2022

#	inf 108

#	inf 201

#	inf 202

#	inf 301
​


# In[9]:


x = """FALL 2020\n
\tCHM 120\n
\tCHM 124\n
\tENG 240Z\n
\tMAT 100\n
\tECE 110\n
\tFSP 100\n
\tUNI 110\n
\nSPRING 2021\n
\tMAT 108\n
\tMAT 112\n
\tPSY 101\n
\tSPN 100\n
SUMMER 2021\n
\tCSI 201\n
FALL 2021\n
\tPHI 112\n
\tCSI 210\n
\tCSI 213\n
SPRING 2022
\tART 110\n
\tART 115\n
\tINF 100X\n
\tINF 124x\n
SUMMER 2022\n
\tAFS 213\n
\tHIS 250\n
\tPHI 112\n
FALL 2022\n
\tINF 108\n
\tINF 201\n
\tINF 202\n
\tINF 301\n
"""

print(x.title())
# 2E. Fall 2020

#	Chm 120

#	Chm 124

#   eng 240Z

#	Mat 100

#	Ece 110

#	Fsp 100

#	Uni 110


#Spring 2021

#	Mat 108

#	Mat 112

#	Psy 101

#	Spn 100

#Summer 2021

#	Csi 201

#Fall 2021

#	Phi 112

#	Csi 210

#	Csi 213

#Spring 2022
#	Art 110

#	Art 115

#	Inf 100X

#	Inf 124X

#Summer 2022

#	Afs 213

#	His 250

#	Phi 112

#Fall 2022

#	Inf 108

#	Inf 201

#	Inf 202

#	Inf 301


# In[11]:


x = """Python uses whitespace indentation, rather than curly brackets or keywords,
to delimit blocks. An increase in indentation comes after certain statements.
It's a sign that the current block will end if the indentation decreases. Thus,
the program's visual structure accurately represents its semantic structure.
The recommended indent size is four spaces."""

print ("visual" in x)
# 3A. True


# In[12]:


x = """Python uses whitespace indentation, rather than curly brackets or keywords,
to delimit blocks. An increase in indentation comes after certain statements.
It's a sign that the current block will end if the indentation decreases. Thus,
the program's visual structure accurately represents its semantic structure.
The recommended indent size is four spaces."""

print ("Visual" in x)
# 3B. False


# In[15]:


x = """Python uses whitespace indentation, rather than curly brackets or keywords,
to delimit blocks. An increase in indentation comes after certain statements.
It's a sign that the current block will end if the indentation decreases. Thus,
the program's visual structure accurately represents its semantic structure.
The recommended indent size is four spaces."""

print ("program" in x)
# 3C. True


# In[16]:


x = """Python uses whitespace indentation, rather than curly brackets or keywords,
to delimit blocks. An increase in indentation comes after certain statements.
It's a sign that the current block will end if the indentation decreases. Thus,
the program's visual structure accurately represents its semantic structure.
The recommended indent size is four spaces."""

print ("accur" in x)
# 3D. True


# In[19]:


fn = input("Input first name: ")
ln = input("Input last name: ")
age = input("Input age: ")

print("Hello " + fn + " " + ln + " are you " + age + " years old?") 
# 4A. Hello Nick Kammerer are you 20 years old?


# In[25]:


fn = input("Input first name: ")
ln = input("Input last name: ")
age = input("Input age: ")

print("Hello, %s %s. Are you %s years old?" % (fn, ln, age))
#4B. Hello, Nick Kammerer. Are you 20 years old?


# In[27]:


fn = input("Input first name: ")
ln = input("Input last name: ")
age = input("Input age: ")

print(F"Hello, {fn} {ln}. Are you {age} years old?")
#4C. Hello, Nick Kammerer. Are you 20 years old?


# In[28]:


c_year = 2022
fn = input("Input first name: ")
ln = input("Input last name: ")
age = input("Input age: ")
year = c_year - int(age)

print(F"Hello, {fn} {ln} are you {age} years old? Were you born in {year}?")
#5. Hello, Nick Kammerer are you 20 years old? Were you born in 2002?


# In[37]:


fib = "112358132134558914423337761098715972584418167651094617711286574636875025121393196418317811514229832040134626921783093524578"

print(fib[:20])
#6A. 11235813213455891442


# In[40]:


fib = "112358132134558914423337761098715972584418167651094617711286574636875025121393196418317811514229832040134626921783093524578"

print(fib[100:110])
#6B. 4013462692


# In[44]:


fib = "112358132134558914423337761098715972584418167651094617711286574636875025121393196418317811514229832040134626921783093524578"

print(F"Digit 100 is {fib[101]}. Digit 110 is {fib[111]}.")
#6C. Digit 100 is 0. Digit 110 is 7.


# In[45]:


fib = "112358132134558914423337761098715972584418167651094617711286574636875025121393196418317811514229832040134626921783093524578"

print(F"The length of the provided Fibonacci sequence is {len(fib)}.")
#6D. The length of the provided Fibonacci sequence is 123.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




