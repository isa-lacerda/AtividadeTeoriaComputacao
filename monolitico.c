#include <stdio.h>

int main() {
    int entrada = 6;
    long long resultado = 1;
    int i = 1;

loop:
    if (i > entrada) goto fim;
    resultado *= i;
    i++;
    goto loop;

fim:
    printf("A fatorial de %d é: %lld\n", entrada, resultado);
    return 0;
}
