import time
from random import randint
import os

def log(funct):
    username = os.getenv("USER")
    funct_name = funct.__name__.title().replace("_", " ")
    def inner(*args, **kwargs):
        with open("machine.log", "a") as f:
            begin = time.time()
            return_value = funct(*args, **kwargs)
            end = time.time() - begin
            if end > 1:
                f.write("({})Running: {: <19} [exec_time = {:.3f} s]\n".format(username, funct_name, end))
            else:
                f.write("({})Running: {: <19} [exec_time = {:.3f} ms]\n".format(username, funct_name, end * 1000))
        return return_value
    return inner

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
        return

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
        return

if __name__ == '__main__':
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
