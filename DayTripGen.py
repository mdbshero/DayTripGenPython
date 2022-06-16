destinations = ['Cool Springs', 'East Nashville', 'Broadway', 'Spring Hill', 'Green Hills', 'Huntsville', 'Columbia', 'Murfreesboro']
restaurants = ['Chauhan', 'Emmy Squared', 'International Market', 'Tansuo', 'House of Cards', 'The Mockingbird', 'Loveless Cafe', 'Pemrose']
transportation = ['automobile', 'bus', 'Uber', 'Lyft', 'bike', 'train', 'helicoptor']
entertainment = ['honkey tonk', 'magic show', 'Grand ol Opry show', 'musical', 'park', 'sporting event', 'music show', 'museum']

# Create a random number generator
from cProfile import run
import random
from tracemalloc import stop
def random_num(list):
    num = random.randrange(0, len(list))
    return num

# Use random number to select from lists
def random_choice(list):
    choice = list[random_num(list)]
    return choice

# Select initial random trip
def initial_trip():
    random_dest = random_choice(destinations)
    random_rest = random_choice(restaurants)
    random_trans = random_choice(transportation)
    random_ent = random_choice(entertainment)
    itrip = [random_dest, random_rest, random_trans, random_ent]
    return itrip

first_trip = initial_trip() #initial trip selection
# initial trip sentence display
def trip_display(trip):
    display_text = "You will travel to " + trip[0] + ". You will eat at " + trip[1] + ". You will travel by " + trip[2] + ". Your day's entertainment will be going to a " + trip[3] +"."
    return display_text

print(trip_display(first_trip))

# reselect trip input function
def trip_reselect():
    trip = first_trip
    choice = input("Which selection would you like to change? Select 1 for destinations, 2 for restaurants, 3 for transportation, 4 for entertainment, or 5 for none\n")
    if choice == "1":
        trip[0] = random_choice(destinations)
    elif choice == "2":
        trip[1] = random_choice(restaurants)
    elif choice == "3":
        trip[2] = random_choice(transportation)
    elif choice == "4":
        trip[3] = random_choice(entertainment)
    elif choice == "5":
        next
    else:
        trip_reselect()
    return trip

# function that asks user if they are happy with their trip or want to make changes
def user_query():
    trip = first_trip
    user_prompt = input("Your current trip plan is as follows: " + trip_display(trip) + " Would you like to make any changes? Please enter 1 for yes or 2 for no\n")
    if user_prompt == "1":
        trip_reselect()
        user_query()
    elif user_prompt == "2":
        print("Your final trip selection is as follows: " + trip_display(trip))
        next
    else:
        user_query()

# run all
def run_all():
    print("Welcome to your random day trip generator")
    user_query()

run_all()