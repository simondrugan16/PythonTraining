capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# nesting

travel_log = {
    "France": ["Paris", "Lyon", "Normandy"],
    "Germany": ["Koln", "Munchen"]
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log_dict = {
    "France": {
        "num_times_visited": 1,
        "cities_visited": ["Paris", "Lyon", "Normandy"]
    },
    "Germany": {
        "num_times_visited": 2,
        "cities_visited": ["Koln", "Munchen"]
    }
}

print(travel_log_dict["Germany"]["cities_visited"][1])