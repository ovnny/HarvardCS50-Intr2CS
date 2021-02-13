
//Redimensionando ARRAYS com "malloc"

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *list = malloc(3 * sizeof(int));    //ponteiro para memória de tamanho de 3
    if (list == NULL)                       //inteiros == 12 bites// condição que 
                                            //>> controla se o ponteiro é funcional
                                            //>> e aponta para um lugar certo.
    {
        return 1;                           // Mensagem de erro padrão
    }

    list[0] = 1;                            // instanciando a ordem dos valores com um array
    list[1] = 2;
    list[2] = 3;

    int *tmp = malloc(4 * sizeof(int));     //cria uma variável temporária para
                                            // >> ampliação do 1º array(list).
    if (tmp == NULL)
    {
        return 1;
    }

    for (int i = 0; i < 3; i++)             //itera sobre o 1º ARRAY e atribui uma nova variável
    {                                       //>>chamada (tmp).
        tmp[i] = list[i];                   //Coloca (list) dentro de (tmp).
    }

    tmp[3] = 4;                             //atribui um quarto elemento ao novo Array (resize)
                                            
    free(list);                             //libera a memória alocado na linha 9.

    list = tmp;                             //trocando os nomes das variáveis. Temporária (tmp)
                                            //de volta para (list)
    
    for (int i = 0; i < 4; i++)             //itera sobre o novo tamanho do array. (dessa vez, 4)     
    {
        printf("%i\n", list[i]);
    }

    free(list);                             //libera a memória alocada na linha 21

}

