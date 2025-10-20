def get_wind_speed():
    msg = input("Please enter the wind speed:\n>")
    try:
        result = float(msg)
        return result
    except:
        print("Please enter a number.")
        return get_wind_speed()

wind_speed = get_wind_speed()

if wind_speed < 74:
    print(f"Tropical Storm ({wind_speed} MPH)")
elif wind_speed < 96:
    print(f"Category 1 ({wind_speed} MPH)")
elif wind_speed < 111:
    print(f"Category 2 ({wind_speed} MPH)")
elif wind_speed < 130:
    print(f"Category 3 ({wind_speed} MPH)")
elif wind_speed < 157:
    print(f"Category 4 ({wind_speed} MPH)")
else:
    print(f"Category 5 ({wind_speed} MPH)")
