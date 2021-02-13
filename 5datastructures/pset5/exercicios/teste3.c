#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define WORD_SIZE 45

unsigned int hash(const char *word);

int main()
{
    while(1)
    {
        char nome[WORD_SIZE + 1];
       

        printf("hashing: ");
        scanf("%s", nome);
        printf("%d\n", hash(nome));
    }
    getchar();
    return 0; 
}


unsigned int hash(const char *word)
{
    word[WORD_SIZE + 1];
    unsigned int charValue[WORD_SIZE];
    unsigned int sum = 0;

    for (int i = 0; i < strlen(word); i++)
    {
        charValue[i] = (int)word[i];
        sum += charValue[i] * i;
    }
    return (sum << 5) - sum;
    
}
