# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 11:17:11 2023

@author: Juan
"""

from flask import Flask, request, render_template
import requests

app = Flask(__name)

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'YOUR_API_KEY'  # Replace with your API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        return render_template('weather.html', city=city, temperature=temperature, weather=weather)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
