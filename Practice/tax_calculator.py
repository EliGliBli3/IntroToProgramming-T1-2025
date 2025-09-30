MN_TAX_RATE = 0.06875

def calculate_tax(item: str, price, rate):
    print(f"Tax to be collected on {item}: {price*rate}\nTotal price: {price+(price*rate)}")

calculate_tax("Apple", 0.25, MN_TAX_RATE)