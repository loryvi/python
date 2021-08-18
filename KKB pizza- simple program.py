print("Welcome to pizza place! KKB NGA LANG ")
name_1 = input("What is your name? ")
name_2 = input("What is your name? ")
name_3 = input("What is your name? ")

print(""" Welcome to the pizza place
   1 Margarita pizza = Php 399.00
   2 Hawaiian pizza = Php 299.00
   3 Italian pizza = Php 399.00
   4 Sisig pizza = Php 299.00
   5 Cheesy pizza = Php 399.00
""")
chosen_pizza= int(input("Enter number of chosen pizza: "))
if (chosen_pizza == 1 or chosen_pizza == 3 or chosen_pizza == 5 ):
    price_pizza, slice_pizza= 399, 48
elif(chosen_pizza ==2 or chosen_pizza == 4):
    price_pizza, slice_pizza = 299, 37

slices_ate_person1 = int(input(name_1+", How many slices did you ate? "))
slices_ate_person2 = int(input(name_2+", How many slices did you ate? "))
slices_ate_person3 = int(input(name_3+", How many slices did you ate? "))

slices = slices_ate_person1 + slices_ate_person2 + slices_ate_person3
if(slices>8):
    extra_slices = slices - 8
    price_pizza = price_pizza + (slice_pizza*extra_slices)

percent_pizzaAte_person1 = (float(slices_ate_person1) / float(slices))
percent_pizzaAte_person2 = (float(slices_ate_person2) / float(slices))
percent_pizzaAte_person3 = (float(slices_ate_person3) / float(slices))


price_paid_person1 = price_pizza*percent_pizzaAte_person1
price_paid_person2 = price_pizza*percent_pizzaAte_person2
price_paid_person3 = price_pizza*percent_pizzaAte_person3

print(f"{name_1} ate {slices_ate_person1} slices which is {percent_pizzaAte_person1 * 100:.2f}% of the pizza. {name_1} will pay: Php {price_paid_person1:.2f}")
print(f"{name_2} ate {slices_ate_person2} slices which is {percent_pizzaAte_person2 * 100:.2f}% of the pizza. {name_2} will pay: Php {price_paid_person2:.2f}")
print(f"{name_3} ate {slices_ate_person3} slices which is {percent_pizzaAte_person3 * 100:.2f}% of the pizza. {name_3} will pay: Php {price_paid_person3:.2f}")

