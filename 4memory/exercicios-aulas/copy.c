#include<cs50.h>
#include<stdio.h>
#include<ctype.h>
#include<string.h>
#include<stdlib.h>

int main(void)
{
    char *s = get_string("s: ");

    char *t = malloc(strlen(s) + 1); //Reserva memória do tamanho de "s" + 1 (null caracter ) 

    strcpy(t, s); //Função para copiar valores de duas strings (ponteiros para array de caracteres)

    t[0] = toupper(t[0]); //transforma o 1º caracter em maiúscula

    printf("%s\n", s);
    printf("%s\n", t);

    free(t); // libera a memória alocada para "t"
}