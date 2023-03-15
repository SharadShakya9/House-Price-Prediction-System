from flask import Flask, request, render_template, flash
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

data = pd.read_csv(
    r'') #input a csv file with full file location between the apostrophes.
forest = pickle.load(open(
    r"", 'rb')) #input the pickle file of the machine learning model with full file location between the inverted commas.


def predict_price(req):
    longitude = req.form.get("longitude")
    latitude = req.form.get("latitude")
    house_age = req.form.get("house_age")
    rooms = req.form.get("rooms")
    bedroom_ratio = req.form.get("bedroom-ratio")
    ocean_proximity = req.form.get("ocean-proximity")

    if ocean_proximity == "<1H OCEAN":
        OCEAN = 1
        INLAND = 0
        ISLAND = 0
        NEAR_BAY = 0
        NEAR_OCEAN = 0
    elif ocean_proximity == "INLAND":
        OCEAN = 0
        INLAND = 1
        ISLAND = 0
        NEAR_BAY = 0
        NEAR_OCEAN = 0
    elif ocean_proximity == "ISLAND":
        OCEAN = 0
        INLAND = 0
        ISLAND = 1
        NEAR_BAY = 0
        NEAR_OCEAN = 0
    elif ocean_proximity == "NEAR BAY":
        OCEAN = 0
        INLAND = 0
        ISLAND = 0
        NEAR_BAY = 1
        NEAR_OCEAN = 0
    else:
        OCEAN = 0
        INLAND = 0
        ISLAND = 0
        NEAR_BAY = 0
        NEAR_OCEAN = 1

    input_data = pd.DataFrame([[longitude, latitude, house_age, rooms,
                                bedroom_ratio, OCEAN, INLAND, ISLAND, NEAR_BAY, NEAR_OCEAN]], columns=['longitude', 'latitude', 'housing_median_age', 'bedroom_ratio', 'household_rooms', '<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])
    prediction = forest.predict(input_data)[0]

    predicted_price = str(np.round(prediction, 2))

    return predicted_price


@app.route('/', methods=['GET'])
def base():
    return render_template("base.html")


@app.route('/predict', methods=['POST'])
def predict():
    predicted_price = predict_price(request)
    return {
        "predicted_price": predicted_price
    }


if __name__ == '__main__':
    app.run(debug=True)
