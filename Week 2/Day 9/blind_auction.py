
def clear_console():
    print("\n" * 100)

def get_highest_score(dict = dict[str, int]):
    highest_bid_with_name = ("", 0)
    for person in dict:
        if dict[person] > highest_bid_with_name[1]:
            highest_bid_with_name = (person, dict[person])
    return highest_bid_with_name

def print_bid_winner(name: str, bid: int):
    print(f"{name} won the auction with a bid of £{bid}")

def start_game():
    continue_game = True
    working_dict = {}
    while continue_game:
        clear_console()
        if input("Would you like to continue, 'y' or 'n'") == "n":
            continue_game = False
        else:
            name = input("What is your name? ")
            bid = int(input("Enter your big amount: £"))
            working_dict[name] = bid
    return working_dict

def main():
    bidders_and_bids = start_game()
    clear_console()
    highest_score = get_highest_score(bidders_and_bids)
    print_bid_winner(highest_score[0], highest_score[1])

main()