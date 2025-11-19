count = 0
press_buffer = [False, False]
while True:
    if cp.button_a and not press_buffer[0]:
        press_buffer[0] = True
        count+=1
    elif not cp.button_a:
        press_buffer[0] = False
        
    if cp.button_b and not press_buffer[1]:
        press_buffer[1] = True
        count-=1
    elif not cp.button_b:
        press_buffer[1] = False
        
    count = min(max(count, 0), 10)
        
    for i, v in enumerate(cp.pixels):
        cp.pixels[i] = (0, 0, 1) if i in range(count) else (0, 0, 0)