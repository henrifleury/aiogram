import requests
api_url = "http://numbersapi.com/43"
response = requests.get(api_url)

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)
# 43 is the maximum number of cars participating in a NASCAR race in the Cup Series or Nationwide Series.
