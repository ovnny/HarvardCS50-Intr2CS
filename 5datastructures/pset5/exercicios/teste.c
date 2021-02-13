/*  1) Open a file and check if it works
    2) Read the file 'till the end and copy every word on that
    3) Take a word and pass a hash function to it
    4) Open a second file and pass only the position number of each word 
    followed by the hash code of that particular word.
    
    5) Check if the second file works fine (not NULL)
    6) Close both files and return
_____________________________________________________________________________*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define WORD_SIZE 45
unsigned int hash(const char *word);


int main(int argc, char *argv[])
{
    if (argc != 2 && argc != 3)
    {
        fprintf(stderr, ">> One or more arguments missing <<\n");
        return 1;
    }
    
    FILE *infile = fopen(argv[1], "r");
    if (infile == NULL)
    {
        fprintf(stderr, ">> Could not open the file <<\n");
        return 2;
    }

    FILE *outfile = NULL;
    char word[WORD_SIZE + 1];
    const char *wordhash;
    unsigned int hashCode;
    int counterWords = 0;

    while (fgets(word, sizeof(word), infile))
    {
        if ((outfile = fopen(argv[2], "a")) == NULL)
        {
            fprintf(stderr, "Could not open the file to apend\n");
            return 3;
        }
        else
        {
            wordhash = &word[WORD_SIZE];
            hashCode = hash(word);
            fputs(word, outfile);
            counterWords++;
            
            printf("%2i   %d\t %s", counterWords, hashCode, word);

        }
    }
    
    fclose(infile);
    fclose(outfile);
    getchar();
    
    return 0;
}

unsigned int hash(const char *word)
{
    unsigned int charValue[WORD_SIZE];
    unsigned int sum = 0;
    unsigned int hashCode = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        charValue[i] = (int)word[i];
        sum += charValue[i] * i;
        hashCode = (sum << 5) - sum;
    } 
    return hashCode % 19683;   
}