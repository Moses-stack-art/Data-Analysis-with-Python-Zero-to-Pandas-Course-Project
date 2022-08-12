#!/usr/bin/env python
# coding: utf-8

# # Project Title - Datascience job salaries
# 
# ### Introduction
# In this project, I will examine a dataset on the pay for several data science professions that I downloaded from Kaggle. Using this dataset, I'll provide answers to a number of questions, including: Does a person's work role have an impact on their salary? Does the sort of employment affect the wage earned? Does the size and location of the company have an impact on the salary paid? 
# To answer these questions, I'll be utilizing Python libraries such as Numpy and Pandas for computations, and Matplotlib and Seaborn for visualizations.
# A lot of what I'll be doing derives its inspiration from the course offered by Jovian; Data Ananlysis: Zerotopandas.
# 

# ## Downloading the Dataset

# In[1]:


get_ipython().system('pip install jovian opendatasets --upgrade --quiet')


# Let's begin by downloading the data, and listing the files within the dataset.

# In[2]:


dataset_url = 'https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries'


# In[3]:


import opendatasets as od
od.download(dataset_url)


# The dataset has been downloaded and extracted.

# In[4]:


data_dir = './data-science-job-salaries'


# In[5]:


import os
os.listdir(data_dir)


# Let us save and upload our work to Jovian before continuing.

# In[6]:


project_name = "datascience-jobs-salaries"


# In[7]:


get_ipython().system('pip install jovian --upgrade -q')


# In[8]:


import jovian


# In[9]:


jovian.commit(project=project_name)


# ## Data Preparation and Cleaning
# 
# **TODO**
# In this step, I'll be preparing the dataset for analysis by removing any null values and duplicate values and reorganizing the dataset in a way that will make the analysis's findings informative.
# 
# 

# In[10]:


import pandas as pd
import numpy as np
import os


# In[11]:


salary_df = pd.read_csv('./data-science-job-salaries/ds_salaries.csv')


# In[12]:


salary_df


# In[13]:


salary_df.drop(["Unnamed: 0"], axis = 1, inplace = True)


# In[14]:


salary_df.columns


# In[15]:


salary_df.info()


# In[16]:


salary_df.describe()


# In[17]:


import jovian


# In[18]:


jovian.commit()


# ## Exploratory Analysis and Visualization
# 
# 
# An exploratory analysis is a thorough examination meant to uncover the underlying structure of a data set and is important because it exposes trends, patterns, and relationships that are not readily apparent.
# 
# 

# Let's begin by importing`matplotlib.pyplot` and `seaborn`.

# In[19]:


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'


# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[20]:


# The level of experience of each job holder.
salary_df.experience_level.value_counts().plot.barh()


# From the above graph, we can see that the senior level of experience has the highest number of job holders, followed by the middle level, entry level, and the executive level.

# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[21]:


# The number of job holders per the type of employment
salary_df.employment_type.value_counts().plot.barh()


# From the above graph, it can be seen that most of the job holders are employed on a full time basis.

# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[22]:


# The number of job holders per the job title
salary_df.job_title.value_counts().head(10).plot.barh()


# Due to the large number of job roles inherent in our dataset, I've decided to use a sample of 10, starting with the job role having the highest number of employees.
# From the above diagram, it can be seen that a large number of employees in our dataset are data scientist, followed by data engineers, data analysts, machine learning engineers, research scientists, data science managers, data architects, big data engineers, machine learning scientists, and principal data scientists.

# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[23]:


# The distribution of the salary_in_usd
plt.hist(salary_df.salary_in_usd)


# From the above diagram, it can be seen that a huge number of employees' salary range from 50,000 to 100,000. We also have outliers, as one of the employees is receiving a salary of 600,000 usd.

# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[24]:


# The number of job holders per the company size
salary_df.company_size.value_counts().plot.barh()


# From the above graph, it can be seen that a huge number of employees are employed in medium sized companies, followed by large sized companies, and small sized companies.

# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[25]:


# we will now determine the relationship between the level of experience of the job holder and the salary (in usd)
salary_df.boxplot(column='salary_in_usd', by='experience_level')


# From the above diagram, it can be seen that there is a correlation between the job holders' level of experience and the amount of salary (in usd) received. The job holders at the executive level receive the highest salary, followed by the ones at the senior level, middle level, and the entry level.

# **TODO** - Explore one or more columns by plotting a graph below, and add some explanation about it

# In[26]:


# we will now determine the relationship between the level of experience and the size of the company.
combined = salary_df[['experience_level', 'company_size']]
combined.value_counts().plot.bar()


# From the above graph, it can be seen that most of the job holders at the senior level are employed in medium sized companies.
# The number of job holders at the executive level is low for both the large, medium, and small sized companies.

# Let us save and upload our work to Jovian before continuing

# In[27]:


import jovian


# In[28]:


jovian.commit()


# ## Asking and Answering Questions
# 
# In this section, I will be answering various questions regarding our dataset.
# #### The importance of asking good questions cannot be over-emphasized, as good questions highlight insights in our dataset that could act as the basis of many decisions regarding employment in the future.
# 

# In[29]:


#pd.set_option('display.max_rows', None)


# #### Q1: TODO - Is there a relationship between the level of experience of the job holder and the amount of salary received?

# In[30]:


salary_df


# In[31]:


experience=salary_df[['experience_level', 'salary_in_usd']]
experience.sort_values(by=['salary_in_usd'], ascending=False)


# In[32]:


salary_df.boxplot(column='salary_in_usd', by='experience_level')


# It is evident that there is a relationship between the level of experience and the salary (in usd), as job holders at the more senior and executive levels tend to receive the highest amount of salary.

# #### Q2: TODO - Is there a relationship between the type of employment and the amount of salary received by the job holder?

# In[33]:


type=salary_df[['employment_type', 'salary_in_usd']]
type.sort_values(by=['salary_in_usd'], ascending=False)
salary_df.employment_type.value_counts()


# In[34]:


salary_df.boxplot(column='salary_in_usd', by='employment_type')


# From the above diagram, we can see that there is a correlation between the type of employment and the amount of salary received. A significant number of job holders under the full mode of employment receive large sums of money. The exception is that a few individuals under the contract mode of employment also receive huge sums of money.

# #### Q3: TODO - Is there a relationship between the role of the job holder and the amount of salary received?

# In[35]:


title=salary_df[['job_title', 'salary_in_usd']]
title.sort_values(by=['salary_in_usd'], ascending=False)


# From our analysis, it is evident that the amount of salary received is proportional to the seniority of the job position held.

# #### Q4: TODO - Is there a relationship between the company location and the amount of salary received? (regardless of the job role)

# In[36]:


location=salary_df[['company_location', 'salary_in_usd']]
location.sort_values(by=['salary_in_usd'], ascending=False)


# The majority of the companies in our dataset are based in the United States. Compared to those outside of the US, the majority of these pay their staff enormous sums of money.

# #### Q5: TODO - Is there a relationship between the size of the company and the amount of salary received? (regardless of the job role)

# In[37]:


size=salary_df[['company_size', 'salary_in_usd']]
size.sort_values(by=['salary_in_usd'], ascending=False)


# In[38]:


salary_df.boxplot(column='salary_in_usd', by='company_size')


# From the above diagram; there is a correlation between the size of the company and the salary. As a significant number of individuals receiving huge amounts of money are employed in large companies.

# Let us save and upload our work to Jovian before continuing.

# In[40]:


import jovian


# In[41]:


jovian.commit()


# ## Inferences and Conclusion
# 
# From our analysis, it is evident that the more senior a position is in a company, the higher the amount of salary it receives.
# From our dataset, most of the companies are located in the US. It can be deduced that the United States has made significant investments in technology, as evidenced by the salaries that US-based companies pay their employees.
# In conclusion, it can be said that there is a great potential for growth in the tech industry (US) as more and more companies are recruiting individuals in tech-related roles, especially in data science.

# In[42]:


import jovian


# In[43]:


jovian.commit()

