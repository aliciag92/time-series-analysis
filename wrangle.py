import pandas as pd
import numpy as numpy

from sklearn.model_selection import train_test_split
import sklearn.preprocessing

############################# Acquire Climate Data ############################# 

def get_movies_data():
    '''
    This function will pull the dataset from the provided .csv file 
    and will write it to a pandas dataframe. 
    
    To reproduce the results, you will need the movies_metadata.csv file in your working directory.
    '''
    df = pd.read_csv('dataset.csv')
    
    return df




############################# Prepare Climate Data ############################# 

# defines function to clean movies data and return as a cleaned pandas DataFrame
def clean_climate(df):
    '''
    clean_climate will take one argument df, a pandas dataframe and will:
    ___,
    ____,
    ___,
    and ___
   
    return: a single pandas dataframe with the above operations performed
    '''
  
    #___
    df = 

    #
    df = 


    #fill in values w/ very little nulls
    df = df.fillna(0)


    return df



# splits a dataframe into train, validate, test 
def split(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames.
    return train, validate, test DataFrames.
    '''
    #split w/ time series data

    return train, validate, test