<!--lint disable no-literal-urls-->
<p align="center">
  <a href="https://Oso.com/">
    <img
      alt="Oso"
      src="http://clipart-library.com/images/ki8pMekir.png" width="192" height="120" 
    />
  </a>
</p>

“HONEY” 

Honeybees are disappearing at an alarming rate. As a consequence, the production of honey is also on the decline. This project is a simple demonstration of sourcing relatively clean data and using it to build a DataFrame that can be easily queried for the purpose of analysis and used for machine learning predictions.

# Table of contents

* [Support](#support)
* [Overview](#overview)
* The Process
  * [Imports](#imports)
  * [Data Analysis](#Data-Analysis)
  * [Data Cleaning](#data-cleaning)
  * [Modeling](#Modeling)
  * [Predicting](#Predicting)


* [Current Project Team Members](#current-project-team-members) 

* [Collaborators](#collaborators)
  
## Support

Looking for help? Send an email for direct support &lt;hizstor@gmail.com&gt;

## Overview
Honey was built with PyCharm 2020.3.3 running Python 3.9.1.

Honey is designed to take a look at a set of data that shows the downward trend of honey production across the united states and predict production for the years to come. The data is already clean and requires little to no manipulation before modeling. The information will be loaded into a Pandas Dataframe grouped by year and then used to train and a model that will predict future honey production. 


## Imports
Libraries that must be imported to python environment for code to run successfully 

* **pandas**: Used to build DataFrames.
* **matplotlib.pyplot**: as plt, used for used to visualize data. 
* **numpy**: as np, a system for working with arrays.   
* **LinearRegression**: from sklearn.linear_model, built in functions for ML modeling.   



## Data Analysis

A few lines of code are included to analyze the data as it is presented from the source material. While not strictly necessary in the final code for it to run successfully it shows the process used to find and organize the requisite information later used for modeling. 

## Data Cleaning

The provided data is essentially clean. The only change made was in the creation of a variable to hold the data relevant to the current project in an array. This array holds the information related to the amount of honey produced and sorts it by year. The array is then “.reshaped” to fit modeling requirements.    
The provided data is essentially clean . 

## Modeling

Now that the data is formatted we can use it in combination with linear regression and plotting functions to create a visual representation of our data. This is done in the form of a scatter plot. The plot shows each of our data points (honey production and year of production) plotted accordingly. It also shows a second set of points representing the linear regression found using the provided data. The plot will show a downward trajectory of honey production. There are also a couple of lines included to show the intercept and slope of the line.

## Predicting

With the functioning model, it is very easy to apply Sklearn’s predict function to the data. This takes the information plugged into the model and projects future honey production for years to come.  According to this prediction, honey will essentially cease entirely in the mid 50’s. If steps are taken to reverse the course of honey production, this model could be used to project future growth instead of decline. The core of this model is the data if you change the data you will change what the model produces. Minor changes can also be made to show other projections for the data. (What state will be first to stop producing honey, what state will be last to stop producing honey, projecting the price of honey in years to come.  etc)   

## Current project team members
* [OsoSuerte](https://github.com/OsoSuerte) -
**Ben Sadler** &lt;hizstor@gmail.com&gt; (he/him)


<!--lint disable prohibited-strings-->

### Collaborators

* [OsoSuerte](https://github.com/OsoSuerte) -
**Ben Sadler** &lt;hizstor@gmail.com&gt; (he/him)

<!--lint enable prohibited-strings-->


