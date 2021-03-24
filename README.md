<!--lint disable no-literal-urls-->
<p align="center">
  <a href="https://Oso.com/">
    <img
      alt="Oso"
      src="http://clipart-library.com/images/ki8pMekir.png" width="192" height="120" 
    />
  </a>
</p>

“YELP” 

[Yelp][] is a hot spot for finding user reviews one of the most popular categories is restaurants. This project will take a look at data sourced from yelp that will help us determine what impacts a restaurant’s reviews and predict the score a new restaurant will receive based on their attributes. 

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
Yelp was built with PyCharm 2020.3.3 running Python 3.9.1.

Yelp is designed to clean and shape data related to restaurants and their attributes. This project will look at different characteristics of restaurants and try to determine which have the greatest impact on their reviews. With this information, we will build a model using linear regression.  This model will help us determine what attributes have the most direct impact on a restaurant’s reviews. With this information, we can plug information about a new restaurant into the model and see a prediction of what kind of reviews the restaurant can expect.

## Imports
Libraries that must be imported to python environment for code to run successfully 

* **pandas**: Used to build DataFrames.
* **matplotlib.pyplot**: as plt, used for used to visualize data. 
* **numpy**: as np, a system for working with arrays.   
* **LinearRegression**: from sklearn.linear_model, built in functions for ML modeling.  
* **train_test_split**: from sklearn.model_selection, built in functions splitting data for training and testing purposes.  



## Data Analysis

Several lines of code in the begining A few lines of code are included to analyze the data as it is presented from the source material. While not strictly necessary in the final code for it to run successfully it shows the process used to find and organize the requisite information later used for modeling. 

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

[Yelp]: https://www.yelp.com/


