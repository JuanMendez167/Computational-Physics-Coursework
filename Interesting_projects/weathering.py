from flask import Flask, request, render_template
import requests

app = Flask(__name)

# Replace with your OpenWeatherMap API key
api_key = 'd7ce011ed825fe14cd539a8184194fec'

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        if not city:
            return render_template('index.html', error="Please enter a city name.")
        
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temperature = data['main']['temp']
            weather = data['weather'][0]['description']
            location = f"Weather in {city}"
            return render_template('weather.html', location=location, temperature=temperature, weather=weather)
        else:
            return render_template('index.html', error="City not found. Please check the spelling.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
