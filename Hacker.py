"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Daksh Narang
ID: 110402115
Username: nardy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Hacker:

    def __init__(self, name):
        self.__name = name
        self.__trace_level = 0
        self.__inventory = [Asset("CryptoToken", "Used to acquire or repair rigs."), ]
        self.__rig = None

    def get_name(self):
        return self.__name

    def get_trace_level(self):
        return self.__trace_level

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def set_trace_level(self, value):
        self.__trace_level = value

    def set_rig(self, rig):
        self.__rig = rig

