class Resturant:
    def __init__(set, name, cuisine):
        set.name = name
        set.cuisine = cuisine

    def my_func(set):
        print("Hello " + set.name + ", your cuisine " + set.cuisine + " is ready.")

class General(Resturant):
   p1 = Resturant("John", "chicken cutlet")
   p1.my_func()