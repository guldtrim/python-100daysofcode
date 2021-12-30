travel_log = [
    {
        "country": "France", 
        "visits" : 3,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits" : 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(a, b, c):
    travel_log.append({"country": a, "visits": b, "cities": c})

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)