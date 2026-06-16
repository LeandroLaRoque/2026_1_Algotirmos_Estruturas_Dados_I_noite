# texto = “João da Silva - Rua A, 132; Maria dos Santos - Rua B, 225”

# Construa um código em Python que manipule a string texto, a fim de construir um JSON conforme o exemplo a seguir

# JSON = ‘
# 	[
# 		{
# 			“nome” : “João da Silva” ,
#  			“endereço” : “Rua A” ,
# 			“numero” : “132”
# 		} ,
# 		{
# 			“nome” : “Maria dos Santos” ,
# 			“endereco“ : “Rua B” ,
# 			“numero” :  "225"
# 		}
# 	] ‘


import json

texto = "João da Silva - Rua A, 132; Maria dos Santos - Rua B, 225"

lista_pessoas = texto.split(";")
resultado = []

for item in lista_pessoas:

    # Separa nome do restante
    nome, resto = item.split(" - ")

    # Separa endereço do número
    rua, numero = resto.split(", ")

    # Dicionário
    pessoa = {
        "nome": nome.strip(),
        "endereço": rua.strip(),
        "numero": numero.strip()
    }
    resultado.append(pessoa)

print("JSON =", json.dumps(resultado, indent=4, ensure_ascii=False))
