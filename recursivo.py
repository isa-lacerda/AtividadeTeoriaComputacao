def fatorial_recursivo(n):
    if n < 0:
        return "Não existe fatorial para número negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

numero = int(input("Digite um número inteiro positivo: "))
print("O fatorial de", numero, "é:", fatorial_recursivo(numero))
