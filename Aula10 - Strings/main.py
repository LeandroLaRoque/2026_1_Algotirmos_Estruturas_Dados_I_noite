txt = "python"

# Imprime os caracteres da string do início até o 2, não pega o 3.
print(txt[:3])

# Imprime os caracteres da string do índice 1 até 2, não pega o 3.
print(txt[1:3])

# Imprime a string de trás para frente. O passo -1 indica que a string deve ser percorrida de trás para frente.
print(txt[::-1])

print("th" in txt)
print("ab" in txt)

txt_maiusculo = txt.upper()  # Transforma a string para maiúscula.

# Transforma a string para maiúscula e depois para minúscula.
print(txt_maiusculo.lower())

txt = "PyThOn"

# Transforma as letras maiúsculas em minúsculas e as letras minúsculas em maiúsculas.
print(txt.swapcase())

txt = "algoritmo e estruturas"

# Transforma a primeira letra da string em maiúscula e o restante em minúscula.
print(txt.capitalize())

# Transforma a primeira letra de cada palavra em maiúscula e o restante em minúscula.
print(txt.title())


txt = "   python   "

# Remove os espaços em branco no início e no final da string.
txt2 = "-" + txt.strip() + "-"
print(txt2)

# Remove os espaços em branco apenas no início(esquerda) da string.
txt2 = "-" + txt.lstrip() + "-"
print(txt2)

# Remove os espaços em branco apenas no final(direita) da string.
txt2 = "-" + txt.rstrip() + "-"
print(txt2)

url = "http://senacrs.com.br"
print(url.removeprefix("http://"))  # Remove o prefixo "http://" da string.

# Remove o sufixo ".com.br" e o prefixo "http://" da string.
print(url.removesuffix(".com.br").removeprefix("http://"))

txt = "python"
print(txt.find("ho"))

txt = "algoritmo"
print(txt.rfind("o"))
print(txt.find("o"))
print(txt.count("o"))
print(txt.replace("ti", "rit"))
print(txt)
print(txt.translate(str.maketrans("o", "0")))

lista = "joão;maria;josé"
print(lista.partition(";"))
print(lista.split(";"))

separador = "-"
print(separador.join(["Júlia", "Carlos", "Matilde"]))
print(txt.isalpha())
txt += "123"
print(txt)
print(txt.isalpha())
print(txt.isalnum())
print(txt.isnumeric())

txt = "Python"
print("tudo minúsculo:", txt.islower())
print("tudo maiúsculo:", txt.isupper())

txt = " "
print(txt.isspace())
