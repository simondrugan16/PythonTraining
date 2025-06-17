import random

def is_ace(card: str):
    is_ace = card[0] == "A"
    return is_ace

def is_not_ace(card: str):
    is_not_ace = not (card[0] == "A")
    return is_not_ace

def is_not_busted(total: int):
    is_not_busted = total < 22
    return is_not_busted

def ace_totals(num_aces):
    totals = set([0])
    for _ in range(num_aces):
        new_totals = set()
        for total in totals:
            new_totals.add(total + 1)
            new_totals.add(total + 11)
        totals = new_totals
    return sorted(totals)

card_values_dict = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

def generate_cards():
    list_suits = ["s", "h", "c", "d"]
    list_ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards_list = []
    for suit in list_suits:
        for rank in list_ranks:
            cards_list.append(rank + suit)
    random.shuffle(cards_list)
    return cards_list

def get_card_and_remove_from_list(card_list: list[str]):
    return card_list.pop(0)

def start_game():
    print("Welcome to Blackjack! The aim of the game is to get as close to 21 as possible!")
    print("However, beware, you will lose if you go above 21!")
    card_list = generate_cards()
    dealer_card_1 = get_card_and_remove_from_list(card_list)
    player_card_1 = get_card_and_remove_from_list(card_list)
    player_card_2 = get_card_and_remove_from_list(card_list)
    print(f"The dealer turns over: {dealer_card_1}")
    print(f"You turn over: {display_hand([player_card_1, player_card_2])}")
    player_final_hand = play_game([player_card_1, player_card_2], card_list)

    print("The dealer turns over their second card")
    dealer_card_2 = get_card_and_remove_from_list(card_list)
    
    print(f"The dealer turns over their second card, it is: {dealer_card_2}")

    if get_highest_total(get_possible_totals(player_final_hand)) is not None:
        dealer_final_hand = play_dealer([dealer_card_1, dealer_card_2], card_list)
    else:
        dealer_final_hand = [dealer_card_1, dealer_card_2]
    
    finish_game(player_final_hand, dealer_final_hand)

def display_hand(hand: list[str]):
    string_builder = ""
    for card in hand:
        string_builder += card + " "
    return string_builder

def win_draw_loss_message(player_total: int, dealer_total: int):
    if player_total is None:
        return f"You busted :c you lose..."
    elif dealer_total is None:
        return f"You win!! The dealer busted\nYou had {player_total}\nDealer had {dealer_total}"
    elif player_total > dealer_total:
        return f"You win!!\nYou had {player_total}\nDealer had {dealer_total}"
    elif dealer_total > player_total:
        return f"Dealer wins :(\nYou had {player_total}\nDealer had {dealer_total}"
    else:
        return f"It was a draw...\nYou had {player_total}\nDealer had {dealer_total}"
    
def get_possible_totals(player_hand: list[str]):
    if not any("A" in card for card in player_hand):
        total = sum(card_values_dict[card[:-1]] for card in player_hand)
        return [total]
    else:
        num_aces = len(list(filter(is_ace, player_hand)))
        cards_without_aces = list(card_values_dict[card[:-1]] for card in filter(is_not_ace, player_hand))
        sum_cards_without_aces = sum(cards_without_aces)
        ace_total = ace_totals(num_aces)
        possible_totals = [potential_total + sum_cards_without_aces for potential_total in ace_total]
        return possible_totals

def get_highest_total(totals: list[int]):
    totals_without_busts = list(filter(is_not_busted, totals))
    if len(totals_without_busts) == 0:
        return None
    else:
        return max(totals_without_busts)

def play_game(player_hand: list[str], card_list: list[str]):
    _continue = True
    print(f"Your current hand is {display_hand(player_hand)}")
    while _continue:
        if get_highest_total(get_possible_totals(player_hand)) is None:
            print("You busted!")
            _continue = False
        else:
            if input("Would you like to hit again? 'y' or 'n' ") == "n":
                print("You stand")
                _continue = False
            else:
                print("You take another card!")
                player_hand.append(get_card_and_remove_from_list(card_list))
                print(f"Your current hand is {display_hand(player_hand)}")
    return player_hand

def finish_game(player_hand: list[str], dealer_hand: list[str]):
    player_final_total = get_highest_total(get_possible_totals(player_hand))
    dealer_final_total = get_highest_total(get_possible_totals(dealer_hand))
    print(win_draw_loss_message(player_final_total, dealer_final_total))

def play_dealer(dealer_hand: list[str], card_list: list[str]):
    _continue = True
    while _continue:
        print(f"The dealers hand is: {display_hand(dealer_hand)}")
        dealer_possible_totals = get_possible_totals(dealer_hand)
        dealer_highest_total = get_highest_total(dealer_possible_totals)
        if dealer_highest_total is None:
            print(f"The dealer busted!")
            _continue = False
        elif dealer_highest_total >= 17:
            print(f"The dealer stands on {dealer_highest_total}")
            _continue = False
        else:
            dealer_hand.append(get_card_and_remove_from_list(card_list))
            play_dealer(dealer_hand, card_list)
    return dealer_hand

start_game()