switch_cooldown = 0.05
last_switch = 0

while True:
    x, y, z = cp.acceleration
    mag = (((x**2)+(y**2)+(z**2))**(1/2))
    
    if mag > 20:
        if time.time() - last_switch > switch_cooldown:
            last_switch = time.time()
            cp.pixels.fill((1,0,0))
            for i, v in enumerate(cp.pixels):
                cp.pixels[i] = (random.randint(0, 5), random.randint(0, 5), random.randint(0, 5))