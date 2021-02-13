
//Redimensionando ARRAYS com "realloc"

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *list = malloc(3 * sizeof(int));    //cria um espaço para um ARRAY de 3 inteiros
    if (list == NULL)
    
    
    {
        return 1;
    }

    list[0] = 1;                            //instancia o array
    list[1] = 2;
    list[2] = 3;

    int *tmp = realloc(list, 4 * sizeof(int));//usa a função "realloc" para realocar memória
                                            //da variável "list".
    if (tmp == NULL)                        //"realloc" já itera sobre o primeiro array e atribui
    {                                       //a ele um novo tamanho (no caso, 4)
        return 1;
    }
    
    list = tmp;                             //depois é só passar o valor da "tmp" para "list"

    list[3] = 4;                            //e setar o valor do 4º elemento

    for (int i = 0; i < 4; i++)             //itera só uma vez pelo tamanho do novo array
    {
        printf("%i\n", list[i]);
    }

    free(list);                             //libera espaço somente uma vez.
}
                                            //A FUNÇÃO ECONOMIZOU 9 LINHAS DE CÓDIGO!