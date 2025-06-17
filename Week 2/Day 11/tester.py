def make_list():
    return [1,2,3]

def fetch_item_from_list(my_list: list[int]):
    return my_list.pop(0)

def main():
    my_list = make_list()
    my_value = fetch_item_from_list(my_list)
    my_value2 = fetch_item_from_list(my_list)
    print(f"my value: {my_value}")
    print(f"my value2: {my_value2}")
    print(f"my list: {my_list}")
    
main()