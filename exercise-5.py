# Iterate over the _key: value_ pairs in `home_town` and print a string for each item, for example:<br>"city = Arcadia"<br>"state = California"<br>"population = 58000"

home_town = {
    "city": "st. catharine's",
    "province": "ontario",
    "population": "130,000"
}

for key in home_town:
    print(key, home_town[key])