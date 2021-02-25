# first install requests module from external library - command - pip install requests

import requests

# res = requests.get("https://www.facebook.com/", verify=False)
# print(res.ok)

# print(res.status_code)
# print(res.headers)

# print(res.text) #html code

# ------------------------------------how to get json data---------------------------------
# method 1 (will only work for some websites)
# res = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/text"}, verify=False) #plain html
res = requests.get("https://icanhazdadjoke.com/",
                   headers={"Accept": "application/json"}, verify=False)
print(res.text)
print(type(res.text))  # will be type of string
# ---------------method -2-------------------------------
res = requests.get(
    "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson", verify=False)

var = res.json()
# will be type of class dictionary. that we can use it as an python dictionary(object- JS)
print(type(var))
print(var["features"][0])
