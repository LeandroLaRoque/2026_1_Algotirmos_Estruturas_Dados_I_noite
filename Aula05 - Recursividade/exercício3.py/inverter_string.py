# 3) Implemente uma função recursiva para inverter uma string

def inverter_string(s):
    if len(s) == 0:
        return
    print(s[-1], end="")
    inverter_string(s[:-1])


texto = input("Digite uma string: ")
inverter_string(texto)
print()
