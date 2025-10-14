"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Daksh Narang
ID: 110402115
Username: nardy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name: str, description: str, encrypted: bool = False):
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    def __str__(self):
        if self.get_encrypted():
            return f"{self.name}: {self.description} [Encrypted]"
        return f"{self.name}: {self.description}"

    def encrypt(self):
        self.__encrypted = True

    def decrypt(self):
        self.__encrypted = False

    def get_encrypted(self):
        return self.__encrypted

    def get_name(self):
        return self.__name

