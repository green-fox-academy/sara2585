import pandas as pd
import numpy as np
import re
from datetime import datetime
import matplotlib.pyplot as plt
import sklearn
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv('df_final.csv')
postcode_lon_lat = pd.read_csv('ukpostcodes.csv')

# print(df)
#define train and test data:
trains = df[['bedrooms', 'houseType', 'residential', 'duration', 'latitude', 'longitude']]
results = df['price']

def LinearRegression_tain( trains, results):
    lr = LinearRegression()
    lr.fit(trains, results)
    return lr
    # score = lr.score(trains, results)
    # return score
# print(LinearRegression_tain(trains, results))
def RandomForestRegressor_train(x, y):
    rfr = RandomForestRegressor()
    rfr.set_params(n_estimators = 70)
    rfr.fit(x, y)
    return rfr

def transfrom_data(postcode, bedrooms, housetype, residential, duration):
    lat_lon = get_lat_lon(postcode)
    lat = lat_lon[0][0]
    lon = lat_lon[0][1]
    # bedrooms = int(bedrooms)
    # housetype = int(housetype)
    # residential = int(residential)
    # duration = int(duration)
    test = [int(bedrooms), int(housetype), int(residential), int(duration), lat, lon]

    return  np.array(test).reshape(1,6)

def get_lat_lon(postcode1):
    record = postcode_lon_lat[postcode_lon_lat['postcode']== postcode1]
    lat_lon = record[['latitude', 'longitude']].values
    return lat_lon

# model = LinearRegression_tain(trains, results)
model = RandomForestRegressor_train(trains, results)

def get_prediction(test):
    prediction = model.predict(test)
    return int(prediction[0])


# test = transfrom_data('BA1 4EQ','3', '0', '1', '0')
# prediction = model.predict(test)
# print(prediction)
# print(get_lat_lon('BA1 4EQ'))


