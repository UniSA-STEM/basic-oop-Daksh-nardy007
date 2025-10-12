"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Daksh Narang
ID: 110402115
Username: nardy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
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

    def condition(self):
        if self.broken:
            return f"Broken (Level{self.upgrade_level})"

        if self.damage ==0:
            return f"Pristine (Level {self.upgrade_level})"

        return f"Damages ({self.damage}) (Level {self.upgrade_level})"
    def __str__(self):

        if not self.storage:
            str_Item = "Empty Rig"
        else:
            str_Item =""
            x=0
            for asst in self.storage:
                str_Item += asst.__str__()
                if x < len(self.storage)-1:
                    str_Item += ", "
                x+=1
        return f"Rig Name:{self.name} | {self.condition()} | Assets stored: {str_Item}"



