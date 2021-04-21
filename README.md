# Texas Temperature Forecast
![Weather](https://theyorkshiresociety.org/wp-content/uploads/2021/03/texas-flag-header-1080x675.jpg)
****

## About the Project

****

### Description and Goals

brief description


### Objectives for this project include:
- Identifying the _______.
- Documenting process and analysis throughout the data science pipeline.
- Demonstrating the information that was discovered.
- Deliverables:
    - README.md file containing overall project information, how to reproduce work, and notes from project planning.
    - [Jupyter Notebook Report](insert link) detailing the pipeline process.
    - Python module that automates the data [wrangling](insert link).

****

### Data Dictionary

Feature      | Description   | Data Type
------------ | ------------- | ------------
date | starts in 1750 for average land temperature and 1850 for max and min land temperatures and global ocean and land temperatures  | datetime
avg_temp | global average land temperature in celsius | float
avg_uncertainty | the 95% confidence interval around the average | float

**** 

### Initial hypotheses
- Does the data increase, decrease, or stay the same over time?
- What is the distribution of yearly average temperature and yearly average uncertainty?
- What is the distribution of monthly average temperature and monthly average uncertainty?


****

### Pipeline Process:

#### Plan
- Understand project description and goals. 
- Form hypotheses and brainstorm ideas.
- Have all necessary imports ready for project.


#### 1. Acquire
- Download dataset from [Kaggle](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalLandTemperaturesByState.csv).
- Move download to desired folder on personal device.
- Define function to get climate data from local csv and return as a pandas DataFrame.
- Read csv in notebook by using wrangle.py script.
- Function to acquire the data is included in [wrangle.py](https://github.com/aliciag92/time-series-analysis/blob/main/wrangle.py.
- Complete initial data summarization and plot distributions of individual variables to get to know data and know what is needed to be prepped/cleaned.

#### 2. Prepare
- Define functions to:
    - clean climate data and return as a cleaned pandas DataFrame.
    - split the dataframe into train, validate, test.
- Functions to prepare the data are included in [wrangle.py](https://github.com/aliciag92/time-series-analysis/blob/main/wrangle.py.

#### 3. Explore
- Address questions posed in planning and brainstorming to forecast temperatures.
- Create visualizations of variables and run statistical tests (as many as needed).
- Summarize key findings and takeaways.

#### 4. Model/Evaluate
- Generate various time series analysis algorithms with varying hyperparameters (as many as needed) and settle on the best algorithm by comparing evaluation metrics.
- Choose the best model and test that final model on out-of-sample data.
- Summarize performance, interpret, and document results.

#### 5. Deliver
- 


****

### Recreating Project
- To reproduce this project, download [wrangle.py](https://github.com/aliciag92/time-series-analysis/blob/main/wrangle.py) and [forecasting-temp-report.ipynb](https://github.com/aliciag92/time-series-analysis/blob/main/forecasting-temp-report.ipynb) in your working directory and follow the steps from the pipeline process above.
- You can always obtain more features, or remove the ones you do not want, do your own exploring, modeling, and evaluating to deliver any new information.

****