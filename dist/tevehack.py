# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                        class declarations
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    1: integer of a PlayerID, usually == 2, but on initialization \ during loading == 0;
        there's a bug with it at 14707, 46037 and 64922, it's never == 1
    2: integer of a PlayerID, usually == 1, but on initialization == 0
    3: food used by Player (by ID)
    4: Profession level, integer of a PlayerID, during initialization \ loading == 0
    5: Something connected to the profession (fishing). Either 1 (after giving the first FishingRod),
        or 0 (when unlearning), during initialization \ loading == 0
    6: Fishing profession points (rank), during initialization \ loading == 0.
        0 = "Never caught a fish"
        1 = "Fishing Newbie"
        2 = "Journeyman Fisherman"
        3 = "Expert Fisherman"
        4 = "Master Fisherman"
        5 = "Legendary Fisherman"
    7: Revival location, an integer
    8. imp5Stage, an integer
    9: usually == 1
    10: hash of a PlayerID's hero
    11: Hero XP
    12: Hero LocationX
    13: Hero LocationY
    14: 2*n(0-4) abilities of a PlayerID's hero:
        1: ability index of GU array of abilities
        2: ability level
    15: checksum
    ~~~ At this point the hero code is generated ~~~
    ~~~     Also set hu = OU[lU], set nu = 1     ~~~
    1: Gold, not more than 1010010
    2: Shards, not more than 477
    3: Some "PvP points"
    4: Some "Unlocked Critter Tiers"
    5: inventory:
        1: number of items carried
        x6 items:
            1: item ID from Yu[] \ 30 if empty
            2: amount of this item if stackable \ 0 otherwise
    6: stash inventory:
        1: number of items carried
        x6 items:
            1: item ID from Yu[] \ 30 if empty
            2: amount of this item if stackable \ 0 otherwise
    7: checksum
"""

class Ability:
    def __init__(self, id, level):
        self.id: int = id
        self.level: int = level


class Item:
    def __init__(self, id, amount):
        self.id: int = id
        self.amount: int = amount


class HeroCodeFields:
    def __init__(self, int1, int2, food, professionLvl, hasFishingRod,
        professionRank, revivalLocation, imp5Stage, int3, heroID, heroXP, locationX, locationY):
        self.int1: int = int1
        self.int2: int = int2
        self.food: int = food
        self.professionLvl: int = professionLvl
        self.hasFishingRod: int = hasFishingRod
        self.professionRank: str = professionRank
        self.revivalLocation: int = revivalLocation
        self.imp5Stage: int = imp5Stage
        self.int3: int = int3
        self.heroID: str = heroID
        self.heroXP: int = heroXP
        self.locationX: int = locationX
        self.locationY: int = locationY
        self.abilities: list = []
        self.checksum: int = 0


class ItemCodeFields:
    def __init__(self, gold, shards, pvpPoints, numberOfItems, unlockedCritterTiers):
        self.gold: int = gold
        self.shards: int = shards
        self.pvpPoints: int = pvpPoints
        self.unlockedCritterTiers: int = unlockedCritterTiers
        self.numberOfItems: int = numberOfItems
        self.items: dict = {}
        self.numberOfStashItems: int = 0
        self.stashItems: dict = {}
        self.checksum: int = 0
    


ProfessionRank = {
    'Never caught a fish': 0,
    'Fishing Newbie': 1,
    'Journeyman Fisherman': 2,
    'Expert Fisherman': 3,
    'Master Fisherman': 4,
    'Legendary Fisherman': 5,
    0: 'Never caught a fish',
    1: 'Fishing Newbie',
    2: 'Journeyman Fisherman',
    3: 'Expert Fisherman',
    4: 'Master Fisherman',
    5: 'Legendary Fisherman'
}

Hero = {
    "Acolyte (Male)": 1,
    "Acolyte (Female)": 2,
    "Archer": 3,
    "Druid": 4,
    "Initiate": 5,
    "Novice (Female)": 6,
    "Novice (Male)": 7,
    "Swordsman": 8,
    "Templar": 9,
    "Thief": 10,
    "Witch Hunter": 11,
    "ArchDruid": 12,
    "ArchTemplar": 13,
    "Cleric (Male)": 14,
    "Cleric (Female)": 15,
    "Hunter": 16,
    "Knight": 17,
    "Mage": 18,
    "Rogue": 19,
    "Slayer": 20,
    "Assassin": 21,
    "Stalker": 22,
    "Imperial Knight": 23,
    "Crusader": 24,
    "High Templar": 25,
    "Dark Templar": 26,
    "Marksman": 27,
    "Tracker": 28,
    "Witcher": 29,
    "Inquisitor": 30,
    "Priest": 31,
    "Matriarch": 32,
    "Wizard": 33,
    "Sage": 34,
    "Shaman": 35,
    "Shapeshifter": 36,
    "ArchSage": 37,
    "White Wizard": 38,
    "Hierophant": 39,
    "Prophetess": 40,
    "Sniper": 41,
    "Monster Hunter": 42,
    "Avenger": 43,
    "Champion": 44,
    "Dark ArchTemplar": 45,
    "Grand Inquisitor": 46,
    "Grand Templar": 47,
    "Master Stalker": 48,
    "Phantom Assassin": 49,
    "Professional Witcher": 50,
    "RuneMaster": 51,
    "Summoner": 52,
    1: "Acolyte (Male)",
    2: "Acolyte (Female)",
    3: "Archer",
    4: "Druid",
    5: "Initiate",
    6: "Novice (Female)",
    7: "Novice (Male)",
    8: "Swordsman",
    9: "Templar",
    10: "Thief",
    11: "Witch Hunter",
    12: "ArchDruid",
    13: "ArchTemplar",
    14: "Cleric (Male)",
    15: "Cleric (Female)",
    16: "Hunter",
    17: "Knight",
    18: "Mage",
    19: "Rogue",
    20: "Slayer",
    21: "Assassin",
    22: "Stalker",
    23: "Imperial Knight",
    24: "Crusader",
    25: "High Templar",
    26: "Dark Templar",
    27: "Marksman",
    28: "Tracker",
    29: "Witcher",
    30: "Inquisitor",
    31: "Priest",
    32: "Matriarch",
    33: "Wizard",
    34: "Sage",
    35: "Shaman",
    36: "Shapeshifter",
    37: "ArchSage",
    38: "White Wizard",
    39: "Hierophant",
    40: "Prophetess",
    41: "Sniper",
    42: "Monster Hunter",
    43: "Avenger",
    44: "Champion",
    45: "Dark ArchTemplar",
    46: "Grand Inquisitor",
    47: "Grand Templar",
    48: "Master Stalker",
    49: "Phantom Assassin",
    50: "Professional Witcher",
    51: "RuneMaster",
    52: "Summoner"
}

ItemName = {
    "Fine Sword": 1,
    "Plated Shield": 2,
    "Staff": 3,
    "Minor Potion of Healing": 4,
    "Minor Potion of Mana": 5,
    "Sharp Claws": 6,
    "Blackpowder Musket": 7,
    "Crystal Wand": 8,
    "Elderwood Bow": 9,
    "Moon Armor": 10,
    "Superior Wand": 11,
    "FrostShield": 12,
    "Frostfang": 13,
    "Elder Rod": 14,
    "Dull Warp Blade": 15,
    "Leather Armor": 16,
    "Lucky Amulet": 17,
    "Potion of Health": 18,
    "Greater Potion of Mana": 19,
    "Psi Blade": 20,
    "Reinforced Armor": 21,
    "Stitches' Dagger": 22,
    "Stitches' Totem": 23,
    "Aiur's Legacy": 24,
    "BlackGrave Wand": 25,
    "Skull Staff": 26,
    "Stitches' Legacy": 27,
    "Clarity Potion": 28,
    "Super Clarity Potion": 29,
    "Potion of Super Restoration": 31,
    "Belt of Endurance": 32,
    "Boots of Speed": 33,
    "Boots of the Eagle": 34,
    "Bracers of the Bear": 35,
    "Celestial Orb": 36,
    "Enchanted Axe": 37,
    "Arcane Staff": 38,
    "Cunning Edge": 39,
    "Firebrand": 40,
    "Helmet of Valor": 41,
    "Long Rifle": 42,
    "Ring of Melitele": 43,
    "Psionic Cuirass": 44,
    "Scroll of the Lich": 45,
    "Shield of the Avenger": 46,
    "Sniper Rifle": 47,
    "Soul Wand": 48,
    "VanCliffe's Armor": 49,
    "Warchief's Pride": 50,
    "Blood Diamond": 51,
    "Chillrend": 52,
    "Dusk's Legacy": 53,
    "Mythpowder Rifle": 54,
    "Sword of Blessed Flame": 55,
    "Scroll of Teleportation": 56,
    "Arcane Amulet": 57,
    "Claws of Striking": 58,
    "Elven Armor": 59,
    "Superior Vizima Gauntlets": 60,
    "Circlet": 61,
    "Sharpened Glaive": 62,
    "Slicer": 63,
    "Stout Shield": 64,
    "Worn Gauntlets": 65,
    "Horadric Staff": 66,
    "The Executioner": 67,
    "Windforce": 68,
    "The Ark Royal": 71,
    "The Spirit Shroud": 72,
    "The Stone of Jordan": 73,
    "Doombringer": 75,
    "Frostbrand": 77,
    "Homunculus": 78,
    "Guardian Naga": 79,
    "Death Reaver": 80,
    "Ghost Armor": 81,
    "Guardian Angel": 83,
    "Hand of Blessed Light": 84,
    "Azurewrath": 85,
    "Synergy Blade": 86,
    "Hand of God": 87,
    "Psionic Stone": 88,
    "The Psionic Razor": 89,
    "The Heart of Evo": 90,
    "Double-Barrel Rifle": 91,
    "The Pendant of Nagre": 92,
    "Lam Esen's Tome": 93,
    "Infernostride": 94,
    "Battle Gauntlets": 95,
    "Atma's Defence": 96,
    "Feral Totem": 97,
    "Tome of Awakening": 98,
    "Hades' Shield": 99,
    "Bethrezen's Flame": 100,
    "Golden Arrows": 101,
    "Necklace of Seven Souls": 102,
    "Stone of Vsmir": 103,
    "Duriel's Shell": 104,
    "Hexfire's Edge": 105,
    "Icecrown's Visage": 106,
    "Megaton Blades": 107,
    "Staff of the Ages": 108,
    "Tome of the Unlife": 109,
    "Zakarum's Hand": 110,
    "Angel's Sanctuary": 113,
    "Athena's Aim": 114,
    "Dawn's Legacy": 116,
    "Eagle Eye": 117,
    "Titan's Aegis": 121,
    "Shield of Unending Flame": 123,
    "Phoenix's Stone": 124,
    "Good Fishing Rod": 133,
    "Basic Fishing Rod": 134,
    "Mastercraft Fishing Rod": 135,
    "Mystic Fishing Rod": 136,
    "Silver Fishing Rod": 137,
    "Fanged Piranah": 138,
    "Flying Wish Fish": 139,
    "Goldskin": 140,
    "King Bass": 141,
    "Mutated Bluefish": 142,
    "Rainbow Fish": 143,
    "Salmon": 144,
    "Thunderfish": 145,
    "Trout": 146,
    "Tuna": 147,
    "Yellowskin Bass": 148,
    "Faded Inspirit": 157,
    "Glowing Inspirit": 186,
    "Faith": 158,
    "Fate": 159,
    "Raising Heart": 160,
    "Reinforce": 161,
    "Rune Sihill": 162,
    "Tooth of Belial": 163,
    "Whirlwind": 164,
    "Hope": 165,
    "Potion of Restoration": 166,
    "Raven's Insight": 177,
    "The Grandfather": 167,
    "The Patriarch": 168,
    "Atlantean's Frozen Heart": 169,
    "Atlantean's Frozen Heart": 170,
    "Neptune's Eye": 171,
    "Atalanta's Speed": 172,
    "Black Hades": 173,
    "Raven's Legacy": 187,
    "Hannah's Legend": 174,
    "Wrath of the Lich King": 175,
    "Blaze's Touch": 176,
    "Megaera's Edge": 178,
    "Chaos Grief": 179,
    "Hellforge Plate": 180,
    "Atalanta's Revenge": 183,
    "Life Essence": 181,
    "Mana Essence": 182,
    "The Destiny": 184,
    "Stabilized Void Prism": 185,
    1: "Fine Sword",
    2: "Plated Shield",
    3: "Staff",
    4: "Minor Potion of Healing",
    5: "Minor Potion of Mana",
    6: "Sharp Claws",
    7: "Blackpowder Musket",
    8: "Crystal Wand",
    9: "Elderwood Bow",
    10: "Moon Armor",
    11: "Superior Wand",
    12: "FrostShield",
    13: "Frostfang",
    14: "Elder Rod",
    15: "Dull Warp Blade",
    16: "Leather Armor",
    17: "Lucky Amulet",
    18: "Potion of Health",
    19: "Greater Potion of Mana",
    20: "Psi Blade",
    21: "Reinforced Armor",
    22: "Stitches' Dagger",
    23: "Stitches' Totem",
    24: "Aiur's Legacy",
    25: "BlackGrave Wand",
    26: "Skull Staff",
    27: "Stitches' Legacy",
    28: "Clarity Potion",
    29: "Super Clarity Potion",
    31: "Potion of Super Restoration",
    32: "Belt of Endurance",
    33: "Boots of Speed",
    34: "Boots of the Eagle",
    35: "Bracers of the Bear",
    36: "Celestial Orb",
    37: "Enchanted Axe",
    38: "Arcane Staff",
    39: "Cunning Edge",
    40: "Firebrand",
    41: "Helmet of Valor",
    42: "Long Rifle",
    43: "Ring of Melitele",
    44: "Psionic Cuirass",
    45: "Scroll of the Lich",
    46: "Shield of the Avenger",
    47: "Sniper Rifle",
    48: "Soul Wand",
    49: "VanCliffe's Armor",
    50: "Warchief's Pride",
    51: "Blood Diamond",
    52: "Chillrend",
    53: "Dusk's Legacy",
    54: "Mythpowder Rifle",
    55: "Sword of Blessed Flame",
    56: "Scroll of Teleportation",
    57: "Arcane Amulet",
    58: "Claws of Striking",
    59: "Elven Armor",
    60: "Superior Vizima Gauntlets",
    61: "Circlet",
    62: "Sharpened Glaive",
    63: "Slicer",
    64: "Stout Shield",
    65: "Worn Gauntlets",
    66: "Horadric Staff",
    67: "The Executioner",
    68: "Windforce",
    71: "The Ark Royal",
    72: "The Spirit Shroud",
    73: "The Stone of Jordan",
    75: "Doombringer",
    77: "Frostbrand",
    78: "Homunculus",
    79: "Guardian Naga",
    80: "Death Reaver",
    81: "Ghost Armor",
    83: "Guardian Angel",
    84: "Hand of Blessed Light",
    85: "Azurewrath",
    86: "Synergy Blade",
    87: "Hand of God",
    88: "Psionic Stone",
    89: "The Psionic Razor",
    90: "The Heart of Evo",
    91: "Double-Barrel Rifle",
    92: "The Pendant of Nagre",
    93: "Lam Esen's Tome",
    94: "Infernostride",
    95: "Battle Gauntlets",
    96: "Atma's Defence",
    97: "Feral Totem",
    98: "Tome of Awakening",
    99: "Hades' Shield",
    100: "Bethrezen's Flame",
    101: "Golden Arrows",
    102: "Necklace of Seven Souls",
    103: "Stone of Vsmir",
    104: "Duriel's Shell",
    105: "Hexfire's Edge",
    106: "Icecrown's Visage",
    107: "Megaton Blades",
    108: "Staff of the Ages",
    109: "Tome of the Unlife",
    110: "Zakarum's Hand",
    113: "Angel's Sanctuary",
    114: "Athena's Aim",
    116: "Dawn's Legacy",
    117: "Eagle Eye",
    121: "Titan's Aegis",
    123: "Shield of Unending Flame",
    124: "Phoenix's Stone",
    133: "Good Fishing Rod",
    134: "Basic Fishing Rod",
    135: "Mastercraft Fishing Rod",
    136: "Mystic Fishing Rod",
    137: "Silver Fishing Rod",
    138: "Fanged Piranah",
    139: "Flying Wish Fish",
    140: "Goldskin",
    141: "King Bass",
    142: "Mutated Bluefish",
    143: "Rainbow Fish",
    144: "Salmon",
    145: "Thunderfish",
    146: "Trout",
    147: "Tuna",
    148: "Yellowskin Bass",
    157: "Faded Inspirit",
    186: "Glowing Inspirit",
    158: "Faith",
    159: "Fate",
    160: "Raising Heart",
    161: "Reinforce",
    162: "Rune Sihill",
    163: "Tooth of Belial",
    164: "Whirlwind",
    165: "Hope",
    166: "Potion of Restoration",
    177: "Raven's Insight",
    167: "The Grandfather",
    168: "The Patriarch",
    169: "Atlantean's Frozen Heart",
    170: "Atlantean's Frozen Heart",
    171: "Neptune's Eye",
    172: "Atalanta's Speed",
    173: "Black Hades",
    187: "Raven's Legacy",
    174: "Hannah's Legend",
    175: "Wrath of the Lich King",
    176: "Blaze's Touch",
    178: "Megaera's Edge",
    179: "Chaos Grief",
    180: "Hellforge Plate",
    183: "Atalanta's Revenge",
    181: "Life Essence",
    182: "Mana Essence",
    184: "The Destiny",
    185: "Stabilized Void Prism"
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                        global variables
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

au = {}
oU = {}
OU = {}
lU = 0
Fu = False
Qu = False
hu = ''
qu = None
nu = 0
fu = False
ku = False
Tu = {}
ju = 0
Yu = {}
xu = 0
Gu = {}
gu = 0
du = {}
Ru = {}
Iu = 0
bj_forLoopBIndex = 0
player_name = ''

keep_hash = False
name_hash = 0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                     function definitions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 70957 ftw
def pEw():  # Init function, takes nothing returns nothing
    global xu, ju, gu, hu, Fu, ku, Qu, qu, nu, fu
    Tu[0x1] = 1211117623
    Tu[0x2] = 1211117620
    Tu[0x3] = 1211117634
    Tu[0x4] = 1211117622
    Tu[0x5] = 1211117621
    Tu[0x6] = 1211117617
    Tu[0x7] = 1211117618
    Tu[0x8] = 1211117619
    Tu[0x9] = 1211117633
    Tu[0xA] = 1211117624
    Tu[0xB] = 1211117625
    Tu[0xC] = 1211117640
    Tu[0xD] = 1211117643
    Tu[0xE] = 1211117637
    Tu[0xF] = 1211117638
    Tu[0x10] = 1211117639
    Tu[0x11] = 1211117642
    Tu[0x12] = 1211117641
    Tu[0x13] = 1211117644
    Tu[0x14] = 1211117645
    Tu[0x15] = 1211117873
    Tu[0x16] = 1211117872
    Tu[0x17] = 1211117874
    Tu[0x18] = 1211117875
    Tu[0x19] = 1211117892
    Tu[0x1A] = 1211117891
    Tu[0x1B] = 1211117877
    Tu[0x1C] = 1211117876
    Tu[0x1D] = 1211117894
    Tu[0x1E] = 1211117893
    Tu[0x1F] = 1211117890
    Tu[0x20] = 1211117889
    Tu[0x21] = 1211117879
    Tu[0x22] = 1211117878
    Tu[0x23] = 1211117881
    Tu[0x24] = 1211117880
    Tu[0x25] = 1211118131
    Tu[0x26] = 1211118132
    Tu[0x27] = 1211118147
    Tu[0x28] = 1211118146
    Tu[0x29] = 1211118149
    Tu[0x2A] = 1211118150
    Tu[0x2B] = 1211118155
    Tu[0x2C] = 1211118152
    Tu[0x2D] = 1211118157
    Tu[0x2E] = 1211118161
    Tu[0x2F] = 1211118156
    Tu[0x30] = 1211118159
    Tu[0x31] = 1211118158
    Tu[0x32] = 1211118160
    Tu[0x33] = 1211118162
    Tu[0x34] = 1211118163
    ju = 52
    Yu[0x1] = 1227894835
    Yu[0x2] = 1227894833
    Yu[0x3] = 1227894834
    Yu[0x4] = 1227894840
    Yu[0x5] = 1227894841
    Yu[0x6] = 1227894850
    Yu[0x7] = 1227894839
    Yu[0x8] = 1227894851
    Yu[0x9] = 1227894838
    Yu[0xA] = 1227894836
    Yu[0xB] = 1227894852
    Yu[0xC] = 1227894853
    Yu[0xD] = 1227894837
    Yu[0xE] = 1227894855
    Yu[0xF] = 1227894856
    Yu[0x10] = 1227894858
    Yu[0x11] = 1227894857
    Yu[0x12] = 1227894849
    Yu[0x13] = 1227894854
    Yu[0x14] = 1227894866
    Yu[0x15] = 1227894864
    Yu[0x16] = 1227894863
    Yu[0x17] = 1227894861
    Yu[0x18] = 1227894860
    Yu[0x19] = 1227894865
    Yu[0x1A] = 1227894862
    Yu[0x1B] = 1227894867
    Yu[0x1C] = 1227895111
    Yu[0x1D] = 1227895110
    Yu[0x1F] = 1227895109
    Yu[0x20] = 1227895116
    Yu[0x21] = 1227895125
    Yu[0x22] = 1227895347
    Yu[0x23] = 1227895128
    Yu[0x24] = 1227895112
    Yu[0x25] = 1227895348
    Yu[0x26] = 1227895123
    Yu[0x27] = 1227895115
    Yu[0x28] = 1227895344
    Yu[0x29] = 1227895345
    Yu[0x2A] = 1227895113
    Yu[0x2B] = 1227895124
    Yu[0x2C] = 1227895121
    Yu[0x2D] = 1227895122
    Yu[0x2E] = 1227895114
    Yu[0x2F] = 1227895120
    Yu[0x30] = 1227895130
    Yu[0x31] = 1227895346
    Yu[0x32] = 1227895117
    Yu[0x33] = 1227895129
    Yu[0x34] = 1227895119
    Yu[0x35] = 1227895118
    Yu[0x36] = 1227895126
    Yu[0x37] = 1227895127
    Yu[0x38] = 1227895350
    Yu[0x39] = 1227895366
    Yu[0x3A] = 1227895353
    Yu[0x3B] = 1227895363
    Yu[0x3C] = 1227895368
    Yu[0x3D] = 1227895367
    Yu[0x3E] = 1227895364
    Yu[0x3F] = 1227895361
    Yu[0x40] = 1227895362
    Yu[0x41] = 1227895365
    Yu[0x42] = 1227895369
    Yu[0x43] = 1227895371
    Yu[0x44] = 1227895370
    Yu[0x47] = 1227895383
    Yu[0x48] = 1227895376
    Yu[0x49] = 1227895377
    Yu[0x4B] = 1227895384
    Yu[0x4D] = 1227895372
    Yu[0x4E] = 1227895381
    Yu[0x4F] = 1227895380
    Yu[0x50] = 1227895374
    Yu[0x51] = 1227895382
    Yu[0x53] = 1227895375
    Yu[0x54] = 1227895378
    Yu[0x55] = 1227895373
    Yu[0x56] = 1227895600
    Yu[0x57] = 1227895603
    Yu[0x58] = 1227895604
    Yu[0x59] = 1227895609
    Yu[0x5A] = 1227895606
    Yu[0x5B] = 1227895607
    Yu[0x5C] = 1227895617
    Yu[0x5D] = 1227895619
    Yu[0x5E] = 1227895618
    Yu[0x5F] = 1227895605
    Yu[0x60] = 1227895608
    Yu[0x61] = 1227895623
    Yu[0x62] = 1227895622
    Yu[0x63] = 1227895625
    Yu[0x64] = 1227895624
    Yu[0x65] = 1227895628
    Yu[0x66] = 1227895630
    Yu[0x67] = 1227895634
    Yu[0x68] = 1227895638
    Yu[0x69] = 1227895633
    Yu[0x6A] = 1227895629
    Yu[0x6B] = 1227895636
    Yu[0x6C] = 1227895627
    Yu[0x6D] = 1227895637
    Yu[0x6E] = 1227895635
    Yu[0x71] = 1227895640
    Yu[0x72] = 1227895639
    Yu[0x74] = 1227895641
    Yu[0x75] = 1227895861
    Yu[0x79] = 1227895642
    Yu[0x7B] = 1227895632
    Yu[0x7C] = 1227895631
    Yu[0x85] = 1227895898
    Yu[0x86] = 1227895895
    Yu[0x87] = 1227895894
    Yu[0x88] = 1227895897
    Yu[0x89] = 1227895896
    Yu[0x8A] = 1227896118
    Yu[0x8B] = 1227896116
    Yu[0x8C] = 1227896115
    Yu[0x8D] = 1227896121
    Yu[0x8E] = 1227896120
    Yu[0x8F] = 1227896114
    Yu[0x90] = 1227896129
    Yu[0x91] = 1227896117
    Yu[0x92] = 1227896113
    Yu[0x93] = 1227896112
    Yu[0x94] = 1227896119
    Yu[0x9D] = 1227896136
    Yu[0x9E] = 1227895386
    Yu[0x9F] = 1227895862
    Yu[0xA0] = 1227895886
    Yu[0xA1] = 1227895887
    Yu[0xA2] = 1227895888
    Yu[0xA3] = 1227895863
    Yu[0xA4] = 1227896135
    Yu[0xA5] = 1227896134
    Yu[0xA6] = 1227895108
    Yu[0xA7] = 1227895858
    Yu[0xA8] = 1227895856
    Yu[0xA9] = 1227895860
    Yu[0xAA] = 1227895860
    Yu[0xAB] = 1227895857
    Yu[0xAC] = 1227895883
    Yu[0xAD] = 1227895385
    Yu[0xAE] = 1227895884
    Yu[0xAF] = 1227895882
    Yu[0xB0] = 1227895885
    Yu[0xB1] = 1227896138
    Yu[0xB2] = 1227895880
    Yu[0xB3] = 1227896139
    Yu[0xB4] = 1227896140
    Yu[0xB7] = 1227896137
    Yu[0xB5] = 1227895602
    Yu[0xB6] = 1227895601
    Yu[0xB8] = 1229210963
    xu = 184
    Gu[0x1] = 1093677109
    Gu[0x2] = 1093677108
    Gu[0x3] = 1093677104
    Gu[0x4] = 1093677105
    Gu[0x5] = 1093677107
    Gu[0x6] = 1093677106
    Gu[0x7] = 1093677112
    Gu[0x8] = 1093677110
    Gu[0x9] = 1093677113
    Gu[0xA] = 1093677111
    Gu[0xB] = 1093677133
    Gu[0xC] = 1093677132
    Gu[0xD] = 1093677131
    Gu[0xE] = 1093677134
    Gu[0xF] = 1093677127
    Gu[0x10] = 1093677125
    Gu[0x11] = 1093677128
    Gu[0x12] = 1093677126
    Gu[0x13] = 1093677121
    Gu[0x14] = 1093677124
    Gu[0x15] = 1093677122
    Gu[0x16] = 1093677123
    Gu[0x17] = 1093677138
    Gu[0x18] = 1093677139
    Gu[0x19] = 1093677140
    Gu[0x1A] = 1093677141
    Gu[0x1B] = 1093677360
    Gu[0x1C] = 1093677362
    Gu[0x1D] = 1093677146
    Gu[0x1E] = 1093677361
    Gu[0x1F] = 1093677143
    Gu[0x20] = 1093677144
    Gu[0x21] = 1093677142
    Gu[0x22] = 1093677145
    Gu[0x23] = 1093677387
    Gu[0x24] = 1093677386
    Gu[0x25] = 1093677385
    Gu[0x26] = 1093677378
    Gu[0x27] = 1093677381
    Gu[0x28] = 1093677382
    Gu[0x29] = 1093677383
    Gu[0x2A] = 1093677384
    Gu[0x2B] = 1093677367
    Gu[0x2C] = 1093677366
    Gu[0x2D] = 1093677365
    Gu[0x2E] = 1093677368
    Gu[0x2F] = 1093677379
    Gu[0x30] = 1093677380
    Gu[0x31] = 1093677369
    Gu[0x32] = 1093677377
    Gu[0x33] = 1093677396
    Gu[0x34] = 1093677397
    Gu[0x35] = 1093677398
    Gu[0x36] = 1093677399
    Gu[0x37] = 1093677401
    Gu[0x38] = 1093677616
    Gu[0x39] = 1093677402
    Gu[0x3A] = 1093677400
    Gu[0x3B] = 1093677393
    Gu[0x3C] = 1093677392
    Gu[0x3D] = 1093677394
    Gu[0x3E] = 1093677395
    Gu[0x3F] = 1093677391
    Gu[0x40] = 1093677390
    Gu[0x41] = 1093677389
    Gu[0x42] = 1093677388
    Gu[0x43] = 1093677876
    Gu[0x44] = 1093677909
    Gu[0x45] = 1093677892
    Gu[0x46] = 1093677879
    Gu[0x47] = 1093677912
    Gu[0x48] = 1093678648
    Gu[0x49] = 1093678132
    Gu[0x4A] = 1093678133
    Gu[0x4B] = 1093677875
    Gu[0x4C] = 1093677894
    Gu[0x4D] = 1093678145
    Gu[0x4E] = 1093677904
    Gu[0x4F] = 1093677872
    Gu[0x50] = 1093677907
    Gu[0x51] = 1093677908
    Gu[0x52] = 1093677889
    Gu[0x53] = 1093677654
    Gu[0x54] = 1093677873
    Gu[0x55] = 1093677898
    Gu[0x56] = 1093677896
    Gu[0x57] = 1093677658
    Gu[0x58] = 1093677893
    Gu[0x59] = 1093677897
    Gu[0x5A] = 1093678152
    Gu[0x5B] = 1093678148
    Gu[0x5C] = 1093678150
    Gu[0x5D] = 1093677895
    Gu[0x5E] = 1093677655
    Gu[0x5F] = 1093677881
    Gu[0x60] = 1093678128
    Gu[0x61] = 1093677891
    Gu[0x62] = 1093677880
    Gu[0x63] = 1093677901
    Gu[0x64] = 1093677878
    Gu[0x65] = 1093678131
    Gu[0x66] = 1093678129
    Gu[0x67] = 1093678130
    Gu[0x68] = 1093677905
    Gu[0x69] = 1093678146
    Gu[0x6A] = 1093678137
    Gu[0x6B] = 1093678147
    Gu[0x6C] = 1093677902
    Gu[0x6D] = 1093677890
    Gu[0x6E] = 1093677906
    Gu[0x6F] = 1093677903
    Gu[0x70] = 1093678135
    Gu[0x71] = 1093678134
    Gu[0x72] = 1093678136
    Gu[0x73] = 1093677656
    Gu[0x74] = 1093677899
    Gu[0x75] = 1093677900
    Gu[0x76] = 1093677877
    Gu[0x77] = 1093677657
    Gu[0x78] = 1093677874
    Gu[0x79] = 1093678169
    Gu[0x7A] = 1093678151
    Gu[0x7B] = 1093678149
    Gu[0x7C] = 1093677652
    Gu[0x7D] = 1093677653
    Gu[0x7E] = 1093678160
    Gu[0x7F] = 1093678164
    Gu[0x80] = 1093678167
    Gu[0x81] = 1093678163
    Gu[0x82] = 1093678913
    Gu[0x83] = 1093678161
    Gu[0x84] = 1093678165
    Gu[0x85] = 1093678168
    Gu[0x86] = 1093677910
    Gu[0x87] = 1093678170
    Gu[0x88] = 1093678386
    Gu[0x89] = 1093678389
    Gu[0x8A] = 1093678409
    Gu[0x8B] = 1093678385
    Gu[0x8C] = 1093678388
    Gu[0x8D] = 1093678384
    Gu[0x8E] = 1093678390
    Gu[0x8F] = 1093678644
    Gu[0x90] = 1093678658
    Gu[0x91] = 1093677913
    Gu[0x92] = 1093678645
    Gu[0x93] = 1093678642
    Gu[0x94] = 1093681997
    Gu[0x95] = 1093678646
    Gu[0x96] = 1093678647
    Gu[0x97] = 1093678657
    Gu[0x98] = 1093678933
    Gu[0x99] = 1093678927
    Gu[0x9A] = 1093678932
    Gu[0x9B] = 1093678930
    Gu[0x9C] = 1093678931
    Gu[0x9D] = 1093678924
    Gu[0x9E] = 1093678929
    Gu[0x9F] = 1093678926
    Gu[0xA0] = 1093678928
    Gu[0xA1] = 1093678925
    Gu[0xA2] = 1093678921
    Gu[0xA3] = 1093678919
    Gu[0xA4] = 1093678918
    Gu[0xA5] = 1093678920
    Gu[0xA6] = 1093678923
    Gu[0xA7] = 1093678917
    Gu[0xA8] = 1093679436
    Gu[0xA9] = 1093678915
    Gu[0xAA] = 1093678916
    Gu[0xAB] = 1093678914
    Gu[0xAC] = 1093678901
    Gu[0xAD] = 1093678899
    Gu[0xAE] = 1093678902
    Gu[0xAF] = 1093678897
    Gu[0xB0] = 1093678896
    Gu[0xB1] = 1093678904
    Gu[0xB2] = 1093678898
    Gu[0xB3] = 1093678903
    Gu[0xB4] = 1093678900
    Gu[0xB5] = 1093678935
    Gu[0xB6] = 1093678936
    Gu[0xB7] = 1093679152
    Gu[0xB8] = 1093678937
    Gu[0xB9] = 1093678938
    Gu[0xBA] = 1093679156
    Gu[0xBB] = 1093679158
    Gu[0xBC] = 1093679153
    Gu[0xBD] = 1093679154
    Gu[0xBE] = 1093679157
    Gu[0xBF] = 1093678678
    Gu[0xC0] = 1093678680
    Gu[0xC1] = 1093678681
    Gu[0xC2] = 1093678679
    Gu[0xC3] = 1093678682
    Gu[0xC4] = 1093678392
    Gu[0xC5] = 1093678675
    Gu[0xC6] = 1093677640
    Gu[0xC7] = 1093678676
    Gu[0xC8] = 1093678677
    Gu[0xC9] = 1093681740
    Gu[0xCA] = 1093681741
    Gu[0xCB] = 1093681742
    Gu[0xCC] = 1093681743
    Gu[0xCD] = 1093681744
    Gu[0xCE] = 1093681496
    Gu[0xCF] = 1093681990
    Gu[0xD0] = 1093682007
    gu = 208
    hu = "ZWAJKLMNOPQRSTUVabcdefghjkmnopqrs8765432XYBCDEFGHtuvwxyz9"
    Fu = True
    ku = True
    Qu = False
    qu = ""
    au[1] = 0
    nu = 1
    fu = False
    du[1] = 0
    Ru[1] = 0


# 73102 rRw
def mFr():  # Init function2, takes nothing returns nothing
    global lU
    oU[0] = ""
    OU[0] = ""
    lU = 0
    kw = "EN3P29DXeruxo6RUW5ZvYFbwgQ7hfAyBztSn4sKCqHpLOajkTVdG8JmcM"
    jw = "vHGKFaXA5V72NbWruZJLxYnSR3k8Owmhepszg6oTyEDdUtqMQP4jcf9CB"
    xw = "9fb%(wgQtS+_n4s[KCqH#pLAyBz<ruxo6R-mcM>EN3PU.D7hW5]ZvYF,8J$OX/eajkTV)d*G2"
    vw = "vHmh/eps#(zFa6o&]TWruZJLxYnSR_=3k>8Ow)A5V>7yEDdU.tqMQP4jcf9,C$+BXG[*K2Nbg"
    mw = "9fb(wgQtS+_n4s[KCqH#pLAyBz<ruxo6R-mcM>EN3PU.D7hW5]ZvYF,8JOXeajkTV)d*G2"
    Qw = "]Z4sp53PU.ed*D7hW6R-mcM>ENzn9fbF,)(wgy[KS+_uxo8JOXG2qH#vYaCQtjkTVBLA<r"
    Ww = "Fs3u.hSZ6w7>LQWfz8aX<gG,trRcNkBeU2pC4Po)qOAxvb]D9dMVET(Yy+5#mHnJj*K["
    Ew = "p>wn8sv<mRHQeX7FrxqC[2K9MWdoUgf5yVGLhAZ+zJu3B#)SPbjD(OT.*c64kENY]t,a"
    Zw = "t[nFb&G.Q*co6Sar2p5Hw8JzqhsREY!VLx9(kP3NXAT>v#ZOWgMd4U)jKBD+m]u<eCy7_f?"
    Uw = "O)_CSDLxWr?6bmBvgUt5dHFQpqY[XokG9P4*yj.T<ZKe>87ERw3Mfza!+2sVc#Anu(hJN]"
    lU = 0
    oU[lU] = kw
    OU[lU] = jw
    lU += 1
    oU[lU] = xw
    OU[lU] = vw
    lU += 1
    oU[lU] = mw
    OU[lU] = Qw
    lU += 1
    oU[lU] = Ww
    OU[lU] = Ew
    lU += 1
    oU[lU] = Zw
    OU[lU] = Uw
    lU += 1
    oU[lU] = "t[nFb&G.)jKp5Hw?8,JzqCy7_fQ*co6Sar2T>v#ZOWghsEY!VLx9(kP3NXABD+m]uR<eMd4U"
    OU[lU] = "ObmBvgUt5d87ERw3Mfza!+2sVc#AnqY[XokG9P4*yu(hJNHFQpj.T,<ZKe>)_CSDLxWr?6]"
    lU += 1
    oU[lU] = "!gWY2tqxeA,Q?aT8&N9Fd6kOm]*)XscB+fZRHnEy[wM5GP#p(z<SLbCKjU_u73hDVr>vo4J"
    OU[lU] = "AZf!N[8qLhzUgCwntGW9SyDb_Pd3Qc?kM4KjvVmeJu*ap65+Y)F,BHROX<#(r]>Exs7To2"

    for i in range(1, 24):
        au[i] = -1


def encode():  # takes nothing returns string
    lWw = len(hu)  # local integer
    yWw = ""  # local string
    qWw = 1000000  # local integer
    aWw = "0123456789"  # local string
    iWw = 0  # local integer
    bWw = {}  # local integer array

    # looks like this is the input-output part
    while True:
        iWw += 1
        if iWw > nu:
            break
        yWw += str(au[iWw]) + "-"

    yWw += str(tWw(yWw))

    if au[1] == 0:
        yWw = "-" + yWw

    # a lot of weird maths
    iWw = 0
    while True:
        bWw[iWw] = 0
        iWw += 1
        if iWw >= 100:
            break

    OWw = 0
    iWw = 0
    while True:
        SWw = 0
        while True:
            bWw[SWw] = bWw[SWw] * 11
            SWw += 1
            if SWw > OWw:
                break
        oWw = 0
        pWw = yWw[iWw: iWw + 1]
        while aWw[oWw: oWw + 1] != pWw:
            oWw += 1
            if oWw > 9:
                break
        bWw[0] += oWw
        SWw = 0
        while True:
            cWw = int(bWw[SWw] / qWw)
            bWw[SWw] -= cWw * qWw
            bWw[SWw + 1] += cWw
            SWw += 1
            if SWw > OWw:
                break
        if cWw > 0:
            OWw += 1
        iWw += 1
        if iWw >= len(yWw):
            break

    # some weird maths
    yWw = ""
    while OWw >= 0:
        SWw = OWw
        while SWw > 0:
            cWw = int(bWw[SWw] / lWw)
            bWw[SWw - 1] = bWw[SWw - 1] + (bWw[SWw] - cWw * lWw) * qWw
            bWw[SWw] = cWw
            SWw -= 1
        cWw = int(bWw[SWw] / lWw)
        iWw = bWw[SWw] - cWw * lWw
        yWw = yWw + hu[iWw: iWw + 1]
        bWw[SWw] = cWw
        if bWw[OWw] == 0:
            OWw -= 1

    # this part divides the code by 4 from right to left with dashes (-)
    iWw = len(yWw)
    eWw = 0
    pWw = ""
    while iWw > 0:
        iWw -= 1
        pWw += yWw[iWw: iWw + 1]
        eWw += 1
        if eWw == 4 and iWw > 0:
            pWw += "-"
            eWw = 0

    return pWw


def ZQw(QQw: int):  # takes integer QQw returns integer
    WQw = int(QQw / (256 * 256 * 256))  # local integer
    QQw = QQw - WQw * 256 * 256 * 256
    EQw = du[WQw]
    WQw = int(QQw / (256 * 256))
    QQw = QQw - WQw * 256 * 256
    EQw = EQw * 64 + du[WQw]
    WQw = int(QQw / 256)
    EQw = EQw * 64 + du[WQw]
    return EQw * 64 + du[QQw - WQw * 256]


def mQw():  # takes nothing returns nothing
    xQw = 0  # local integer
    vQw = 0  # local integer
    while True:
        du[xQw + 48] = vQw
        Ru[xQw] = xQw + 48
        vQw += 1
        xQw += 1
        if xQw >= 10:
            break
    xQw = 0
    while True:
        du[xQw + 97] = vQw
        du[xQw + 65] = vQw + 26
        Ru[xQw + 10] = xQw + 97
        Ru[xQw + 26 + 10] = xQw + 65
        vQw += 1
        xQw += 1
        if xQw >= 26:
            break


def AQw(UQw: int):  # takes integer UQw returns integer
    IQw = int(UQw / (64 * 64 * 64))  # local integer
    UQw -= IQw * 64 * 64 * 64
    PQw = Ru[IQw]
    IQw = int(UQw / (64 * 64))
    UQw -= IQw * 64 * 64
    PQw = PQw * 256 + Ru[IQw]
    IQw = int(UQw / 64)
    PQw = PQw * 256 + Ru[IQw]
    return PQw * 256 + Ru[UQw - IQw * 64]


def rxw(uxw: int):  # takes integer uxw returns integer
    global Qu
    if not Qu:
        Qu = True
        mQw()
    if uxw <= ju:
        return Tu[uxw]
    return AQw(uxw)


def MQw(XQw: str):  # takes string returns integer (number of the character \ number in an array)
    CQw = 0  # local integer
    VQw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # local string
    BQw = "abcdefghijklmnopqrstuvwxyz"  # local string
    NQw = "0123456789"  # local string
    while True:
        if VQw[CQw: CQw + 1] == XQw:
            return CQw
        if BQw[CQw: CQw + 1] == XQw:
            return CQw
        CQw += 1
        if CQw >= 26:
            break
    CQw = 0
    while True:
        if NQw[CQw: CQw + 1] == XQw:
            return CQw
        CQw += 1
        if CQw >= 10:
            break
    return 0


def decode(dWw: str):  # takes string dWw returns boolean
    global nu, name_hash
    GWw = 0  # local integer
    FWw = ""  # local string
    kWw = len(hu)  # local integer
    jWw = -1  # local integer
    xWw = 1000000  # local integer
    vWw = "0123456789-"  # local string
    fWw = 0  # local integer
    hWw = {}  # local integer
    while True:
        hWw[fWw] = 0
        fWw += 1
        if fWw >= 100:
            break
    gWw = 0
    fWw = 0
    while True:
        RWw = 0
        while True:
            hWw[RWw] *= kWw
            RWw += 1
            if RWw > gWw:
                break
        jWw += 1
        if jWw == 4:
            jWw = 0
            fWw += 1
        YWw = kWw
        mWw = dWw[fWw: fWw + 1]
        while True:
            YWw -= 1
            if YWw < 1:
                break
            if hu[YWw: YWw + 1] == mWw:
                break
        hWw[0] += YWw
        RWw = 0
        while True:
            TWw = int(hWw[RWw] / xWw)
            hWw[RWw] -= TWw * xWw
            hWw[RWw + 1] += TWw
            RWw += 1
            if RWw > gWw:
                break
        if TWw > 0:
            gWw += 1
        fWw += 1
        if fWw >= len(dWw):
            break
    while gWw >= 0:
        RWw = gWw
        while RWw > 0:
            TWw = int(hWw[RWw] / 11)
            hWw[RWw - 1] += (hWw[RWw] - TWw * 11) * xWw
            hWw[RWw] = TWw
            RWw -= 1
        TWw = int(hWw[RWw] / 11)
        fWw = hWw[RWw] - TWw * 11
        FWw = vWw[fWw: fWw + 1] + FWw
        hWw[RWw] = TWw
        if hWw[gWw] == 0:
            gWw -= 1
    fWw = 0
    RWw = 0
    while True:
        while fWw < len(FWw):
            if fWw > 0 and FWw[fWw: fWw + 1] == "-" and FWw[fWw - 1: fWw] != "-":
                break
            fWw += 1
        if fWw < len(FWw):
            TWw = fWw
        GWw += 1
        try:
            au[GWw] = int(FWw[RWw: fWw])
        except ValueError:
            return False
        RWw = fWw + 1
        fWw += 1
        if fWw >= len(FWw):
            break
    RWw = tWw(FWw[:TWw])
    nu = GWw - 1
    # if RWw == au[GWw]:
    #     return True
    # return False
    # return True

    name_hash = au[GWw] - RWw
    return validate()


def tWw(wWw: str):  # takes string wWw returns integer, calculates the hash
    uWw = 0  # local integer
    rWw = 0  # local integer
    if keep_hash:
        rWw += name_hash
    else:
        sWw = player_name  # local string
        if ku:
            while True:
                rWw += MQw(sWw[uWw: uWw + 1])
                uWw += 1
                if uWw >= len(sWw):
                    break
    uWw = 0
    while True:
        rWw += MQw(wWw[uWw: uWw + 1])
        uWw += 1
        if uWw >= len(wWw):
            break
    return rWw


def Cjw(Xjw: str):  # takes string Xjw returns boolean
    global Fu, hu
    if not Fu:
        hu = hu.upper()
        Xjw = Xjw.upper()
    return decode(Xjw)


def tkr(ukr: str):  # takes string ukr returns boolean
    global hu, qu, fu
    rkr = False  # local boolean
    skr = lU  # local integer
    while skr >= 0:
        hu = oU[skr]
        qu = ukr
        fu = Cjw(qu)
        if fu:
            rkr = True
            break
        skr -= 1
    return rkr


def mkr(kkr: str):  # takes string kkr returns boolean
    global hu, qu, fu
    xkr = False
    vkr = lU
    while vkr >= 0:
        hu = OU[vkr]
        qu = kkr
        fu = Cjw(qu)
        if fu:
            xkr = True
            break
        vkr -= 1
    return xkr


def Oxw(oxw: int):  # takes integer oxw returns integer
    global Qu, xu
    if not Qu:
        Qu = True
        mQw()
    if oxw <= xu:
        return Yu[oxw]
    return AQw(oxw)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       utility functions
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def validate():
    if au[6] not in range(len(ProfessionRank)):
        return False
    if au[10] not in range(1, len(Hero) + 1):
        return False
    return True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                              API
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def load_hero_code(code: str):  # Tkr, 51129
    global Iu, nu

    if not tkr(code):
        print("Load Failed. Please recheck your code.")
        return None

    print("Load Successful.")
    result = HeroCodeFields(au[1], au[2], au[3], au[4], au[5], ProfessionRank[au[6]],
                            au[7], au[8], au[9], Hero[au[10]], au[11], au[12], au[13])
    for i in range(int((nu - 13) / 2)):
        result.abilities.append(Ability(au[14 + 2 * i], au[15 + 2 * i]))
    result.checksum = au[nu + 1]

    return result


def load_item_code(code: str):  # Jkr, 40635
    global nu

    if not mkr(code):
        print("Load Failed. Please recheck your code.")
        return None

    print("Load Successful.")
    result = ItemCodeFields(au[1], au[2], au[3], au[4], au[5])
    print(f'the number of items is: {au[4]}')
    nu = 5
    for i in range(6):
        nu += 1
        itemId = au[nu]
        nu += 1
        if itemId != 30:  # not an empty slot
            itemAmount = au[nu]
            result.items[i] = Item(itemId, itemAmount)
    
    print(f'the real number of items is: {len(result.items)}')
    print(result.items)
    for item in result.items.values():
        print(f'item is: {ItemName[item.id]}')
        print(f'amount is: {item.amount}')

    result.numberOfStashItems = au[nu]
    nu += 1
    for i in range(6):
        nu += 1
        itemId = au[nu]
        nu += 1
        if itemId != 30:  # not an empty slot
            itemAmount = au[nu]
            result.stashItems[i] = Item(itemId, itemAmount)

    result.checksum = au[nu + 1]

    return result


def save_hero_code(fields: HeroCodeFields, name: str=None):
    global hu, nu, player_name, keep_hash
    if not name or name == '':
        keep_hash = True
    else:
        player_name = name
    hu = oU[lU]
    au[1] = fields.int1
    au[2] = fields.int2
    au[3] = fields.food
    au[4] = fields.professionLvl
    au[5] = fields.hasFishingRod
    try:
        au[6] = ProfessionRank[fields.professionRank]
    except KeyError:
        return None
    au[7] = fields.revivalLocation
    au[8] = fields.imp5Stage
    au[9] = 1
    try:
        au[10] = Hero[fields.heroID]
    except KeyError:
        return None
    au[11] = fields.heroXP
    au[12] = fields.locationX
    au[13] = fields.locationY
    nu = 13
    for ability in fields.abilities:
        nu += 1
        au[nu] = ability.id
        nu += 1
        au[nu] = ability.level
    
    encoded = encode()
    keep_hash = False
    return encoded


def save_item_code(fields: ItemCodeFields, name: str=None):
    global hu, nu, player_name, keep_hash
    if not name or name == '':
        keep_hash = True
    else:
        player_name = name
    hu = OU[lU]
    au[1] = fields.gold
    au[2] = fields.shards
    au[3] = fields.pvpPoints
    au[4] = fields.unlockedCritterTiers
    au[5] = fields.numberOfItems
    nu = 5

    i = 6
    for item in fields.items.values():
        nu += 1
        au[nu] = item.id
        nu += 1
        au[nu] = item.amount
        i -= 1
    while i > 0:
        nu += 1
        au[nu] = 30
        nu += 1
        au[nu] = 0
        i -= 1

    nu += 1
    au[nu] = fields.numberOfStashItems
    i = 6
    for item in fields.stashItems.values():
        nu += 1
        au[nu] = item.id
        nu += 1
        au[nu] = item.amount
        i -= 1
    while i > 0:
        nu += 1
        au[nu] = 30
        nu += 1
        au[nu] = 0
        i -= 1
        
    encoded = encode()
    keep_hash = False
    return encoded


def encoding_version():
    return lU + 1


def save(fields: HeroCodeFields | ItemCodeFields, name: str=None):
    if type(fields) == HeroCodeFields:
        return save_hero_code(fields, name)
    elif type(fields) == ItemCodeFields:
        return save_item_code(fields, name)
    else:
        return None


def load(code: str, mode: int=1):
    in_brackets = False

    if len(code) < 1:
        print("Load Failed. The code is too short.")
        return None

    min_length = 10
    if code[0] == '"' and code[len(code) - 1] == '"' or \
        code[0] == "'" and code[len(code) - 1] == "'":
        if len(code) < min_length:
            print("Load Failed. The code is too short.")
            return None
        code = code[1: len(code) - 1]
        in_brackets = True
        min_length -= 2

    if len(code) >= min_length:
        if code[:6] == '-load ':
            code = code[6:]
        elif code[:7] == '-load2 ':
            code = code[7:]
            mode = 2
    elif in_brackets:
        print("Load Failed. The code is neither of supported types.")
        return None

    if code[0] == ' ': code = code[1:]

    if mode == 1:
        return load_hero_code(code)
    else: return load_item_code(code)


def load_file(text: str):
    # find the player_name
    pattern = 'call Preload( "Player Name: '
    start_pos = text.find(pattern) + len(pattern)
    end_pos = text.find('\n', start_pos) - 3
    if start_pos < 300 or end_pos < start_pos:  # roughly
        print("Load Failed. The save file is invalid.")
        return None
    name = text[start_pos: end_pos]

    # find the first code
    pattern = 'call Preload( "-load '
    start_pos = text.find(pattern) + len(pattern)
    end_pos = text.find('\n', start_pos) - 3
    if end_pos <= start_pos:  # yields neither end_pos nor start_pos is -1
        print("Load Failed. The save file is invalid.")
        return None
    code1 = text[start_pos:end_pos]

    # find the second code
    pattern = 'call Preload( "-load2 '
    start_pos = text.find(pattern) + len(pattern)
    end_pos = text.find('\n', start_pos) - 3
    if end_pos <= start_pos:  # yields neither end_pos nor start_pos is -1
        print("Load Failed. The save file is invalid.")
        return None
    code2 = text[start_pos:end_pos]

    return name, load_hero_code(code1), load_item_code(code2), code1, code2


def print_code(code: HeroCodeFields | ItemCodeFields, name: str = None):
    if type(code) == HeroCodeFields:
        hero = code
        print(f"Code: {save_hero_code(hero, name)}")
        print("Hero Code Fields:")
        print(f"  Int1: {hero.int1}")
        print(f"  Int2: {hero.int2}")
        print(f"  Food: {hero.food}")
        print(f"  Profession Level: {hero.professionLvl}")
        print(f"  Has Fishing Rod: {hero.hasFishingRod}")
        print(f"  Profession Rank: {hero.professionRank}")
        print(f"  Revival Location: {hero.revivalLocation}")
        print(f"  Imp5 Stage: {hero.imp5Stage}")
        print(f"  Int3: {hero.int3}")
        print(f"  Hero ID: {hero.heroID}")
        print(f"  Hero XP: {hero.heroXP}")
        print(f"  Location X: {hero.locationX}")
        print(f"  Location Y: {hero.locationY}")
        print("  Abilities:")
        for idx, ability in enumerate(hero.abilities):
            print(f"    {idx + 1}. ID: {ability.id}, Level: {ability.level}")
        print(f"  Checksum: {hero.checksum}")
    elif type(code) == ItemCodeFields:
        items = code
        print(f"Code: {save_item_code(items, name)}")
        print("Item Code Fields:")
        print(f"  Gold: {items.gold}")
        print(f"  Shards: {items.shards}")
        print(f"  PVP Points: {items.pvpPoints}")
        print(f"  Unlocked Critter Tiers: {items.unlockedCritterTiers}")
        print(f"  Number of Items: {items.numberOfItems}")
        print("  Items:")
        for item_id, item in items.items.items():
            print(f"    {item_id + 1}) ID: {item.id}, Amount: {item.amount}")
        print(f"  Number of Stash Items: {items.numberOfStashItems}")
        print("  Stash Items:")
        for item_id, item in items.stashItems.items():
            print(f"    {item_id + 1}) ID: {item.id}, Amount: {item.amount}")
        print(f"  Checksum: {items.checksum}")
    else:
        print("No code given.")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                        initialization
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

pEw()
mFr()

# don't do it, it might break the game
def encode_danger():
    # our_things = [0, 0, 0, 7, 1, 1, 1, 16, 163710, -8115, 2535, 39, 13, 40, 1, 41, 17, 42, 25, 171]
    # our_things = [0, 0, 0, 447, -661, -5546, 4566, 16, 999, -170, 44400, -39, 13, -45340, 4531, 44531, 17, 42, 25, 4677, 555]
    our_things = [0, '-']
    for i in range(len(our_things)):
        au[i + 1] = our_things[i]
    nu = len(our_things)
    hu = oU[lU]
    print('-load ' + encode())

# encode_danger()
