# index.py

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Calculate emissions or something lol'

@app.route('/travel/car', methods=['POST'])
def car():
    type_of_car = request.form['type']
    distance = request.form['distance_miles']
    return jsonify({'CO2e_MT' : calc(type_of_car, 1, distance)})

@app.route('/travel/train', methods=['POST'])
def train():
    type_of_train = request.form['type']
    passengers = request.form['passengers']
    distance = request.form['distance_miles']
    return jsonify({'CO2e_MT' : calc(type_of_train, passengers, distance)})

@app.route('/travel/bus', methods=['POST'])
def bus():
    passengers = request.form['passengers']
    distance = request.form['distance_miles']
    return jsonify({'CO2e_MT' : calc("bus", passengers, distance)})

@app.route('/travel/plane', methods=['POST'])
def plane():
    passengers = request.form['passengers']
    distance = request.form['distance_miles']
    if int(distance) < 300:
        length_of_journey = "less_than_300"
    elif int(distance) > 300 and int(distance) < 2300:
        length_of_journey = "300_to_2300"
    else:
        length_of_journey = "more_than_2300"
    return jsonify({'CO2e_MT' : calc(length_of_journey, passengers, distance)})

@app.route('/event', methods=['POST'])
def event():
    return 'Calculate emissions or something lol'

def calc(travel_type,passengers,distance):
    emmissions = {"passenger": 0.000359995, "light_truck": 0.000492056,
                  "motorcycle": 0.000194836, "intercity_rail": 0.0001371015,
                  "communter_rail": 0.0001702257, "transit_rail": 0.0001205691,
                  "bus": 0.000055164, "less_than_300": 0.0002535709,
                  "300_to_2300": 0.0001444006, "more_than_2300": 0.0001686838 }
    return emmissions[travel_type] * int(distance) * int(passengers)
"""def car():
    return 'Hello, World!'

@app.route('/travel/train', methods=['POST'])
def train():
    return 'Hello, World!'

@app.route('/travel/bus', methods=['POST'])
def bus():
    passengers = request.form['passengers']
    distance = request.form['distance_miles']
    emissions = 0.000_055_164 * int(passengers) * int(distance)
    return jsonify({'CO2e_MT': emissions})

@app.route('/travel/plane', methods=['POST'])
def plane():
    return 'Hello, World!'"""

if __name__ == "__main__":
    app.run(host='0.0.0.0')
