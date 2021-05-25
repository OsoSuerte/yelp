<!--lint disable no-literal-urls-->
<p align="center">
  <a href="https://Oso.com/">
    <img
      alt="Oso"
      src="https://github.com/OsoSuerte/Logizomechanophobia/blob/master/Osos%20profile.png" width="300" height="300" 
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

Yelp is designed to clean and shape data related to restaurants and their attributes provided by Yelp.com. This project will look at different characteristics of restaurants and try to determine which have the greatest impact on their reviews. With this information, we will build a model using linear regression. This model will help us determine what attributes have the most direct impact on a restaurant’s reviews. With this information, we can plug information about a new restaurant into the model and see a prediction of what kind of reviews the restaurant can expect.

## Imports
Libraries that must be imported to python environment for code to run successfully 

* **pandas**: Used to build DataFrames.
* **matplotlib.pyplot**: as plt, used for used to visualize data. 
* **numpy**: as np, a system for working with arrays.   
* **LinearRegression**: from sklearn.linear_model, built in functions for ML modeling.  
* **train_test_split**: from sklearn.model_selection, built in functions splitting data for training and testing purposes.  



## Data Analysis

Towards the beginning of this project, there are multiple lines of code that are commented out. They were used to help me evaluate the accumulated data. They are not needed for the code to run when completed but I left them in place to show the process used in determining how the data should be structured and what elements should be the focus. There is some back and forth at this point. Analyzing the data helps determine what to clean and after it has been cleaned we can reevaluate and determine what data is most relevant to our model

## Data Cleaning

This data is fairly raw. The first step in formatting it into something more manageable was to merge the different sets of data into one DataFrame and remove features from the data frame that are not helpful in our modeling. Essentially all columns are removed that do not have continuous or binary values. For linear regression to work properly we will remove all missing or “NaN” values and replace them with “0” which works as a value for both binary and continuous values.  We can then do some analysis and determine which features to include in our model. 

## Modeling

After determining which features will be our focus we can create a training and testing set from our data for modeling. This is best done by defining a function that can be called with different subsets of data. Running the model on the different subsets helps determine which set of data is the best predictor of future outcomes. The highest scoring model is the one that uses all features so that is what we will use in the next step.

## Predicting

We now know what information is needed from a restaurant to predict how many stars it will get from Yelp reviewers. We can plug the values of a new restaurant into our model and get a prediction of how it will do. Preemptively we can plan a new restaurant based on this model that will have a high likelihood of scoring extremely well with reviewers. This serves the purpose of both predicting how a restaurant will be reviewed but guided development to ensure those reviews are positive. 

## Current project team members
* [OsoSuerte](https://github.com/OsoSuerte) -
**Ben Sadler** &lt;hizstor@gmail.com&gt; (he/him)


<!--lint disable prohibited-strings-->

### Collaborators

* [OsoSuerte](https://github.com/OsoSuerte) -
**Ben Sadler** &lt;hizstor@gmail.com&gt; (he/him)

<!--lint enable prohibited-strings-->

[Yelp]: https://www.yelp.com/


