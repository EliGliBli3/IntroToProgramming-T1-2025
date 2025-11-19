while True:
        for i, v in enumerate(cp.pixels):
            if i <= 4:
                cp.pixels[i] = (0, (cp.switch)*5, 0)
            else:
                cp.pixels[i] = (0, (not cp.switch)*5, 0)