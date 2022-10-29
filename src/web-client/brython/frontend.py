from browser import document, window, html

coordinate_x = document['coordinate-x']
coordinate_y = document['coordinate-y']
svg = document["map_svg"]

def update_location(x, y):
    x, y = int(x), int(y)
    coordinate_x.value = x
    coordinate_y.value = y
    window.createMark(x, y, 35)

def map_clicked(ev):
    # get the bounding rectangle of the element clicked
    rect = window.Rectangle(ev)

    # Mouse position
    x = ev.clientX - rect.left
    y = ev.clientY - rect.top

    print(f"coordinates : {x}, {y}")
    update_location(x, y)

def coordinate_changed():
    window.createMark(coordinate_x.value, coordinate_y.value, 35)

svg.bind("click", map_clicked)
coordinate_x.bind('change', coordinate_changed)
coordinate_y.bind('change', coordinate_changed)
