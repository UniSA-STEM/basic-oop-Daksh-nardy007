"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Daksh Narang
ID: 110402115
Username: nardy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:

    def __init__(self, name: str):
        self.name = name
        self.damage = 0
        self.broken = False
        self.upgrade_level = 0
        self.storage= [
            Asset("Data Spike", "Used in battles."),
            Asset("Data Spike", "Used in battles."),
            Asset("Removable Drive", "Found in rigs and used for extraction."),
        ]

    def take_hit(self):
        self.damage +=1
        if self.damage >=2 and self.upgrade_level ==0:
            self.broken = True