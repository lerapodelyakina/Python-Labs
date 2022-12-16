class Rocket():
    def __init__(self, weight, fuel, engine):      
        self.weight = weight
        self.fuel = fuel
        self.engine = engine
    def spend_fuel(self, count):              
        self.fuel -= count           
        self.weight -= count             
        if self.fuel <= 0:
            self.fuel = 0
            self.engine = False
            return False
        else:
            self.engine = True
            return True
    def get_fuel_level(self):                                       
        return f'Количество топлива: {self.fuel}'
    def get_total_weight(self):                                     
        return f'Общая масса: {self.weight}'
    def get_is_engine_running(self):                                
        return f'Состояние двигателя: {self.engine}'

def main():
    my_rocket = Rocket(1000, 250, True)
    while my_rocket.fuel > 0:
        my_rocket.spend_fuel(50)
        print(my_rocket.get_fuel_level(), end='; ')
        print(my_rocket.get_total_weight(), end='; ')
        print(my_rocket.get_is_engine_running())
main()