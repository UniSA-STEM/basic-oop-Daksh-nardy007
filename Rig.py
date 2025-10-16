"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Daksh Narang
ID: 110402115
Username: nardy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:

    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__upgrade_level = 0
        self.__storage = [
            Asset("Data Spike", "Used in battles."),
            Asset("Data Spike", "Used in battles."),
            Asset("Removable Drive", "Found in rigs and used for extraction."),
        ]

    def name(self):
        return self.__name

    def damage(self):
        return self.__damage

    def broken(self):
        return self.__broken

    def upgrade_level(self):
        return self.__upgrade_level

    def storage(self):
        return self.__storage

    def take_hit(self):
        self.__damage +=1
        if self.__damage >=2 and self.__upgrade_level ==0:
            self.__broken = True

