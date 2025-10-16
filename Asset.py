"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Daksh Narang
ID: 110402115
Username: nardy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self, name, description, encrypted=False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    def __str__(self):
        if self.encrypted():
            return f"{self.name()}: {self.description()} [Encrypted]"
        return f"{self.name}: {self.description}"

    def encrypt(self):
        self.__encrypted = True

    def decrypt(self):
        self.__encrypted = False

    def name(self):
        return self.__name

    def description(self):
        return self.__description

    def encrypted(self):
        return self.__encrypted


