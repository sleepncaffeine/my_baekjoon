n = int(input())
toppings = list(input().split())
cheesetopping = {}
for topping in toppings:
    if topping.endswith("Cheese"):
        if topping in cheesetopping:
            cheesetopping[topping] += 1
        else:
            cheesetopping[topping] = 1

if len(cheesetopping) >= 4:
    print("yummy")
else:
    print("sad")
