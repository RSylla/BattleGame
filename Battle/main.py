"""
Instructions for battle game program!
*Several parent classes with several child classes.
*Randomly creates an army to each faction.
*Classes are in a separate file from main program file.
*Arguments are taken from separate txt file to create an army.
*Army members will be saved in the separate csv file after randomly created.
*Game requires some user input to lead the game (select faction, some battle decisions)
*Need to use some kind of time count function to delay some functions or processes"""

import random as rm
import pandas as pd
import openpyxl

class Soldier:

    def soldier_generator(self):
        self.attr_keys_list = ["Name", "Type", "Health", "Strength", "Stealth", "Speed", "Accuracy"]
        soldier_types = ["Sniper", "Marine", "Intelligence"]
        names_list = [x[:-1] for x in list(open("names.txt", "r"))]
        surnames_list = [x[:-1] for x in list(open("surnames.txt", "r"))]
        self.name = f"{rm.choice(names_list)} {rm.choice(surnames_list)}"
        self.type = rm.choice(soldier_types)
        self.attr_values_list = [self.name,self.type]

        if self.attr_values_list[1] == "Sniper":
            self.attr_values_list.extend(self.__sniper_attr())
        elif self.attr_values_list[1] == "Marine":
            self.attr_values_list.extend(self.__marine_attr())
        elif self.attr_values_list[1] == "Intelligence":
            self.attr_values_list.extend(self.__intelli_attr())

        return dict(zip(self.attr_keys_list,self.attr_values_list))

    def __sniper_attr(self):
        self.health = rm.randrange(900, 1300)  # Health
        self.strength = rm.randrange(40, 70)  # Strength
        self.stealth = rm.randrange(150, 199)  # Stealth
        self.speed = rm.randrange(110, 140)  # Speed
        self.accuracy = rm.randrange(170, 200)  # Accuracy
        list = [self.health,self.strength,self.stealth,self.speed,self.accuracy]
        return list

    def __marine_attr(self):
        self.health = rm.randrange(1600, 2000)  # Health
        self.strength = rm.randrange(140, 190)  # Strength
        self.stealth = rm.randrange(50, 99)  # Stealth
        self.speed = rm.randrange(60, 110)  # Speed
        self.accuracy = rm.randrange(80, 120)  # Accuracy
        list = [self.health,self.strength,self.stealth,self.speed,self.accuracy]
        return list

    def __intelli_attr(self):
        self.health = rm.randrange(1200, 1600)  # Health
        self.strength = rm.randrange(50, 90)  # Strength
        self.stealth = rm.randrange(160, 200)  # Stealth
        self.speed = rm.randrange(60, 90)  # Speed
        self.accuracy = rm.randrange(100, 140)  # Accuracy
        list = [self.health,self.strength,self.stealth,self.speed,self.accuracy]
        return list

class Army(Soldier):

    def __init__(self, size, name):
        self.size = int(size)
        self.army_name = name


    def army_generator(self):
        army_list = []
        for x in range(self.size):
            soldier = self.soldier_generator()
            army_list.append(soldier)

        army_df = pd.DataFrame(army_list)
        army_df.to_excel(f"Armies/{self.army_name}.xlsx")

