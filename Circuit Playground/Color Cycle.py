colormap = {
    0: (10, 0, 0),
    1: (10, 2, 0),
    2: (10, 10, 0),
    3: (0, 10, 0),
    4: (0, 0, 10),
    5: (2, 0, 10),
    6: (10, 2, 10)
}

color = 0
press_buffer = False
while True:
    cp.pixels.fill(colormap[color])
    
    if cp.button_a and not press_buffer:
        press_buffer = True
        color = (color + 1)%len(colormap)
    elif not cp.button_a:
        press_buffer = False