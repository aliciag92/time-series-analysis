# Texas Temperature Forecast
![Weather](https://theyorkshiresociety.org/wp-content/uploads/2021/03/texas-flag-header-1080x675.jpg)
****

## About the Project

****

### Description and Goals

Some say climate change is the biggest threat of our age while others say it’s a myth based on dodgy science.

Early data was collected by technicians using mercury thermometers, where any variation in the visit time impacted measurements. In the 1940s, the construction of airports caused many weather stations to be moved. In the 1980s, there was a move to electronic thermometers that are said to have a cooling bias. Given this complexity, there are a range of organizations that collate climate trends data.

For this project, I will be focusing on average temperatures specifically from Texas.


### Objectives for this project include:
- Forecast Texas temperatures more accurately.
- Documenting process and analysis throughout the data science pipeline.
- Demonstrating the information that was discovered.
- Deliverables:
    - [README.md](https://github.com/aliciag92/time-series-analysis/blob/main/README.md) file containing overall project information, how to reproduce work, and notes from project planning.
    - [Jupyter Notebook Report](https://github.com/aliciag92/time-series-analysis/blob/main/forecasting-temp-report.ipynb) detailing the pipeline process.
    - Python module that automates the data [wrangling](https://github.com/aliciag92/time-series-analysis/blob/main/wrangle.py).

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
- The previous cycle model performs with an average temperature error of 1.68 degrees Celsius.
- This would be the best performing model moving forward for predicting average temperature and average temperature uncertainity for Texas


****

### Recreating Project
- To reproduce this project, download dataset from Kaggle, [wrangle.py](https://github.com/aliciag92/time-series-analysis/blob/main/wrangle.py) and [forecasting-temp-report.ipynb](https://github.com/aliciag92/time-series-analysis/blob/main/forecasting-temp-report.ipynb) in your working directory and follow the steps from the pipeline process above.
- You can always obtain more features, or remove the ones you do not want, do your own exploring, modeling, and evaluating to deliver any new information.

****