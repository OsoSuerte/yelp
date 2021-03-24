
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# All data needed for this project is from the files below.
businesses = pd.read_json('C:\Coding\Portfolio\Yelp\yelp_regression_project\yelp_business.json', lines=True)
reviews = pd.read_json('C:\Coding\Portfolio\Yelp\yelp_regression_project\yelp_review.json', lines=True)
users = pd.read_json('C:\Coding\Portfolio\Yelp\yelp_regression_project\yelp_user.json', lines=True)
checkins = pd.read_json('C:\Coding\Portfolio\Yelp\yelp_regression_project\yelp_checkin.json', lines=True)
tips = pd.read_json('C:\Coding\Portfolio\Yelp\yelp_regression_project\yelp_tip.json', lines=True)
photos = pd.read_json('C:\Coding\Portfolio\Yelp\yelp_regression_project\yelp_photo.json', lines=True)

pd.options.display.max_columns = 50
pd.options.display.max_colwidth = 500

# These lines were used to evaluate data and are not needed for modeling.
'''
print(businesses.head())
print(len(businesses))
print(reviews.head())
print(reviews.columns)
print(users.head())
print(users.describe())
print(checkins.head())
print(tips.head())
print(photos.head())
print(businesses[businesses['business_id'] == '5EvUIR4IzCWUOm0PsUZXjA']['stars'])
'''

# merges the above files into one larger DataFrame. Then removes the unwanted features.
full = pd.merge(businesses, reviews, how = 'left', on = 'business_id')
full = pd.merge(full, users, how = 'left', on = 'business_id')
full = pd.merge(full, checkins, how = 'left', on = 'business_id')
full = pd.merge(full, tips, how = 'left', on = 'business_id')
full = pd.merge(full, photos, how = 'left', on = 'business_id')
to_clean = ['address','attributes','business_id','categories','city','hours','is_open','latitude','longitude','name','neighborhood','postal_code','state','time']
full.drop(to_clean, axis=1, inplace=True)

# Checks for missing of NaN values that will disrupt modeling.
# print(full.isna().any())
full.fillna({'weekday_checkins':0,
           'weekend_checkins':0,
           'number_tips':0,
           'average_caption_length':0,
           'number_pics':0,
           'average_tip_length':0},
          inplace=True)

# Shows plot for a single review feature
plt.scatter(full['average_review_sentiment'], full['stars'],alpha=0.1)
plt.xlabel('average_review_sentiment')
plt.ylabel('Yelp Rating')
plt.show()

features = full[['average_review_length','average_review_age']]
ratings = full['stars']
sentiment = ['average_review_sentiment']
binary_features = ['alcohol?','has_bike_parking','takes_credit_cards','good_for_kids','take_reservations','has_wifi']
numeric_features = ['review_count','price_range','average_caption_length','number_pics','average_review_age','average_review_length','average_review_sentiment','number_funny_votes','number_cool_votes','number_useful_votes','average_tip_length','number_tips','average_number_friends','average_days_on_yelp','average_number_fans','average_review_count','average_number_years_elite','weekday_checkins','weekend_checkins']
all_features = binary_features + numeric_features

# This function will take one of the above lists to model as a parameter
def model_these_features(feature):
    # Define ratings and features, with the features limited to our chosen subset of data
    ratings = full.loc[:, 'stars']
    features = full.loc[:, feature]

    # perform train, test, split on the data
    X_train, X_test, y_train, y_test = train_test_split(features, ratings, test_size=0.2, random_state=1)

# Allows model to work with a single feature
    if len(X_train.shape) < 2:
        X_train = np.array(X_train).reshape(-1, 1)
        X_test = np.array(X_test).reshape(-1, 1)

    # create and fit the model to the training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # print the train and test scores
    print('Train Score:', model.score(X_train, y_train))
    print('Test Score:', model.score(X_test, y_test))

    # print the model features and their corresponding coefficients, from most predictive to least predictive
    print(sorted(list(zip(feature, model.coef_)), key=lambda x: abs(x[1]), reverse=True))

    # Use the test data to predict yelp ratings
    y_predicted = model.predict(X_test)

    # plot the actual Yelp Ratings vs the predicted Yelp ratings for the test data
    plt.scatter(y_test, y_predicted)
    plt.xlabel('Yelp Rating')
    plt.ylabel('Predicted Yelp Rating')
    plt.ylim(1, 5)
    plt.show()

# The will produce models of the different features for comparison
print(model_these_features(sentiment))
print(model_these_features(binary_features))
print(model_these_features(numeric_features))
print(model_these_features(all_features))

# Pull everything together and define variables to use for predicting future Yelp reviews
features = full.loc[:,all_features]
ratings = full.loc[:,'stars']
X_train, X_test, y_train, y_test = train_test_split(features, ratings, test_size = 0.2, random_state = 1)
model = LinearRegression()
model.fit(X_train,y_train)

# Predict the yelp score a new restaurant will receive based on its features.
new_restaurant = np.array([0,1,1,1,1,1,10,2,3,10,10,1200,0.9,3,6,5,50,3,50,1800,12,123,0.5,0,0]).reshape(1,-1)
print(model.predict(new_restaurant))








