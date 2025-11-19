def get_touch_input(length):
    result = []
    buffer = False
    
    while len(result) < length:
        is_touching = cp.touch_A1 or cp.touch_A2 or cp.touch_A3 or cp.touch_A4 or cp.touch_A5 or cp.touch_A6 or cp.touch_A7
        touch_id = -1
        
        if is_touching and not buffer:
            buffer = True
            touch_id = 0 if cp.touch_A1 else 1 if cp.touch_A2 else 2 if cp.touch_A3 else 3 if cp.touch_A4 else 4 if cp.touch_A5 else 5 if cp.touch_A6 else 6 if cp.touch_A7 else -1     # I dont care to rewrite this, it works.
            
            cp.play_tone(200+(touch_id*20), 0.15)
            result.append(touch_id)
        elif not is_touching and buffer:
            buffer = False
            touch_id = -1
    
    return result

while True:

    started = False
    while not started:
        cp.pixels[6] = (1, 1, 1)
        if cp.touch_A1:
            started = True
            cp.pixels[6] = (0, 0, 0)
            

    order = []
    while started:
        
        # A1 - A7
        touch_ids = [6, 8, 9, 0, 1, 3, 4]
        order.append(touch_ids[random.randint(0, 6)])
        
        #for i in order:
        time.sleep(1)
        for i in order:
            cp.pixels[i] = (0, 1, 0)
            cp.play_tone(200+((touch_ids.index(i))*20), 0.5)
            time.sleep(0.25)
            cp.pixels[i] = (0, 0, 0)
            time.sleep(0.1)
        press_order = [touch_ids[x] for x in get_touch_input(len(order))]
        
        if press_order == order:
            cp.pixels.fill((0, 1, 0))
            time.sleep(0.5)
            cp.pixels.fill((0,0,0))
        else:
            cp.pixels.fill((1, 0, 0))
            time.sleep(0.5)
            cp.pixels.fill((0,0,0))
            started = False