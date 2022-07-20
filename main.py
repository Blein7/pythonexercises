import random
from art import logo
from art import vs
from game_data import data

flag = False
score = 0
check = 0


def compare(choice_a, choice_b, score):
    global check
    if choice_a['follower_count'] > choice_b['follower_count'] and selection == 'A':
        print(f"You're right! Current score:{score + 1}")
        return score + 1
    elif choice_a['follower_count'] < choice_b['follower_count'] and selection == 'B':
        print(f"You're right! Current score:{score + 1}")
        return score + 1
    else:
        check = 1
        print(f"Sorry, that's wrong. Final score: {score}")
        return check


choice_a = random.choice(data)
choice_b = random.choice(data)
print(logo)
while choice_a != choice_b:
    while not flag:

        print(f"Compare A: {choice_a['name']},{choice_a['description']}, from {choice_a['country']}")
        print(vs)
        print(f"Compare B: {choice_b['name']},{choice_b['description']}, from {choice_b['country']}")
        selection = input("Who has more followers?Type 'A' or 'B': ")
        score = compare(choice_a, choice_b, score)
        if check == 1:
            flag = True
        else:
            choice_a = choice_b
            choice_b = random.choice(data)
