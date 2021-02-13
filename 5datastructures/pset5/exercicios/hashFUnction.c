#include <stdio.h>
#include <stdlib.h>
#include <math.h>


#define LENGTH 45
const unsigned long long int N = pow(27, 3);
unsigned long hash = 19683;

typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}node;

node node1;

int main(int argc, char *argv[])
{
    
    
    if (argc != 2)
    {
        fprintf(stderr, "Error: 404\n");
        return 1;
    }
    
    FILE *inputF = fopen(argv[1], "r");
    if (inputF == NULL)
    {
        fprintf(stderr, "Could not open the file %s.\n", argv[1]);
        return 2;
    }

    char *word;

    printf("The length size is: %lld\n", N);
    printf("The unsigned size is: %ld\n", hash << 3);
    printf("The pointer size is: %lld\n", (hash << 6) / N);
}
