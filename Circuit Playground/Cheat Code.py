press_buffer = [False, False]
press_order = []

# 0 = A, 1 = B, 2 = A + B
press_code = [0, 0, 1, 0, 1, 1, 1, 0, 2]

while True:
    while len(press_order) < len(press_code):
        if cp.button_a and not press_buffer[0]:
            press_buffer[0] = True
            cp.pixels[2] = (1,1,1)  # Turns on the light closest to the 'A' button to indicate it's been pressed (My buttons suck).
        elif not cp.button_a and press_buffer[0]:
            press_buffer[0] = False
            
            if not cp.button_a: press_order.append(0)
            cp.pixels[2] = (0,0,0)
            
            
        if cp.button_b and not press_buffer[1]:
            press_buffer[1] = True
            cp.pixels[7] = (1,1,1)  # Turns on the light closest to the 'A' button to indicate it's been pressed (My buttons suck).
        elif not cp.button_b and press_buffer[1]:
            press_buffer[1] = False
                
            press_order.append(1 if not cp.button_a else 2)
            cp.pixels[7] = (0,0,0)
        
      
    if press_order == press_code:
        cp.pixels.fill((0, 1, 0))
        cp.play_tone(800, 0.1)
    else:
        cp.pixels.fill((1, 0, 0))
        cp.play_tone(500, 0.1)

    time.sleep(1)
    cp.pixels.fill((0,0,0))
    press_order.clear()