"""
File: Asset.py
Description: Defines Asset class
Author: Daksh Narang
ID: 110402115
Username: nardy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self, name, description, encrypted=False):
        # Private attributes for encapsulation
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted

    def __str__(self):
        # Display name and description, show [Encrypted] if applicable
        if self.encrypted():
            return f"{self.name()}: {self.description()} [Encrypted]"
        return f"{self.name()}: {self.description()}"

    def encrypt(self):
        # Mark asset as encrypted
        self.__encrypted = True

    def decrypt(self):
        # Mark asset as decrypted
        self.__encrypted = False

    def name(self):
        # Return asset name
        return self.__name

    def description(self):
        # Return asset description
        return self.__description

    def encrypted(self):
        # Return True if asset is encrypted
        return self.__encrypted


