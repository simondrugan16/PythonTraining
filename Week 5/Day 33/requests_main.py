import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response.json())

data = response.json()["iss_position"]

print(data)

# response2 = requests.get("http://random.unused-webiste-lalala.com")
# response2.raise_for_status()

sunset_params = {
    "lat": 51.454514,
    "lng": -2.587910
}
sunset_response = requests.get("https://api.sunrise-sunset.org/json", params = sunset_params)
sunset_response.raise_for_status()
print(sunset_response.json())