import pandas as pd
import numpy as numpy

from datetime import datetime

############################# Acquire Temperature Data ############################# 

def get_temps_data():
    '''
    This function will pull the dataset from the provided .csv file 
    and will write it to a pandas dataframe. 
    
    To reproduce the results, you will need the GlobalLandTemperaturesByState.csv file downloaded in your working directory.
    '''
    df = pd.read_csv('GlobalLandTemperaturesByState.csv')
    
    return df




############################# Prepare Temperature Data ############################# 

# defines function to clean movies data and return as a cleaned pandas DataFrame
def clean_temps(df):
    '''
    clean_temps will take one argument df, a pandas dataframe and will:
    shorten dataset with only Texas temperatures,
    rename columns,
    convert date (`dt`) column to datetime datetype,
    set date as index,
    and drop `Country` and `State` columns
   
    return: a single pandas dataframe with the above operations performed
    '''
  
    #specify Texas data
    df = df[df.State.str.contains('Texas')]

    #rename columns
    df = df.rename(columns={"dt": "date", 
                        "AverageTemperature": "avg_temp",
                        "AverageTemperatureUncertainty": "avg_uncertainty"})

    #convert date column to datetime
    df.date = pd.to_datetime(df.date)

    # setting date column to index
    df = df.set_index('date').sort_index()

    #drop `Country` column
    df = df.drop(columns=['Country', 'State'])

    return df



# splits a time series dataframe into train, validate, test 
def split(df):
    '''
    takes in a DataFrame,
    sets train, validate, and test size, 
    uses the values to split the DataFrame, and 

    returns train, validate, test DataFrames.
    '''

    #set train size to be 50% of total
    train_size = int(len(df) * .5)
    train_size

    #set validate size to be 30% of total
    validate_size = int(len(df) * .3)
    validate_size

    #validate end index will go from 1162 to 1162 + 697
    validate_end_index = train_size + validate_size
    validate_end_index

    #train will go from 0 to 1161
    train = df[: train_size]

    #validate will go from 1162 to 1858
    validate = df[train_size:validate_end_index]

    #test will include 1859 to the end
    test = df[validate_end_index:]

    return train, validate, test