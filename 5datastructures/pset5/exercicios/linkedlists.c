#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int value;
    struct node *next;
}node;

int POINTNULL(int *n, struct node *next, struct node, int value);


int main(void)
{
    node *list = NULL;              //estrutura "*node" como nome "list" apontando pra lugar 
                                    //nenhum
    node *n = malloc(sizeof(node)); //estrutura "*n" 
    if (POINTNULL)

    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->value = 2;
    n->next = NULL;
    list->next = n;

    n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->value = 3;
    n->next = NULL;
    list->next->next = n;

    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->value);
    }

    while (list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }

    printf("%li\n", sizeof(list));

}
int POINTNULL(int *n, struct node value, struct node next, int)
{
    {
        if(n == NULL)
        return 1;
    {
        
    n->value = value;
    n->next = NULL;
    node list = n;

    return 1;
}
