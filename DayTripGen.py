# (5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip.

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

# (10 points): As a user, I want to display my completed trip in the console.

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

destinations = ['Cool Springs', 'East Nashville', 'Broadway', 'Spring Hill', 'Green Hills', 'Huntsville', 'Columbia', 'Murfreesboro']
restaurants = ['Chauhan', 'Emmy Squared', 'International Market', 'Tansuo', 'House of Cards', 'The Mockingbird', 'Loveless Cafe', 'Pemrose']
transportation = ['automobile', 'bus', 'Uber', 'Lyft', 'bike', 'train', 'helicoptor']
entertainment = ['honkey tonk', 'magic show', 'Grand ol Opry show', 'musical', 'park', 'sporting event', 'music show', 'museum']

# Create a random number generator
import random
def random_num(list):
    num = random.randrange(0, len(list))
    return num

print(random_num(destinations))