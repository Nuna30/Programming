#!/usr/bin/env python
# coding: utf-8

# In[16]:


N=int(input())
count=1
shom=666
while N!=count:
    shom+=1
    for i in range(len(str(shom))-2) :
        if str(shom)[i:i+3]=='666' :
            count+=1
            break
print(shom)
    


# In[ ]:





# In[ ]:




