"""
#### Exercício 1

Receba um número e calcule o fatorial dele.

Obs: O fatorial de um número é calculado pela seguinte fórmula "n! = n · (n-1) · (n-2) … 3 · 2 · 1". Ou seja, por exemplo:

4! = 4 * 3 * 2 * 1 = 24.

Exemplo:

Digite um número:
4

O fatorial de 4 é 24.
--------
Digite um número:
5

O fatorial de 5 é 120.

Dica: Para ajudar nesse cálculo, lembre-se das estruturas de repetição. 

Pode-se utilizar o comando "while" ou até o "for" para te ajudar nisso.

Fonte: Curso em vídeo.
"""

numero = int(input("Digite um número: ")) 
fatorial = 1 # Variável para armazenar o resultado do fatorial, iniciada com 1, pois o fatorial de 0 é 1 e o fatorial de 1 também é 1

for i in range(2, numero + 1): # Utiliza um loop for para percorrer os números de 2 até o número digitado pelo usuário (inclusive), pois o fatorial de 0 e 1 é 1, então começamos a multiplicar a partir de 2
    fatorial = fatorial * i # Multiplica cada número ao valor da variável fatorial

print(f"O fatorial de {numero} é {fatorial}.")
