while True:
    light = cp.light
    
    for i, v in enumerate(cp.pixels):
        if i in range((30-light)//3):
            cp.pixels[i] = (0, 0, 1)
        else:
            cp.pixels[i] = (0, 0, 0)