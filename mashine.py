import sys 
class Machine:
    def __init__(self, milk, water, beans, cups, money):
        self.milk = milk
        self.water = water
        self.beans = beans
        self.cups = cups
        self.money = money

    
    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        coffee = input()
        if coffee == 'back':
            Machine.action(self)
        elif int(coffee) == 1:
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                self.water = self.water - 250
                self.beans = self.beans - 16
                self.money = self.money + 4
                self.cups = self.cups - 1
                print('I have enough resources, making you a coffee!')
            elif self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough disposable cups")
        elif int(coffee) == 2:
            if self.water >= 350 and self.milk >=75 and self.beans >= 20 and self.cups >= 1:
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.beans = self.beans - 20
                self.money = self.money + 7
                self.cups = self.cups - 1
                print('I have enough resources, making you a coffee!')
            elif self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.beans < 20:
                print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough disposable cups")     
        else:
            if self.water >= 200 and self.milk >=100 and self.beans >= 12 and self.cups >= 1:
                self.water = self.water - 200
                self.milk = self.milk - 100
                self.beans = self.beans - 12
                self.money = self.money + 6
                self.cups = self.cups - 1
                print('I have enough resources, making you a coffee!')
            elif self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
            else:
                print("Sorry, not enough disposable cups")  

            
            
    def fill(self):
        print('Write how many ml of water you want to add: ')
        add_water = int(input())
        self.water = self.water + add_water
        print('Write how many ml of milk you want to add: ')
        add_milk = int(input())
        self.milk = self.milk + add_milk
        print('Write how many grams of coffee beans you want to add: ')
        add_beans = int(input())
        self.beans = self.beans + add_beans
        print('Write how many disposable cups of coffee you want to add: ')
        add_cups = int(input())
        self.cups = self.cups + add_cups
        
    def take(self):
        print('I gave you', self.money)
        self.money = 0
    
        
    def exit(self):
        sys.exit()
        
    def action(self):
        print('Write action (buy, fill, take, remaining, exit): ')
        act = input()
        if act == "buy":
            Machine.buy(self)
        elif act == "fill":
            Machine.fill(self)
        elif act == "remaining":
            Machine.summary(self)
        elif act == "exit":
            Machine.exit(self)
        else:
            Machine.take(self)
            
    def summary(self):
        print('The coffee machine has:')
        print(self.water,'ml of water')
        print(self.milk,'ml of milk')
        print(self.beans,'g of coffee beans')
        print(self.cups,'disposable cups')
        print("$%s of money"%self.money)
        
    def run_machine(self):
        while True:
            Machine.action(self)
        
        

m = Machine(milk=540, water=400 , beans=120, cups=9, money=550)
m.run_machine()
