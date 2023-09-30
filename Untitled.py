#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# range of 1 to 25.


# In[ ]:


# ANS: Python def keyword is used to define a function, it is placed before a function name that is provided by 
#     the user to create a user-defined function.

number1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


# In[ ]:


def get_odd():
    odd_list = []
    for i in number1:
        if i % 2!=0:
            odd_list.append(i)
        
    return odd_list


# In[ ]:


odd_num_list = get_odd()


# In[ ]:


print(odd_num_list)
        


# In[ ]:





# In[ ]:


# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
# to demonstrate their use.


#ANS: Python has *args which allow us to pass the variable number of non keyword arguments to function.

# *args

# In the function, we should use an asterisk * before the parameter name to pass variable length arguments.
# The arguments are passed as a tuple and these passed arguments make tuple inside the function with same name as 
# the parameter excluding asterisk *



# **kwargs

# it allows us to pass the variable length of keyword arguments to the function.

# In the function, we use the double asterisk ** before the parameter name to denote this type of argument.
# The arguments are passed as a dictionary and these arguments make a dictionary inside function with name same as 
# the parameter excluding double asterisk **.


# In[8]:


# *args
def test11(*args):
    return args
test11(1,2,1,3,4,5)
type(test11())


# In[9]:


# **kwargs
def test15(**kwargs):
    return kwargs
test15(id=100,name="jd")
type(test15())


# In[10]:


# Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
# used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
# 16, 18, 20].

# ANS: An iterator in Python is an object that contains a countable number of elements that can be iterated upon.
# In simpler words, we can say that Iterators are objects that allow you to traverse through all the elements of a 
# collection and return one element at a time. More specifically, we say that an iterator is an object that 
# implements the iterator protocol



# In[12]:


# define a iterable such as a list
list1 = [2, 4, 6, 8, 10, 12, 14,
16, 18, 20]
# get an iterator using iter()
iter1 = list1.__iter__()
#iertae the item using __next__method
print(iter1.__next__())


# In[28]:


given_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Create an iterator
iter_list = iter(given_list)

# Iterate and print the first five elements
for i in range(5):
    try:
        element = next(iter_list)
        print(element)
    except StopIteration:
        break


# In[29]:


given_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Create an iterator
iter_list = iter(given_list)

# Iterate and print the first five elements
for i in range(5):
        element = next(iter_list)
        print(element)


# In[34]:


# Q4.  What is a generator function in python? Why yield keyword is used? Give an example of a generator
# function.

# ANS:
# In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated 
# over.

#  Generators are useful when we want to produce a large sequence of values, but we don't want to store all of 
# them in memory at once.


# yield

# yield keyword is used to create a generator function. A type of function that is memory efficient and can be used
# like an iterator object.
# the yield keyword will turn any expression that is given with it into a generator object and return it to the 
# caller. Therefore, you must iterate over the generator object if you wish to obtain the values stored there.



def my_gen(n):
    value= 0
    while value < n :
        yield value
        value +=1
        
for value in my_gen(3):
    print(value)


# In[32]:



    
    


# In[33]:





# In[ ]:




