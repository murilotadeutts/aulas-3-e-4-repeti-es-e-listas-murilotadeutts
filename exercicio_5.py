"""
#### Exercício 5 - Lista de organismos

Você recebeu uma lista que contém, para cada organismos detectado numa amostra, uma outra lista contendo a 
quantidade de leituras que esse organismo teve em cada identificador taxonômico.

Obs: Deixei a lista direto no exercício para facilitar. Mas faça o código para descobrir, não coloque a resposta direto!

Por exemplo:

[[100, 200, 300], [1, 99, 10000], [1, 1, 1]].

Eu quero que você identifique o organismo que teve a maior média de leituras entre todos os organismos da lista.

Ao identificar digite a posição em que esse organismo se encontra na lista.

No exemplo acima, você imprimiria:

"O organismo com maior média é o da posição 1 da lista."

Porque o organismo da posição 0 tem média de (100 + 200 + 300) / 3 = 200, o organismo da posição 0
tem média de (1 + 99 + 10000) / 3 = 3366,66 e o da posição 2 tem média de (1 + 1 + 1) / 3 = 1.

Logo o da posição 1 é maior.

------

Exemplo:
lista_de_organismos = [[100, 200, 300], [1, 99, 10000], [1, 1, 1]]

Resposta:
O organismo com maior média é o da posição 1 da lista.

Dica: Utilize mais de um for para resolver o exercício, um para a lista de organismos e um para cada lista. Cuidado com a identação.

O cálculo de média já foi feito em sala e pode ser usado de exemplo.
"""

# Lista
lista_de_organismos = [[50, 50, 50], [125, 99, 12], [19, 91, 42], [40, 189, 0], [1, 0, 0], [100, 100, 70], [99, 12, 12]]

# Fazer a partir daqui

maior_media = 0 # Variável para armazenar a maior média encontrada, iniciada com 0
organismo_com_maior_media = 0 # Variável para armazenar o índice do organismo com a maior média, iniciada com 0

for i in range(len(lista_de_organismos)): # Utiliza um loop for para percorrer cada organismo na lista de organismos, utilizando a função len() para obter o número de organismos e range() para criar um índice para cada organismo
    soma = 0 # Variável para armazenar a soma das leituras do organismo atual, iniciada com 0
    for leitura in lista_de_organismos[i]: # Utiliza um loop for para percorrer cada leitura do organismo atual, utilizando a variável 'leitura' para representar cada leitura individualmente
        soma = soma + leitura # Adiciona cada leitura à variável soma
    media = soma / len(lista_de_organismos[i]) # Calcula a média das leituras do organismo atual dividindo a soma pelo número de leituras, utilizando a função len() para obter o número de leituras
    if media > maior_media: # Compara a média do organismo atual com a maior média encontrada até agora
        maior_media = media # Se a média do organismo atual for maior, atualiza a variável maior_media com essa nova média
        organismo_com_maior_media = i # Atualiza o índice do organismo com a maior média

print(f"O organismo com maior média é o da posição {organismo_com_maior_media} da lista.") 
