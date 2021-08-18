print("Welcome to our fruit store!\n")

price_product_1 = 70
quantity_product_1 = int(input("How many dragonfruit do you want?"))
price_product_2 = 30
quantity_product_2 =int(input("How many kilo of kalamansi do you want?"))
price_product_3 = 60
quantity_product_3 = int(input("How many kilo of mango do you want?"))
price_product_4 = 60
quantity_product_4 = int(input("How many kilo of rambutan do you want"))

cost_prod1 = price_product_1 * quantity_product_1
cost_prod2 = price_product_2 * quantity_product_2
cost_prod3 = price_product_3 * quantity_product_3
cost_prod4 = price_product_4 * quantity_product_4

print(f"The cost of {quantity_product_1} dragonfruits: {cost_prod1}")
print(f"The cost of {quantity_product_2} kalamansi: {cost_prod2}")
print(f"The cost of {quantity_product_3} mango: {cost_prod3}")
print(f"The cost of {quantity_product_2} rambutan: {cost_prod2}")

cost = cost_prod1 + cost_prod2 + cost_prod3 + cost_prod4
print(f"Your total is: {cost}php")
pay = float(input("Please pay:"))
print("Your change is: ", pay - cost)
print("thank you for shopping!")
