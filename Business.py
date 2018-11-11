class Business:

    # https://docs.google.com/spreadsheets/d/1mX8wGG1Oy76nhv-tBZ-oPmKiynng8fMS87EMxmoyB0Y/htmlview#gid=827245973

    business = [
        {'type': 'bunker', 'supply_tick_seconds': 84},
        {'type': 'coke',   'supply_tick_seconds': 72},
        {'type': 'meth',   'supply_tick_seconds': 90},
        {'type': 'cash',   'supply_tick_seconds': 96},
        {'type': 'weed',   'supply_tick_seconds': 120},
        {'type': 'docs',   'supply_tick_seconds': 90}]

    def __init__(self, owner, type, stock = 0, supplies, upgrades = ):
        self.owner = owner
        self.type = type
        self.stock = stock
        self.supplies = supplies
        self.upgrades = upgrades
