# index.py

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/travel/car', methods=['POST'])
def car():
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
    return 'Hello, World!'
