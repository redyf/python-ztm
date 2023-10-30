# OOP
class PlayerCharacter:
    # Class object attribute (Objeto que não dinâmico que armazena um valor fixo, diferente dos atributos que podem mudar posteriormente).
    membership = True

    def __init__(self, name="anonymous", age=0):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f"my name is {self.name}")

    def run(self, hello):
        print(f"my name is {self.name}")


player1 = PlayerCharacter("Cindy", 24)
player2 = PlayerCharacter("Tom", 21)

print(player1.shout())
