#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Calculate the area of a circle gi# Calculate the area of a circle given its radius
area = 3.14159 * (radius ** 2)  # Using the formula πr²
ven its radius
area = 3.14159 * (radius ** 2)  # Using the formula πr²


# In[2]:


# Calculate the area of a circle given its radius
def calculate_area(radius):
    # Using the formula πr²
    area = 3.14159 * (radius ** 2)
    return area


# In[3]:


# This function calculates the factorial of a number using recursion.
# Reference: "Introduction to Algorithms" by Cormen et al., Chapter 9
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# In[5]:


def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    The Fibonacci sequence is defined as follows:
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

    Reference:
    - Sedgewick, R., & Wayne, K. (2011). "Algorithms" (4th Edition), Chapter 1.

    Parameters:
        n (int): Index of the Fibonacci sequence to calculate

    Returns:
        int: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# In[6]:


import numpy as np

# Generate a random matrix using NumPy
# Reference: https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html
matrix = np.random.rand(3, 3)


# In[7]:


# Implementing Dijkstra's Algorithm for shortest path
# Reference: Dijkstra, E. W. (1959). "A Note on Two Problems in Connexion with Graphs."
def dijkstra(graph, start_vertex):
    # Initialization of shortest paths
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    # Algorithm code...


# In[8]:


# References:
# 1. "Python Programming for the Absolute Beginner" by Michael Dawson
# 2. "Effective Python" by Brett Slatkin
# 3. PEP 8 – Style Guide for Python Code: https://peps.python.org/pep-0008/


# In[ ]:


"""
Script to perform basic data cleaning on a dataset.

References:
- "Python for Data Analysis" by Wes McKinney
- Pandas Documentation: https://pandas.pydata.org/pandas-docs/stable/
"""

import pandas as pd

# Load the dataset
# Reference: Dataset available at https://example.com/dataset
data = pd.read_csv("data.csv")

def clean_data(df):
    """
    Clean the dataset by handling missing values and duplicates.

    Steps:
    1. Fill missing values with column means.
    2. Remove duplicate rows.

    Parameters:
        df (pd.DataFrame): Dataframe to be cleaned

    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    # Fill missing values
    df.fillna(df.mean(), inplace=True)  # Filling NaNs with column mean

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    return df

# Applying the cleaning function
cleaned_data = clean_data(data)

