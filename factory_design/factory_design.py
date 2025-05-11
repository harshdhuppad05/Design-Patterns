from abc import ABC, abstractmethod

# step1 -: define product interface

class Coffee(ABC):
    @abstractmethod
    def prepare():
        pass

# step2 -: implement concrete methods

class Latte(Coffee):
    def prepare():
        return "preparing Latte"
    
class Espresso(Coffee):
    def prepare():
        return "preparing Espresso"
    

# step3-: implement factory method

class CoffeeMachine:
    def make_coffee(self, coffee_type):
        if coffee_type == "Latte":
            return Latte.prepare()
        elif coffee_type == "Espresso":
            return Espresso.prepare()
        else:
            return "Unknown Coffee type"
        

if __name__ == "__main__":
    machine = CoffeeMachine()
    coffee = machine.make_coffee("Latte")
    print(coffee)

