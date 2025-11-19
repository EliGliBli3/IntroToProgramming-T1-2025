while True:
    if cp.button_a:
        for i, v in enumerate(cp.pixels):
            cp.pixels[i] = (0, 0, 5)
            time.sleep(0.1)
            cp.pixels[i] = (0, 0, 0)