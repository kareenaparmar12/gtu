#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[2]:


import numpy as np
file=np.loadtxt("cric.tsv",skiprows=1)
file


# In[3]:


import numpy as np
cric_data = np.loadtxt("cric_data.tsv",skiprows=1)
sachin=cric_data[:,1]
sachin


# In[4]:


import numpy as np
cric_data = np.loadtxt("cric_data.tsv",skiprows=1)
Dravid=cric_data[:,2]
Dravid


# In[5]:


import numpy as np
cric_data = np.loadtxt("cric_data.tsv",skiprows=1)
india=cric_data[:,3]
india


# In[6]:


mean = np.mean(sachin)
mean


# In[7]:


mean = np.mean(Dravid)
mean


# In[9]:


mean = np.mean(india)
mean


# In[10]:


max=np.max(sachin)
max


# In[11]:


max=np.max(Dravid)
max


# In[12]:


max=np.max(india)
max


# In[ ]:




