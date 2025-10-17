"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Daksh Narang
ID: 110402115
Username: nardy007
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig

Trace_threshold = 5
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

    def _take_from_inventory(self, name):
        index = 0
        for a in self.__inventory:
            if a.name() == name:
                return self.__inventory.pop(index)
            index += 1
        return None

    def _peek_inventory(self, name):
        for a in self.__inventory:
            if a.name() == name:
                return a
        return None

    def _blocked(self):
        return self.__trace_level > Trace_threshold

    def acquire_rig(self, rig_name):
        if self.__rig:
            return False
        token = self._take_from_inventory("CryptoToken")
        if not token:
            return False
        self.__rig = Rig(rig_name)
        print(f"Rig Activated {rig_name}")
        return True

    def upgrade_rig(self):
        if not self.__rig:
            return False
        if self._blocked():
            print("Trace too high")
            return False
        patch = self._take_from_inventory("Hardware Patch")
        if not patch:
            print("No Hardware Patch available")
            return False
        return self.__rig.upgrade(patch)

    def repair_rig(self):
        if not self.__rig:
            return False
        token = self._take_from_inventory("CryptoToken")
        if not token:
            print("No token to repairs.")
            return False
        return self.__rig.repair(token)

    def retrieve_from_rig(self, name):
        if not self.__rig:
            return False
        item_asset = self.__rig.release(name)
        if not item_asset:
            return False
        self.__inventory.append(item_asset)
        return True

    def store_to_rig(self,name):
        if not self.__rig:
            return False
        item = self._take_from_inventory(name)
        if not item:
            return False
        self.__rig.store(item)
        return True

    def encrypt_asset(self, where, name):
        target = None
        if not self.__rig:
            return False
        if where == "inventory":
            for asset in self.__inventory:
                if asset.name() == name:
                    target = asset
                    break
        elif where == "rig":
            for asset in self.__rig.storage():
                if asset.name() == name:
                    target = asset
                    break
        else:
            return False

        is_encrypted = target.encrypted()
        if is_encrypted:
            target.decrypt()
            print("Asset decrypted successfully")
        else:
            target.encrypt()
            print("Asset encrypted successfully")
        return True

