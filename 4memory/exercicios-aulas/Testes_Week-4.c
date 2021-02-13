#include<stdio.h>
#include<stdlib.h>

int main(void)
{    
    int i = 50;
    int *n = &i;

    printf("Adress: %p\n", &n);

    *n = i;

    printf("%i\n", *n);

    printf("\n");
}

//LINHA 7 e 9: "&"" representa o endereço onde a variável está armazenada representada por hexadecimais... >
// >> como "0x7ffd34bfac80", por exemplo.

//Se por acaso, ao invés do endereço, eu desejar passar valores de uma variável pra outra,... >
// >> tudo o que preciso fazer é:

//LINHA 11 e 13: O ponteiro de n recebe o valor de i. Não a cópia, mas o valor contido na memória
// No printf, a sintaxe é representada abaixo. No typeholder "%" eu mantenho o tipo de variável...
// >> Após a vírgula, eu indico o ponteiro para a variável que recebe de outra variável.