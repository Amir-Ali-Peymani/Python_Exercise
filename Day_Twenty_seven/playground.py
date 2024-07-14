#positional arguments
#def add(*args):
#    return sum(args)
#print(add(3,3,3))

#key word arguments
#i acts an store like dictionnary 
def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply=4)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
my_car = Car(make="fuck", model="you")
print(my_car.model)


