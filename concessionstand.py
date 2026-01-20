menu = {"pizza" : 4,
        "Burger": 2,
        "fries": 1,
        "popcorn": 1.2,
        "coke":1.8,
        "chips": 1.35,
        "dips":1.1}

cart = []
total = 0

print("------------MENU------------")
for key, values in menu.items():
    print(f"{key:10}: ${values:.2f}")
print("----------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
print("-------- YOUR ORDER --------")
for food in cart:
    total += menu.get(food)
    print (food, end= " ")
    
print ()
print(f"Total is : ${total:.2f}")
        