import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "61d9c4eac84ac9bd1a7849466822bc15"

account_sid = "avskfhgolrsij;ldm934" #example the site is called twilio
auth_token = "your_auth_token"


weather_params = {
    "lat":5678889,#exampl
    "lon":45676567,#exampl
    "appid":api_key,
    "exlude":"current,minutely,daily"
}

response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        will_rain = True
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
    .create(
        body="It is going to rain today,Bring an umbrella",
        from_='+3456789875434567',#twilio phone number
        to='+65789765678796857'#client number
    )
print(message.sid)