class User:
    def sign_in(self):
        print("Logged in")


# Herança
class Wizard(User):
    def __init__(self, name, power) -> None:
        self.name = name
        self.power = power

    # Polimorfismo
    def attack(self):
        print(f"Attacking with power of {self.power}")


class Archer(User):
    def __init__(self, name, num_arrows) -> None:
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"Attacking with arrows: arrows left - {self.num_arrows}")


class Healer(User):
    def __init__(self, name, mana) -> None:
        self.name = name
        self.mana = mana


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
wizard1.attack()
archer1.attack()
