"""
#### Exercício 2 - Filtrando uma lista.

Receba uma lista de input do usuário.

Ele digitará como um texto com os números separados por vígula. Para isso, pode-se utilizar o código disponibilizado que
vai transformar esse texto em lista para você.

Depois imprima uma lista apenas com os números ímpares.

Dica: Crie outra lista e popule ela, a partir da varredura da lista original.

Exemplos:

----------------------------------

Digite a sua lista (separando os números por vírgula): 1, 2, 3, 4, 5
Resposta:
Os números ímpares são [1, 3, 5]
"""

# Código para pegar a lista
lista = [*map(int, input("Digite a sua lista (separando os números por vírgula): ").split(","))]

# Fazer a partir daqui...

impares = [] # Cria uma nova lista vazia para armazenar os números ímpares

for numero in lista: # Utiliza um loop for para percorrer cada número na lista original
    if numero % 2 != 0: # Verifica se o número é ímpar utilizando o operador de módulo (%), que retorna o resto da divisão do número por 2. Se o resultado for diferente de 0, significa que o número é ímpar
        impares.append(numero) # Se o número for ímpar, adiciona ele à lista 'impares' utilizando o método append()

print(f"Os números ímpares são {impares}.")
