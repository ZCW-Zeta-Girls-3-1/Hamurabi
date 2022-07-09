class Hamurabi(object):

    def play_game(self):
        print
        "Let's play!"
    ## lots more methods here...


if __name__ == '__main__':
    Hamurabi().play_game()

import random

# print(random.randint(0, 5))
# #This will output either 1, 2, 3, 4 or 5.
# print(random.random()) # will print a number from 0.0 to less than 1.0
# # so if you need a number between 0.0 and 100.0
# print(random.random() * 100.0)

def do_plague(num_of_people):
    # simulate whether or not a plague happened and return a consequence
    if random.randint(0, 100) < 15:
        print ("***O great Hammurabi, unluckily a horrible PLAGUE" \
        " happened!", num_of_people / 2, "people died***")
        return num_of_people / 2
    else:
        print ("***Thank God! No plague this year***")
        return 0

def get_starved_num(num_of_people, grain_fed):
    # get the number of people starved this year
    num_of_the_starved = num_of_people - grain_fed / 20
    if num_of_the_starved > 0:
        print ("***O great Hammurabi, unfortunately this year we " \
        "have", num_of_the_starved, "PEOPLE STARVED***")
        return num_of_the_starved
    else:
        print ("***O brilliant Hammurabi! This year we have NO people starved***")
        return 0

def do_dismissal_for_starv(num_of_the_starved, num_of_people, yr):
    # judge whether or not the user should be dismissed according
    # to the numbers of people starved
    if num_of_the_starved > 0.45 * num_of_people:
        print ("***O great Hammurabi, we  really regret to inform you that this " \
        "year", num_of_the_starved, "people have been starved, which represent " \
        "more than 45% of total population in your Samaria kingdom. According " \
        "to our laws, you're now unfortunately given an immediate dismissal request")
        # game_ends(yr)

def get_immigrts_num(acres, bushels, num_of_people, num_of_the_starved):
    # get the number of immigrants to our country this year
    if num_of_the_starved:
        print ("***O great Hammurabi, due to starvation, NO IMMIGRANTS this year" \
        "come to our kingdom***")
        return 0
    else:
        num_of_immigrts = (20 * acres + bushels) / (100 * num_of_people) + 1
        print ("***O great Hammurabi, this year", num_of_immigrts, "immigrants" \
        "come to our kingdom***")
        return num_of_immigrts

def get_havst_bushels(acres, unit_havst):
    # get bushels of grain harvested this year
    bushels_havst =  acres * unit_havst
    print ("***O great Hammurabi, this year we harvest", bushels_havst, "bushels" \
    " of grain***")
    return bushels_havst

def get_unit_havst():
    # get bushels per acre yielded
    return random.randint(1, 8)


def do_rats_infest():
    '''Check if there was rats' infestation'''
    chance = random.randint(1, 100)
    if chance <= 40:
        return True
    else:
        return False


def percent_destroyed():
    '''Calculates the percent destroyed by rat infestations'''
    if do_rats_infest():
        percent_destroyed = random.uniform(0.1, 0.3)
        return percent_destroyed
    else:
        return 0


def get_land_price():
    # get the price of land next year
    land_price = random.randint(17, 23)
    print ("***O great Hammurabi, the price of land will be", land_price, "bushels" \
    "ls per acre next year***")
    return land_price

get_land_price()
do_rats_infest()
percent_destroyed()
