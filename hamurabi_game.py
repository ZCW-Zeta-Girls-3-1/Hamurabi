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
        bushels_destroyed_by_rats = 200

        for year in range(1,11):
            print("Our benevolent leader Hamurabi!\n"
                  "It is year " + str(year_of_rule) + " of your ten year rule.\n"
                  "In the previous year " + str(people_starved) + " people starved to death.\n"
                  "In the previous year " + str(people_entered) + " people entered the kingdom.\n"
                  "The population is now " + str(population) + ".\n"
                  "We harvested " + str(bushels_harvested) + " bushels at " + str(bushels_harvested_per_acre) +" bushels per acre.\n"
                  "Rats destroyed " + str(bushels_destroyed_by_rats) + " bushels, leaving " + str(bushels) + " in storage.\n"
                  "The city owns " + str(acres_of_land) + " acres of land.\n"
                  "Land is currently worth " + str(land_value) + " bushels per acre. \n" )

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

            acres_planted = ask_to_plant_land(population, bushels)
            bushels -= acres_planted * 2

            # ============ GAMZE SECTION ================
            plague_deaths = 0
            population -= plague_deaths
            people_starved = 0
            #overthrow starvation
            population -= people_starved
            people_entered = 0
            population =+ people_entered
            bushels_harvested_per_acre = 3
            bushels_harvested = 1000 #XXX(acres_planted, bushels_harvested_per_acre)
            bushels_destroyed_by_rats = 0
            bushels += bushels_harvested - bushels_destroyed_by_rats
            land_value = 20
            print()

            #==============END OF THIS PART OF GAMZE SECTION============

        summary(acres_of_land, bushels, population, people_starved)



    def rules(self):
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
    acres = int(input("How many acres of land do you want to buy?\n"))
    while acres * cost > bushels_in_storage:
        print("You only have" + str(bushels_in_storage) + "bushels of grain.")
        acres = int(input("Again, how many acres do  you want to buy?\n"))
    return acres

def ask_to_sell_land(curr_acres, cost):
    acres = int(input("How many acres of land do you want to sell?\n"))
    while acres > curr_acres:
        print("You don't have enough acres to sell.\n")
        acres = int(input("Again, how many acres do you want to sell?"))
    return acres

def ask_to_feed_people(curr_bushels, num_of_people):
    bushels_ongoing = int(input("How many bushels of grain will you feed the people?\n"))
    while bushels_ongoing > curr_bushels:
        print("You don't have enough bushels of grain.")
        bushels_ongoing = int(input("Try again. How many bushels do you want to feed your people?\n"))
      return bushels_ongoing

def ask_to_plant_land(num_of_people, bushels_ongoing):
    acres = int(input("How many acres of land do you want to plant with seed?\n"))
    while True:
        if acres > num_of_people * 10:
            print("You don't have enough people to farm the land.\n")
            acres = int(input("Try again. How many acres do you want to plant?\n"))
            continue
        if bushels_ongoing < acres * 2:
            print("You don't have enough bushels to plant.\n")
            acres = int(input("Try again. How many bushels to plant?\n"))
            continue
        break
    return acres

    #=================GAMZE CALCULATIONS==============

def summary():
    print ("Summary goes here")

if __name__ == '__main__':
    Hamurabi().play_game()