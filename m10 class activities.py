# Module 10 Class Activities

class Pakuri:
    def __init__(self, name):
        self.name = name
    def attack(self, attack_name):
        print(f'{self.name} used {attack_name}!')
    def speak(self):
        print(f'{self.name}, {self.name}!')

# pikabu = Pakuri('Pikabu')
# pikabu.speak()
# pikabu.attack('Ts Attack')

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f'Deposited ${amount}.')
        else: print('Invalid amount.')
    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have enough money :(")
        elif amount >= 0:
            self.balance -= amount
            print(f'Withdrew ${amount}.')
        else: print('Invalid amount.')
    def display(self):
        print(f'Current balance: ${self.balance}')

# account = BankAccount()
# account.display()
# account.deposit(-1)
# account.deposit(10)
# account.display()
# account.withdraw(20)
# account.withdraw(-5)
# account.withdraw(1)
# account.display()
# account.withdraw(9)
# account.display()

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if not isinstance(other, Coordinate):
            return False
        if self.x == other.x and self.y == other.y:
            return True
        else: return False
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new = Coordinate(new_x, new_y)
        return new
    def __str__(self):
        return f'({self.x}, {self.y})'

p1 = Coordinate(2, 4)
p2 = Coordinate(3, 7)
p3 = Coordinate(2, 4)
p4 = p1 + p2
print("p1 == p2?", p1 == p2)
print("p1 == p3?", p1 == p3)
print(f"{p1} + {p2} = {p4}")
print(p1)

