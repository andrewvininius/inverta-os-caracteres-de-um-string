string = input("Digite a string que deseja inverter: ")

# Transforma a string em uma lista de caracteres
lista_chars = list(string)

# Define a posição inicial e final da lista
inicio = 0
fim = len(lista_chars) - 1

# Inverte a ordem dos caracteres trocando de posição os caracteres do início e do fim da lista
while inicio < fim:
    lista_chars[inicio], lista_chars[fim] = lista_chars[fim], lista_chars[inicio]
    inicio += 1
    fim -= 1

# Transforma a lista de volta em uma string
string_invertida = ''.join(lista_chars)

print("A string invertida é:", string_invertida)
