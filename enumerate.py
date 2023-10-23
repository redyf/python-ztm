# Enumerate
# A função enumerate converte um objeto de coleção de dados em um objeto inumerável. Retorna um objeto que contém um contador como chave para cada valor dentro do objeto fazendo os items dentro da coleção serem mais fáceis de acessar. A chave é o index do item.
for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f"index of 50 is: {i}")
