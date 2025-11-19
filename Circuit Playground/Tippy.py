while True:
    x, y, z = cp.acceleration
    for i in [1, 2, 3]:
        cp.pixels[i+(5 if x < 0 else 0)] = (2, 0, 4)
    cp.pixels.fill((0,0,0))