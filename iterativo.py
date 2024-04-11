def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

while True:
    entrada = input("Digite um número inteiro positivo: ")
    if entrada.isdigit():
        numero = int(entrada)
        if numero >= 0:
            print("O fatorial de", numero, "é:", fatorial(numero))
            break
    else:
        print("Insira um número inteiro válido.")
