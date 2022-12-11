#!/usr/bin/env python
# coding: utf-8

# In[6]:


#  Exercise 01a


print('Hello world!')


# In[7]:


#  Exercise 01b


public class HelloWorld
{
 public static void main(String[] args)
 {
  System.out.println("Hello world!");
 }
}


#  SyntaxError: invalid syntax (kernel is Python3 not Java)


# In[10]:


# Exercise 01c


namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            System.Console.WriteLine("Hello world!");
        }
    }
}


# SyntaxError: invalid syntax (kernel is Python3 not C#)


# In[9]:


#  Exercise 01d


#include <stdlib.h>
#include <stdio.h>

int main(void)
{
  printf("Hello world!\n");
  return EXIT_SUCCESS;
}


# SyntaxError: invalid syntax (kernel is Python3 not C)


# In[11]:


#  Exercise 02 


print('Nick Kammerer')


# In[13]:


#  Exercise 03

print(" ")


# In[16]:


#  Exercise 04a

len("Python")

#  return: 6


# In[17]:


#  Exercise 04b


len("My favorite number is nine")

#  return: 26


# In[18]:


#  Exercise 04c


len("In 2022, Python 3.10.4 and 3.9.12 were expedited and so were older releases including 3.8.13, and 3.7.13 because of many security issues in 2022. Python 3.9.13 is the latest 3.9 version, and from now on 3.9 (and older; 3.8 and 3.7) will only get security updates.")

#  return: 263


# In[23]:


#  Exercise 05a


9988870 * 303


#  return: 3026627610


# In[24]:


#  Exercise 05b


34199820 / 2121.4


#  return: 16121.34439521071


# In[25]:


#  Exercise 05c


9988870 + 34199820 + 2121.4


#  return: 44190811.4


# In[26]:


#  Exercise 05d


(9988870 + 34199820 + 2121.4) / 2


#  return: 22095405.7


# In[28]:


#  Exercise 05e


(130 + 45 - 12) / (98 * 2)


#  return: 0.8316326530612245


# In[29]:


#  Exercise 05f


332,403,650 - 332,524,270


#  return: (332, 403, 318, 524, 270)


# In[45]:


#  Exercise 06


participants = 325
teamCap = 6
wholeTeams = participants // teamCap
runtTeam = participants % teamCap

print("Complete teams = " + str(wholeTeams) + ".")
print("The remaining team consists of " + str(runtTeam) + ".")


#  return: Complete teams = 54.0.
#  return: The remaining team consists of 1 participants.
#  I got this result by utilizing the // operator, as well as modulo


# In[46]:


#  Exercise 07a


import math

math.log(10)


#  return: 2.302585092994046


# In[41]:


#  Exercise 07b


import math
math.sqrt(255)


#  return: 15.968719422671311


# In[42]:


#  Exercise 07c


import math
math.gcd(200, 25)

#  return: 25


# In[52]:


#  Exercise 07d


import math

wholeTeams = round(325/6)
runtTeam = math.remainder(325,6)

print(wholeTeams)
print(runtTeam)


#  wholeTeams = 54
#  runtTeam = 1.0


# In[53]:


#  Exercise 08a


89 == 87


# return: False


# In[55]:


#  Exercise 08b


332433240365003633240365050 != 332433240365003633240365050


# return: False


# In[54]:


#  Exercise 08c


332433240365003633240365050 == 332433240365003633240365050


# return: True


# In[56]:


#  Exercise 08d


89 > 89


# return: False


# In[57]:


#  Exercise 08f

89 < 89


# return: False


# In[58]:


#  Exercise 08g


89 == 89


# return: True


# In[59]:


#  Exercise 08h


89 >= 89


# return: True


# In[60]:


#  Exercise 08i


89 <= 89


# return: True


# In[62]:


#  Exercise 08j


89 == '89'


# return: False


# In[63]:


#  Exercise 08k


89 != '89'


# return: True


# In[64]:


#  Exercise 08l


True == True


# return: True


# In[66]:


#  Exercise 08m


True == 'True'


# return: False


# In[68]:


#  Exercise 08n


'Hello World!' == 'Hello World!'


# return: True


# In[3]:


#  Exercise 09


area = 929
digits = " 255-6000"
number = '(' + str(area) + ')' + digits

print(number)


# return: "(929) 255-6000"


# In[5]:


#  Exercise 10

print('Hello World!')
name = input('What is your name? ') # prompt input user's name
print('It is good to meet you, ' + name)
print ('The length of your name is:')
print(len(name))
age = input('What is your age?') # prompt input user's age
print('You will be ' + str(int(age) + 1) + ' in a year.')

#  return: 
#  Hello World!
#  What is your name?Joe Mama
#  It is good to meet you, Joe Mama
#  The length of your name is:
#  8
#  What is your age?100000000
#  You will be 100000001 in a year.

