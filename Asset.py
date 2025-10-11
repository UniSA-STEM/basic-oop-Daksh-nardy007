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
        self.name = name
        self.description = description
        self.encrypted = encrypted

    def __str__(self) -> str:
        if self.encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        return f"{self.name}: {self.description}"

    def encrypt(self) -> None:
        self.encrypted = True

    def decrypt(self) -> None:
        self.encrypted = False