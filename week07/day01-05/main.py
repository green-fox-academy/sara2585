from flask import Flask
from flask import render_template
from flask import request
from functions import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route('/prediction', methods=['GET','POST'])
def enter_conditions():

    return render_template('predict.html')


@app.route('/result', methods=['POST'])
def price_prediction():

    housetype = request.form.get('housetype')
    bedrooms = request.form.get('bedrooms')
    newbuild = request.form.get('newbuild')
    duration = request.form.get('duration')
    postcode = request.form.get('postcode')
    # postcode and bedroom cannot be null:
    if len(get_lat_lon(postcode)) > 0:
    # print(housetype, bedrooms, newbuild, duration,postcode)
        test = transfrom_data(postcode, bedrooms, housetype, newbuild, duration)
        prediction = get_prediction(test)
    else:
        prediction = 'Please input correct postcode'

    return render_template('result.html', prediction = prediction)




