from tevehack import HeroCodeFields, ItemCodeFields, save, load, load_file
from tevehack import ItemName, Item
from browser import document, window, DOMEvent
import javascript

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                        constants & html elements
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

coordinate_x = document['coordinate-x']
coordinate_y = document['coordinate-y']
svg = document['map_svg']
hero_code_field = document['HeroCode']
hero_code_button = document['HeroCodeButton']
items_code_field = document['ItemsCode']
items_code_button = document['ItemsCodeButton']
map_side = 14250 * 2
side = map_side / 2
mark_side = 35

input_prof_rank = document['profession-rank-input']
input_prof_lvl = document['prof-lvl']
input_hero = document['hero']
input_xp = document['xp']
input_gold = document['gold']
input_shards = document['shards']
input_pvp_points = document['pvp_points']
input_player_name = document['player_name']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                        global code states
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

HeroCodeValid = True
HeroCode = HeroCodeFields(int1=2, int2=1, food=1, professionLvl=0, hasFishingRod=0, professionRank='Never caught a fish',
    revivalLocation=0, imp5Stage=0, int3=1, heroID='Novice (Female)', heroXP=0, locationX=0, locationY=0)

ItemCodeValid = True
ItemCode = ItemCodeFields(gold=0, shards=0, pvpPoints=0, unlockedCritterTiers=0, numberOfItems=0)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                        load functionality
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def handleFileSelect(evt):
    def onload(evt = 0):
        name, hero, items, hero_code, items_code = load_file(reader.result)

        if name is None or hero is None or items is None:
            return

        parse_hero_code(hero)
        parse_item_code(items)

        input_player_name.value = name
        hero_code_field.value = f'-load {hero_code}'
        items_code_field.value = f'-load2 {items_code}'
        handleDragLeave()

    evt.stopPropagation()
    evt.preventDefault()

    files = evt.dataTransfer.files
    if len(files) < 1: return
    file = files[0]
    reader = window.FileReader.new()

    # Read the file content as text
    reader.readAsText(file)
    reader.bind('load', onload)

def handleDragOver(evt):
    document['upload-field-pattern'].classList.add('text-emerald-600')
    document['upload-field-border'].classList.add('border-4')
    document['upload-field-border'].classList.add('border-emerald-400')
    evt.stopPropagation()
    evt.preventDefault()

def handleDragLeave(evt = 0):
    document['upload-field-pattern'].classList.remove('text-emerald-600')
    document['upload-field-border'].classList.remove('border-4')
    document['upload-field-border'].classList.remove('border-emerald-400')

document['upload-field'].bind('drop', handleFileSelect)
document['upload-field'].bind('dragover', handleDragOver)
document['upload-field'].bind('dragleave', handleDragLeave)


def parse_hero_code(HeroCodeFields):
    global HeroCode
    HeroCode = HeroCodeFields

    input_prof_rank.value = HeroCodeFields.professionRank
    input_prof_lvl.value = HeroCodeFields.professionLvl
    input_hero.value = HeroCodeFields.heroID
    input_xp.value = HeroCodeFields.heroXP
    print(f'x = {HeroCodeFields.locationX} y = {HeroCodeFields.locationY}')
    update_location(HeroCodeFields.locationX, HeroCodeFields.locationY)

    hero_code_field.focus()


def parse_item_code(ItemCodeFields):
    global ItemCode
    ItemCode = ItemCodeFields

    input_gold.value = ItemCodeFields.gold
    input_shards.value = ItemCodeFields.shards
    input_pvp_points.value = ItemCodeFields.pvpPoints

    print(f'numberOfItems = {ItemCodeFields.numberOfItems}')
    for i in range(6):
        if i < len(ItemCodeFields.items):
            item, amount = ItemName[ItemCodeFields.items[i].id], ItemCodeFields.items[i].amount
        else:
            item, amount = '', ''
        document[f'item-{i + 1}'].value = item
        document[f'item-{i + 1}-count'].value = amount

    for i in range(6):
        if i < len(ItemCodeFields.stashItems):
            item, amount = ItemName[ItemCodeFields.stashItems[i].id], ItemCodeFields.stashItems[i].amount
        else:
            item, amount = '', ''
        document[f'stash-item-{i + 1}'].value = item
        document[f'stash-item-{i + 1}-count'].value = amount

    items_code_field.focus()


def load_hero_code(ev = 0):
    res = load(hero_code_field.value)
    if res is None:
        hero_code_field.setCustomValidity("An invalid code.")
        return
    
    if type(res) == ItemCodeFields:
        hero_code_field.setCustomValidity("Codes are swapped over.")
        parse_item_code(res)
        items_code_field.value = hero_code_field.value
        hero_code_field.value = ''
        return

    parse_hero_code(res)


def load_item_code(ev = 0):
    res = load(items_code_field.value)
    if res is None:
        items_code_field.setCustomValidity("An invalid code.")
        return
    
    if type(res) == HeroCodeFields:
        items_code_field.setCustomValidity("Codes are swapped over.")
        parse_item_code(res)
        hero_code_field.value = items_code_field.value
        items_code_field.value = ''
        return
        
    parse_item_code(res)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                        save functionality
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_name():
    name = input_player_name.value
    if name is javascript.NULL or name == '': return ''
    if len(name) < 2 and name[0].isalpha(): return name

    end = name.rfind('#')
    return name[:end] if end!= -1 else name


def refresh_hero_code_validity(ev = 0):
    hero_code_field.setCustomValidity("")


def refresh_item_code_validity(ev = 0):
    items_code_field.setCustomValidity("")


def refresh_hero_code(ev = 0):
    if not HeroCodeValid: return
    
    code = save(HeroCode, get_name())
    if code: hero_code_field.value = f'-load {code}'
    refresh_hero_code_validity()


def refresh_item_code(ev = 0):
    if not ItemCodeValid: return
    
    code = save(ItemCode, get_name())
    if code: items_code_field.value = f'-load2 {code}'
    refresh_item_code_validity()


def draw_location(x, y):
    window.createMark(x, y, mark_side)


def update_location(x, y):
    rect = window.Rectangle(svg)
    rec_x = rect.right - rect.left
    rec_y = rect.bottom - rect.top
    x, y = float(x), float(y)
    x = int(-side if x < -side else side if x > side else x)
    y = int(-side if y < -side else side if y > side else y)

    draw_location(*convert_coordinates(x, y, rec_x, rec_y, 'game_to_webgui'))
    print(f'coordinates : {x}, {y}')
    coordinate_x.value = HeroCode.locationX = x
    coordinate_y.value = HeroCode.locationY = y

    refresh_hero_code()


def map_clicked(ev):
    rect = window.Rectangle(svg)
    x = ev.clientX - rect.left
    y = ev.clientY - rect.top
    rec_x = rect.right - rect.left
    rec_y = rect.bottom - rect.top

    x = int(0 if x < 0 else rec_x if x > rec_x else x)
    y = int(0 if y < 0 else rec_y if y > rec_y else y)
    x, y = convert_coordinates(x, y, rec_x, rec_y, 'webgui_to_game')
    update_location(x, y)


def convert_coordinates(x, y, rec_x, rec_y, mode):
    if mode == 'webgui_to_game':
        x = int( (x - rec_x / 2) / rec_x * map_side)
        y = int(-(y - rec_y / 2) / rec_y * map_side)
    elif mode == 'game_to_webgui':
        x = int( (x / map_side + 0.5) * rec_x)
        y = int(-(y / map_side - 0.5) * rec_y)
    else:
        return None
    
    return x, y


def is_valid_datalist_data(list, value) -> bool:
    if not list or list is javascript.NULL: return False
    if value is javascript.NULL: value = ''
    option = document.select("#" + list + " option[value='" + value + "']")
    if option is not None:
        return len(option) > 0

    return False


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                            refreshes
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def refresh_coordinates(ev = 0):
    x = 0 if coordinate_x.value == '' else coordinate_x.value
    y = 0 if coordinate_y.value == '' else coordinate_y.value
    update_location(x, y)


def refresh_name(ev = 0):
    refresh_hero_code()
    refresh_item_code()


def refresh_prof_lvl(ev = 0):
    global HeroCodeValid

    try:
        prof_lvl = int(input_prof_lvl.value)
    except ValueError:
        input_prof_lvl.setCustomValidity("Invalid field.")
        HeroCodeValid = False
        return

    HeroCode.professionLvl = prof_lvl
    input_prof_lvl.setCustomValidity("")

    HeroCodeValid = True
    refresh_hero_code()


def refresh_xp(ev = 0):
    global HeroCodeValid

    try:
        xp = int(input_xp.value)
    except ValueError:
        input_xp.setCustomValidity("Invalid field.")
        HeroCodeValid = False
        return

    HeroCode.heroXP = xp
    input_xp.setCustomValidity("")
    
    HeroCodeValid = True
    refresh_hero_code()


def refresh_prof_rank(ev = 0):
    global HeroCodeValid

    if not is_valid_datalist_data('profession-rank', input_prof_rank.value):
        input_prof_rank.setCustomValidity("Invalid field.")
        HeroCodeValid = False
        return
    
    HeroCode.professionRank = input_prof_rank.value
    input_prof_rank.setCustomValidity("")
    
    HeroCodeValid = True
    refresh_hero_code()


def refresh_hero(ev = 0):
    global HeroCodeValid
    
    if not is_valid_datalist_data('characters', input_hero.value):
        input_hero.setCustomValidity("Invalid field.")
        HeroCodeValid = False
        return

    HeroCode.heroID = input_hero.value
    input_hero.setCustomValidity("")
    
    HeroCodeValid = True
    refresh_hero_code()


def refresh_gold(ev = 0):
    global ItemCodeValid

    try:
        gold = int(input_gold.value)
    except ValueError:
        input_gold.setCustomValidity("Invalid field.")
        ItemCodeValid = False
        return
    
    ItemCode.gold = gold
    input_gold.setCustomValidity("")
    
    ItemCodeValid = True
    refresh_item_code()


def refresh_shards(ev = 0):
    global ItemCodeValid

    try:
        shards = int(input_shards.value)
    except ValueError:
        input_shards.setCustomValidity("Invalid field.")
        ItemCodeValid = False
        return
    
    ItemCode.shards = shards
    input_shards.setCustomValidity("")

    ItemCodeValid = True
    refresh_item_code()


def refresh_pvp_points(ev = 0):
    global ItemCodeValid

    try:
        pvp_points = int(input_pvp_points.value)
    except ValueError:
        input_pvp_points.setCustomValidity("Invalid field.")
        ItemCodeValid = False
        return

    ItemCode.pvpPoints = pvp_points
    input_pvp_points.setCustomValidity("")
    
    ItemCodeValid = True
    refresh_item_code()


def refresh_item(ev):
    global ItemCodeValid

    if isinstance(ev, DOMEvent): ev = ev.target

    if ev.type == 'number':
        try:
            if ev.value is javascript.NULL: ev.value = 0 
            int(ev.value)  # just a check for cast validity
            if not ev.checkValidity():
                ItemCodeValid = False
                return
            item_element = document[ev.id[:-6]]
            if  item_element.value is javascript.NULL or item_element.value == '':
                return
            refresh_item(item_element)
        except (TypeError, ValueError, KeyError):
            ev.setCustomValidity("Invalid field.")
            ItemCodeValid = False
        return

    pop = False
    if not is_valid_datalist_data('items', ev.value):
        if ev.value is javascript.NULL or ev.value == '':
            pop = True
        else:
            ev.setCustomValidity("Invalid field.")
            ItemCodeValid = False
            return

    # Items or StashItems
    count = document[ev.id + '-count']
    if not count.checkValidity():
        return
    try:
        int(count.value)  # just a check for cast validity
    except (TypeError, ValueError, KeyError):
        count.value = 1
    
    if pop:
        (ItemCode.items if ev.id[0] == 'i' else ItemCode.stashItems).pop(int(ev.id[-1]) - 1, None)
    else:
        item = Item(ev.value, count.value)
        (ItemCode.items if ev.id[0] == 'i' else ItemCode.stashItems)[int(ev.id[-1]) - 1] = item

    ev.setCustomValidity("")
    count.setCustomValidity("")

    ItemCodeValid = True
    refresh_item_code()
    


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                            bindings
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

svg.bind('click', map_clicked)
coordinate_x.bind('change', refresh_coordinates)
coordinate_y.bind('change', refresh_coordinates)
hero_code_button.bind('click', load_hero_code)
items_code_button.bind('click', load_item_code)
hero_code_field.bind('click', refresh_hero_code_validity)
items_code_field.bind('click', refresh_item_code_validity)
for i in range(6):
    document[f'item-{i + 1}'].bind('change', refresh_item)
    document[f'item-{i + 1}-count'].bind('change', refresh_item)
    document[f'stash-item-{i + 1}'].bind('change', refresh_item)
    document[f'stash-item-{i + 1}-count'].bind('change', refresh_item)

input_prof_rank.bind('change', refresh_prof_rank)
input_prof_lvl.bind('change', refresh_prof_lvl)
input_hero.bind('change', refresh_hero)
input_xp.bind('change', refresh_xp)
input_gold.bind('change', refresh_gold)
input_shards.bind('change', refresh_shards)
input_pvp_points.bind('change', refresh_pvp_points)
input_player_name.bind('change', refresh_name)
