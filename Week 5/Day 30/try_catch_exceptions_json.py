import json

# FileNotFoundError
# with open("RandomFileName.txt") as file:

# KeyError
# my_dict = {"a", 2}
# my_dict["b"]

# IndexError
# my_list = ["a", "b", "c"]
# my_list[3]

# TypeError
# my_string = "hello"
# variable = my_string * 4

try:
    file = open("Week 5/Day 30/file_non_exist.txt")
    my_dict = {"a": 2, "b": 7}
    # print(my_dict["hello"])
except FileNotFoundError:
    file = open("Week 5/Day 30/file_non_exist.txt", "w")
    file.write("hello")
except KeyError as error_message:
    print(f"That was not a key! Message: {error_message}")
else:
    content = file.read()
    print(content)
finally:
    print("Block is done!!! Going to raise an exception")
    # raise InterruptedError("Oh no!! I made up this error!")


my_dict_for_json = {
    "key1": "value1",
    "key2": ["value2.1", "value2.2", "value2.3"],
    "key3": "value3",
    "key4": {
        "key4.1": "value4.1",
        "key4.2": ["value4.21", "value4.22", "value4.23", "value4.24"],
        "key4.3": "value4.3"
    }
}

updated_data_dict = {
    "key5": "value5"
}

# with open("Week 5/Day 30/my_nu_jason.json", "r") as file:
    # json.dump(my_dict_for_json, file)

with open("Week 5/Day 30/my_nu_jason.json", "r") as file:
    data = json.load(file)
    data.update(updated_data_dict)

with open("Week 5/Day 30/my_nu_jason.json", "w") as file:
    json.dump(data, file, indent = 4)
    # print(type(json.load(file)))