import sys
import unittest
import numpy as np
import pandas as pd

def Director_full_choice(data: pd.DataFrame) -> dict:
    """For each director fill corresponding list with all
    data about the movie. Return dictionary.
    """

    Directors_choice={}
    for i in range(len(data)):
        name=data.iloc[i,0]
        if name[-1]==' ':
            name=name[:-1]
        if name not in Directors_choice:
            Directors_choice[name]=[(data.iloc[i,1].strip(),int(data.iloc[i,2]),data.iloc[i,3].strip())]
        else:
            Directors_choice[name].append((data.iloc[i,1].strip(),int(data.iloc[i,2]),data.iloc[i,3].strip()))
    return Directors_choice 
    
def matrix_init(alist: list) -> pd.DataFrame:
    """Create 2-D matrix from 1-D array with column and row values
    as per element of the 1-D array.
    """
    
    size=len(alist)
    initial=np.array([0 for i in range(size**2)])
    Full=pd.DataFrame(initial.reshape(size,size),index=alist,columns=alist)
    return Full 

def count_common(hashtable: dict, name1: str, name2: str) -> int:
    """Lookup the hashtable and count common elements for 2 elements.
    """
    
    list1=[line[0] for line in hashtable[name1]] 
    list2=[line[0] for line in hashtable[name2]] 
    count=len(set(list1).intersection(list2))
    return count
