import requests
import webbrowser


def show_location(latitude, longitude):
    url = f"https://www.google.com/maps?q={latitude},{longitude}"
    webbrowser.open_new_tab(url)

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)
data = response.json()
longitude = data['iss_position'] ['longitude']
latitude = data['iss_position'] ['latitude']

show_location(latitude, longitude)
print(data)
print(longitude)
print(latitude)


