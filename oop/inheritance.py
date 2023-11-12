class User(object):
    def __init__(self, email):
        self.email = email

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

    def run(self):
        print("ran really fast")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows) -> None:
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


class Healer(User):
    def __init__(self, name, mana) -> None:
        self.name = name
        self.mana = mana


hb1 = HybridBorg("borgie", 50, 100)
print(hb1.attack())
print(hb1.run())
# wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")
# print(dir(wizard1))  # introspection
# archer1 = Archer("Robin", 100)
