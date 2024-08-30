# Luftverschmutzung_API

Gets Air Quality Data from api.wagi.info and takes a city as paramater.

##How to start
Set your personal API Token as an env variable. You can generate a token on https://aqicn.org/data-platform/token/
Set the token like this:
''' export API_TOKEN=<<api-token>> '''

Run:
''' pip install -r requirements.txt '''
''' python3 main.py ''' runs code by default on http://127.0.0.1

Get the air quality data for your city:
''' http://127.0.0.1:5000/getAirQuality?city=hamburg '''
