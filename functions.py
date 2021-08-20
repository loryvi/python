def per_1(name):
    print(name + ": Hello, how can i help you?")

def person2_1(food,drink,dessert,name):
    name = input("What is your name? ")
    food= input("What do you want to eat?" )
    drink=input("What do you want to drink? ")
    dessert = input("Any desserts you want?")

    print(name+": I would like "+food+ " and " + drink +". and some "+dessert)

def per1_2(name):
    print(name+": Thank you")

per_1("cashier")
person2_1("food","drink","dessert","name")
per1_2("cashier")
