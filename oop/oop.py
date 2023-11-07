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

    # Não precisamos instanciar uma classe para poder usar o class method. Raramente usado mas é bom saber.
    @classmethod
    def adding_things(cls, num1, num2):
        return cls("Teddy", num1 + num2)


player1 = PlayerCharacter("Cindy", 24)
player2 = PlayerCharacter("Tom", 21)
player3 = PlayerCharacter.adding_things(2, 3)
print(player3.age)
