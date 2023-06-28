milkshakes = {1: ['banana',1.50], 2: ['strawberry',1.75]}
count= len(milkshakes)
for i in range (0,count):
    waiter = int(input("what can i fix for you? : "))
    print(milkshakes.get(waiter))