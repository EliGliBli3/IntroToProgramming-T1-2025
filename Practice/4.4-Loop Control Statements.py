import random

for i in range(20):
    if i == 15: break
    print(i)
    
print("-----\n")

for i in range(30):
    if i%2 == 0: continue
    print(i)
    
print("-----\n")
    
for i in range(10):
    pass    # In the future, will count all even numbers from 1 to 10.

for i in range(10)[::-1]:
    if i+1 == 5: continue
    print(i+1)
    
print("-----\n")

n_list = [random.randint(-2, 20) for i in range (25)]
n_poslist = []
for i in n_list:
    if i < 0: break
    n_poslist.append(i)
print(f"{sum(n_poslist)} ({(" + ".join([str(n) for n in n_poslist]))})")