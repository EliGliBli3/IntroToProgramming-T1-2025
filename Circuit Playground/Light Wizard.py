buff = False
while True:
    x, y, z = cp.acceleration
    
    # Right = -9.8 x
    # Left = 9.8 x
    # Forward = -9.8 z
    # Backward = 9.8 z
    
    if cp.button_a and not buff:
        buff = True
        
        cp.pixels.fill((0,0,0))
        color = (0, 0 ,0)
        pixels = []
        
        if abs(x) >= abs(y):
            if x > 0: # Left
                color = (0, 1, 0)
                pixels = [1, 3, 5, 6]
            else: # Right
                color = (1, 0 ,0)
                pixels = [1, 2, 3, 4, 8, 9]
        else:
            if y > 0: # Backward
                color = (0, 0, 1)
                pixels = [2, 4, 8]
            else: # Forward
                color = (1, 1, 0)
                pixels = [3, 5, 6, 7]
        
        for p in pixels:
            cp.pixels[p] = color
    elif not cp.button_a and buff:
        buff = False