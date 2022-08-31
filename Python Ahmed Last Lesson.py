#!/usr/bin/env python
# coding: utf-8

# In[2]:


fruits= ['apples\n', 'oranges\n', 'bananas\n', 'mangoes\n', 'strawberries\n', 'cherries\n']

with open('fruits.txt', 'w') as f:
    for fruit in fruits:
        f.write(fruit)


# In[4]:


with open('fruits.txt', 'r') as f:
    print(f.read())


# In[8]:


with open('fruits2.txt', 'w') as f:
    f.writelines(fruits)


# In[9]:


with open('fruits2.txt', 'r') as f:
    print(f.read())


# In[7]:


fruits2= ['apples ', 'oranges ', 'bananas ', 'mangoes ', 'strawberries ', 'cherries ']
with open('fruits3.txt', 'w') as f:
    f.writelines(fruits2)


# In[10]:


with open('fruits3.txt', 'r') as f:
    print(f.read())


# In[11]:


with open('fruits.txt', 'a') as f:
    f.write('melon\n')


# In[13]:


with open('fruits2.txt', 'w') as f:
    f.write('melon')


# In[15]:


with open('fruits2.txt', 'a') as f:
    f.write('\nLichies')


# In[16]:


with open('fruits.csv', 'r') as f:
    print(f.read())


# In[17]:


with open('people.csv', 'r') as f:
    print(f.read())


# In[31]:


import csv
with open('people.csv', 'r') as f:
    ppl_rows = csv.reader(f)
    print(type(ppl_rows))
    
    for row in ppl_rows:
        print(row)
    print(type(row[0]))
    print(len(row))


# In[ ]:




