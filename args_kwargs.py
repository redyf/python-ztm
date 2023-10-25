# *args and **kwargs


# def super_func(args):
#     return sum(args)
#
#
# super_func(
#     1, 2, 3, 4, 5
# )  # Não funciona pois ele espera apenas 1 posicional argument invés de 5, então devemos usar *args para tornar possível a utilização de um parâmetro na função que aceita diversos argumentos. Ao printar *args ele retorna uma tupla.
# **kwargs funciona de maneira similar porém é usado para keywords e retorna um dicionário ao printar.
# Exemplo abaixo:


def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=10, num2=15))

# Regra: parâmetros, *args, default parameters, **kwargs.
