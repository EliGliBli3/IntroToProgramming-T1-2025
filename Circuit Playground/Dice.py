press_buffer = False
while True:
    if cp.button_a and not press_buffer:
        press_buffer = True
        
        r = random.randrange(1, 11)
        cp.pixels.fill((0, 0, 0))
        for i in range(r):
            cp.pixels[i] = (0, 0, 1)
    elif not cp.button_a: press_buffer = False
    
    if cp.button_b:
        cp.pixels.fill((0, 0, 0))