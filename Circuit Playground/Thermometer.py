def get_color(idx):
        if idx in range(0, 3): return (0, 0, 1)
        elif idx in range(3, 7): return (1, 1, 0)
        elif idx in range(7, 10): return (1, 0, 0)

while True:
    temp = (cp.temperature*1.8)+32
    
    cp.pixels[0] = get_color(0)
    for i, v in enumerate(cp.pixels):
        if temp > (77 + i):
            cp.pixels[i] = get_color(i)
        else:
            cp.pixels[i] = (0, 0, 0)