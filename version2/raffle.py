"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries
import Random

def randomly_pick_winner(customers):
    winner = random.choice(customers)
    print(f'reach out to {name} at {email} and tell them they won!'.format(name = winner.name
    email = winner.email))

def run_raffle():
    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)


if __name__ == "__main__":
    run_raffle()