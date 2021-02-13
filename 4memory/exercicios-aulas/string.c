#include<cs50.h>
#include<stdio.h>
#include<stdlib.h>

int main(void)
{
    char *s = "EMMA";
    printf("%s\n", s);

    printf("%c\n", *s);
    printf("%c\n", *(s + 1));
    printf("%c\n", *(s + 2));
    printf("%c\n", *(s + 3));
    printf("%i\n", s[4]);
}

//strings não existem. Na verdade, são ponteiros para o início de um..
//...array de caracteres.

// strings = char *s = "VINICIUS";

//Se defini que uma variável local é um ponteiro no topo, não preciso
//defini-la de novo nos comandos. Por outro lado, se uso como uma função
//como nas linhas de 10 à 12, preciso expecificá-la pra achar o endereço ou
//mesmo o valor resultante da expressão ou função.

//Essa técnica acima chama-se syntatic sugar!
