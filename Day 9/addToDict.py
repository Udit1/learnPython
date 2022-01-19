travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Not a good way


def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})

# better Approch


def add_new_country1(country, visits, cities):
    new_dict = {}
    new_dict["country"] = country
    new_dict["visits"] = visits
    new_dict["cities"] = cities

    travel_log.append(new_dict)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


add_new_country1("India", 20, ["Delhi", "Mumbai", "Pune"])
print(travel_log)
