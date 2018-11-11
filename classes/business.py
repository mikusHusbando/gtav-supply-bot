# -*- coding: utf-8 -*-
class business:
    def get_business_details(self,name):
        for b in self.business:
            if b['type'] == name:
                return b
        return None
    def __init__(self):
        # https://docs.google.com/spreadsheets/d/1mX8wGG1Oy76nhv-tBZ-oPmKiynng8fMS87EMxmoyB0Y/htmlview#gid=827245973
        self.business = [
        {'type': 'bunker', 'supply_tick_seconds': 84},
        {'type': 'coke',   'supply_tick_seconds': 72},
        {'type': 'meth',   'supply_tick_seconds': 90},
        {'type': 'cash',   'supply_tick_seconds': 96},
        {'type': 'weed',   'supply_tick_seconds': 120},
        {'type': 'docs',   'supply_tick_seconds': 90}]
    #def __init__(self, owner, type, stock = 0, supplies, upgrades = ):
    #    self.owner = owner
    #    self.type = type
    #    self.stock = stock
    #    self.supplies = supplies
    #   self.upgrades = upgrades
