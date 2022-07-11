import random


class Hamurabi(object):
    def play_game(self):

        population = 100
        bushels = 2800
        acres_of_land = 1000
        land_value = 19
        year_of_rule = 0
        bushels_harvested = 3000
        bushels_harvested_per_acre = 3
        people_starved = 0
        people_entered = 5
        bushels_destroyed = 200
        plague_deaths = 0
        print_rules(self)


        for year in range(1,11):
            print("Our benevolent leader Hamurabi!\n"
                  "It is year " + str(year_of_rule) + " of your ten year rule.\n"
                  "In the previous year " + str(people_starved) + " people starved to death.\n"
                  "In the previous year " + str(people_entered) + " people entered the kingdom.\n"
                  "The population is now " + str(population) + ".\n"
                  "We harvested " + str(bushels_harvested) + " bushels at " + str(bushels_harvested_per_acre) +" bushels per acre.\n"
                  "Rats destroyed " + str(bushels_destroyed) + " bushels, leaving " + str(bushels) + " in storage.\n"
                  "The city owns " + str(acres_of_land) + " acres of land.\n"
                  "Land is currently worth " + str(land_value) + " bushels per acre. \n" 
                  "There were " + str(plague_deaths) + " deaths from the plague\n"
                  "============********* Year " + str(year_of_rule) + " **********==========\n")


            acres_bought = ask_to_buy_land(bushels, land_value)
            if acres_bought:
                acres_of_land += acres_bought
                bushels -= acres_bought * land_value
            else:
                acres_sold = ask_to_sell_land(acres_of_land, land_value)
                acres_of_land -= acres_sold
                bushels += acres_sold * land_value

            bushels_fed = ask_to_feed_people(bushels, population)
            bushels -= bushels_fed

            acres_planted = ask_to_plant_land(population, bushels, acres_of_land)
            bushels -= acres_planted * 2


            plague_deaths = do_plague(population)
            population -= plague_deaths
            people_starved = get_starved_num(population, bushels_fed)
            do_dismissal_for_starv(people_starved, population, year_of_rule)
            population -= people_starved
            people_entered = int(get_immigrts_num(acres_of_land, bushels, population, people_starved))
            population += people_entered
            bushels_harvested_per_acre = get_unit_havst()
            bushels_harvested = get_havst_bushels(acres_planted,bushels_harvested_per_acre)
            bushels_destroyed = do_rats_infest(bushels_harvested)
            bushels += bushels_harvested - bushels_destroyed
            land_value = get_land_price()
            year_of_rule = year_of_rule +1
            print()



        final_summary(acres_of_land, bushels, population, people_starved, plague_deaths)



def print_rules(self):
     print("Congratulations! You are the new ruler of ancient Sumer, elected for a ten year term of office. \n"
            "Your duties are to dispense food, direct farming, and buy and sell land as needed to support your people.\n"
            "Watch out for rat infestations and the plague! Grain is the general currency, measured in bushels.\n"
            "The following will help you in your decisions:\n"
            "\n"
            "-Each person needs at least 20 bushels of grain per year to survive\n"
            "-Each person can farm at most 10 acres of land\n"
            "-It takes 2 bushels of grain to farm an acre of land\n"
            "-The market price for land fluctuates yearly\n"
            " \n"
            "Rule wisely and you will be showered with appreciation at the end of your term. \n"
            "Rule poorly and you will be kicked out of office!")
     print("Let's play!\n ===========================================")

def ask_to_buy_land(bushels_in_storage, cost):
    print("**You have " + str(bushels_in_storage) + " bushels available to buy land, feed people and plant seed.**\n")
    acres = int(input("How many acres of land do you want to buy?\n"))
    while acres * cost > bushels_in_storage:
        print("Oh Hamurabi!! You only have" + str(bushels_in_storage) + " bushels of grain.\n")
        acres = int(input("Again, how many acres do  you want to buy?\n"))
    return acres

def ask_to_sell_land(curr_acres, cost):
    acres = int(input("How many acres of land do you want to sell?\n"))
    while acres > curr_acres:
        print("You don't have enough acres to sell. You only have " + str(curr_acres) + " available.\n")
        acres = int(input("Again, how many acres do you want to sell?"))
    return acres

def ask_to_feed_people(curr_bushels, num_of_people):
    print("\n**You have " + str(curr_bushels) + " bushels of grain available to feed your people.**\n"
            "**You need " + str(num_of_people * 20) + " bushels to feed all your people.**\n")
    bushels_fed = int(input("How many bushels of grain will you feed the people?\n"))
    while bushels_fed > curr_bushels:
        print("You don't have enough bushels of grain.")
        bushels_fed = int(input("Try again. How many bushels do you want to feed your people?\n"))
    return bushels_fed

def ask_to_plant_land(num_of_people, bushels_ongoing, curr_acres):
    acres = int(input("How many acres of land do you want to plant with seed?\n"))
    while True:
        if acres > num_of_people * 10:
            print("You don't have enough people to farm the land.\n")
            acres = int(input("Try again. How many acres do you want to plant? You have enough people to plant "
                + str(num_of_people * 10) + " acres of land.\n"))
            continue
        if bushels_ongoing < acres * 2:
            print("You don't have enough bushels to plant.\n")
            acres = int(input("Try again. How many bushels to plant? You have enough bushels of grain to plant " +
                              str(bushels_ongoing//2) + " acres.\n"))
            continue
        if acres > curr_acres:
            print("You don't have enough land!\n")
            acres = int(input("Try again. How many acres to plant?\n"))
            continue
        break
    return acres

def do_plague(num_of_people):
        # simulate whether or not a plague happened and return a consequence
    if random.randint(0, 100) < 15:
        print("***O great Hammurabi, a horrible PLAGUE happened! ", str(num_of_people // 2), " people died***")
        return num_of_people // 2
    else:
        return 0

def get_starved_num(num_of_people, bushels_fed):
        # get the number of people starved this year
    num_of_the_starved = ((num_of_people *20) - bushels_fed) / 20
    if num_of_the_starved > 0:
        return int(num_of_the_starved)
    else:
        return 0

def do_dismissal_for_starv(num_of_the_starved, num_of_people, year_of_rule):
        # judge whether or not the user should be dismissed according
        # to the numbers of people starved
    if (int(num_of_the_starved) > (0.45 * num_of_people)):
        game_ends(year_of_rule)


def get_immigrts_num(acres, bushels, num_of_people, num_of_the_starved):
        # get the number of immigrants to our country this year
    if num_of_the_starved:

        return 0
    else:
        num_of_immigrts = (20 * acres + bushels) // (100 * num_of_people) + 1
        return num_of_immigrts

def get_havst_bushels(acres, unit_havst):
        # get bushels of grain harvested this year
    bushels_havst = acres * unit_havst
    return bushels_havst

def get_unit_havst():
        # get bushels per acre yielded
    return random.randint(1, 6)

def do_rats_infest(hvst):
    if random.randint(1, 100) < 40:
        bushels_destroyed_by_rats = random.randint(10, 30) * hvst // 100
        return bushels_destroyed_by_rats
    else:
        return 0

def get_land_price():
    # get the price of land next year
    land_price = random.randint(17, 23)
    # print("***O great Hammurabi, the price of land will be", land_price, "bushels" \
    #                                                                          " per acre next year***")
    return land_price

def final_summary(acres, bushels, num_of_people, num_of_the_starved, num_of_plague_deaths):
    print("CONGRATULATIONS!\n"
          "Hamurabi our wonderful leader, you've made it successfully through your ten years in charge.\n"
          "In your final year of rule \n"
          "Your kingdom owns " + str(acres) + " acres of fertile land.\n"
          "Your kingdom has " + str(bushels) + " bushels of grain in storage.\n"
          "Your kingdom has a total population of " + str(num_of_people) + ".\n"
          "You had " + str(num_of_the_starved) + " people starve.\n"
          "You had " + str(num_of_plague_deaths) + " die of the plague\n")


    eval_population(num_of_people)
    eval_acres_per_person(acres, num_of_people)


def game_ends(year_of_rule):
    print("Oh Hamurabi....Hamurabi...\n"
          "Unfortunately you starved people and your remaining subjects revolted!\n"
          "Your authority ended in the " + str(year_of_rule) + " of your ten year term.")
    quit()

def eval_population(population):
    if population > 200:
        print("Wow! Your kingdom is thriving! You attracted many newcomers and your population doubled in 10 years.\n")
    elif population >= 100 :
        print("Your population showed a little growth. A solid effort.")
    elif population < 100:
        print("Hamurabi!! You must feed your people! You have less people than the beginning of your term.\n"
              "Stop being stingy with the grain!")

def eval_acres_per_person(acres, population):
    acres_pp = acres // population
    if acres_pp > 20:
        print("Amazing Hamurabi! You've doubled the acres per person in your ten year term.\n")
    elif acres_pp >= 10:
        print("Total acres per person has increased slightly showing conservative land management\n"
              )
    else:
        print("Oh Hamurabi. Poor management shows a decrease in the acres per person at the end of your term.\n")
    print("The total acres per person is " + str(acres_pp) + ".\n")



if __name__ == '__main__':
    Hamurabi().play_game()