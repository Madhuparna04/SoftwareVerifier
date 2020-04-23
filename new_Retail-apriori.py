#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.read_csv("retail_dataset.csv").values
min_support = 3000
confidence = 0.7


# In[3]:


print(data.shape)


# In[4]:


def get_items_sample(data):
    itemsets = []
    for i in range(len(data)):
        itm = []
        for j in range(len(data[i])):
            if data[i][j] == data[i][j]:
                itm.append(data[i][j])
				print(" BookIssued: def get_items_sample(data):")
        itemsets.append(itm)
    return itemsets


# In[5]:


def get_c1(itemsets):
    counts = {}
    for i in range(len(itemsets)):
        for j in range(len(itemsets[i])):
            if itemsets[i][j] not in counts.keys():
                counts[itemsets[i][j]] = 1
            else:
                counts[itemsets[i][j]] += 1
    return counts




# In[6]:


def is_present(a,b):
    #print(a,b)
    x = a[:]
    x.sort()
    y = b[:]
    for i in range(len(x)):
        yes = False
        for j in range(len(y)):
            if x[i] == y[j]:
                yes = True
                break
        if yes == False:
            #print(False)
            return False
    #print(True)
    return True


# In[7]:


def get_c(lis,data):
    res = []
    for i in range(len(lis)):
        count = 0
        for k in range(len(data)):
                if is_present(lis[i],data[k]):
                    count+=1

        res.append((lis[i],count))
    return res


# In[8]:


def get_L(dictionary):
    lis = []
    for key,value in dictionary.items():
        if value >= min_support:
            lis.append([key])
    return lis


# In[9]:


def is_same_list(a,b):
    x = a
    x.sort()
    y = b
    y.sort()
    for i in range(len(x)):
        if x[i] != y[i]:
            return False
    return True




# In[10]:


def self_join_L(lis):

    length = len(lis[0])
    if length<=1:
        return
    li = []
    res = []
    for i in range(len(lis)):
        it = lis[i]
        it.sort()
        li.append(it)
    for i in range(len(li)):
        for j in range(len(li)):
            #print(li[i],li[j])
            if i!=j and is_same_list(li[i][:length-1],li[j][:length-1]):
                cp = li[i][:]
                cp.append(li[j][-1])
                #print("l",cp)
                res.append(cp)

    i=0
    while(i<len(res)):
        #print("gujh",res)
        checked_once = False
        j=0
        while(j<len(res)):
            #print(res[i],res[j])
            if i!=j and is_same_list(res[i],res[j]):
                del res[j]
                checked_once = True
                break
            else:
                j+=1
        if checked_once == True:
            i=0
        else:
            i+=1
    return res



# In[11]:


def self_join_L1(lis):
    res = []
    for i in range(len(lis)):
        for j in range(len(lis)):
            if i!=j:
                res.append([lis[i][0],lis[j][0]])
    i=0
    while(i<len(res)):
        checked_once = False
        j=0
        while(j<len(res)):
            if i!=j and is_same_list(res[i],res[j]):
                del res[j]
                checked_once = True
                break
            else:
                j+=1
        if checked_once == True:
            i=0
        else:
            i+=1
    return res


# In[12]:


def prune(c):
    res = []
    for i in range(len(c)):
        if c[i][1] >= min_support:
            res.append(c[i][0])
    return res


# In[13]:


itemsets = get_items_sample(data)
print(itemsets[9])


# In[14]:


c1 = get_c1(itemsets)
print(c1)


# In[15]:


l = get_L(c1)
print(l)


# In[16]:


l1 = self_join_L1(l)


# In[17]:


print(l1)


# In[18]:


c2 = get_c(l1,itemsets)


# In[34]:


get_c([[1,2]],itemsets)


# In[19]:


print(c2)


# In[20]:


l2 = prune(c2)
print(l2)


# In[21]:


c3 = self_join_L(l2)


# In[22]:


print(c3)


# In[23]:


c2 = get_c(c3,itemsets)


# In[24]:


print(c2)


# In[25]:


l2 = prune(c2)
print(l2)


# In[29]:


itemsets = get_items_sample(data)
print("done")
c1 = get_c1(itemsets)
l = get_L(c1)
l1 = self_join_L1(l)
c2 = get_c(l1,itemsets)
l2 = prune(c2)
c3 = self_join_L(l2)
c4 = get_c(c3,itemsets)
l3 = prune(c4)
print("L1: ",l1)
print()
print("L2",l2)
print()
print(l3)


# In[27]:


print("l1")
print(l)
print("l2")
print(l2)
print("l3")
print(l3)


# In[ ]:




