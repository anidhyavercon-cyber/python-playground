#shopping cart

foods = []
prices = []
total = 0

while True:
    food = input ("Enter the food item you want to buy (q to quit) : ")
    if food == "q" or food == "Q":
        break
    else:
        price = float(input(f"Enter the price of the {food} : $"))
        foods.append(food)                                     #this will take the input of food in foods
        prices.append(price)                                   #this will take the input of price of that food in prices
    
print ("---- YOUR CART ----")
for food in foods:
    print (food)
for price in prices:
    total = total + price 
    
print (f"Your total is {total}")