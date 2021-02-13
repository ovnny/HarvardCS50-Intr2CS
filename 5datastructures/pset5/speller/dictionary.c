// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>

#include "dictionary.h"

#define TOTAL_BUCKETS 19683 // 27³ buckets == alphabet + "'"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = TOTAL_BUCKETS;
unsigned int wordCounter = 0; 

// Hash table
node *table[N];

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
//Check if the file is not NULL
{
    FILE *infile = fopen(dictionary, "r");
    if (infile == NULL)
        return  false;
//Set all of hashtable nodes to null      
    for (int i = 0; i < N; i++)
        table[i] = NULL;
//Initialize a linked list node to null    
    node *newNode = NULL;

    char dictWord[LENGTH + 1];
//Storing the read dictionary words on buffer
    while (fscanf(infile, "%s", dictWord) != EOF)
    {
//If word is loaded, count it
        wordCounter++;
        
        do
/*Allocating memory for every new node created
and checking if those aren't NULL*/        
        {
            newNode = malloc(sizeof(node));
            if (newNode == NULL)
                unload();
                
        }while (newNode == NULL);
//Copying words from dictionary to table        
        strncpy(newNode->word, dictWord, sizeof(dictWord));
/*Setting the hashtable index to every single word based on the 
the hash function product*/
        int hashID = hash(newNode->word);
        node *head = table[hashID];

        if(table[hashID] == NULL)
        {
//Handling with colisions creating new nodes linked by linked lists
            newNode->next = NULL;
            table[hashID] = newNode;
        }
        else
        {
            newNode->next = table[hashID];
            table[hashID] = newNode;
        }
    }
    fclose(infile);
    return true;
}

// Hashes word to a number
unsigned int hash(const char *word)
/*Hash function created by me based on Dr. Rob Edwards 
youtube channel (San Diego State University). Related link:
https://www.youtube.com/watch?v=jtMwp0FqEcg */
{
    unsigned int charValue[LENGTH + 1];
    unsigned int sum = 0;
    unsigned int hashCode = 0;

    for (int i = 0; i < strlen(word + 1); i++)
    {
        charValue[i] = (int)word[i];
        sum += charValue[i] * i;
        hashCode = (sum << 5) - sum;
    }
    return hashCode % N;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return wordCounter;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int c = strlen(word);
    char spelledWord[LENGTH + 1];
//Setting all the text characters to lower case to compare words
    for (int i = 0; i < c; i++)
    {
        spelledWord[i] = tolower(word[i]);
    }
//Setting the last character as null terminator
    spelledWord[c] = '\0';
//Generating hash IDs on the words of text to compare with our hash table data 
    int bucketLocation = hash(spelledWord);
//creating a cursor to move into our hashtable
    node *cursor = table[bucketLocation];

    while (cursor != NULL)
    {
//Comparing the words
        if (strcasecmp(cursor->word, spelledWord) == 0)
            return true;
        
//Moving to next node if the words is not compatible
        else
            cursor = cursor->next;
    }
    return false;
}



// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
//Iterating over all buckets in hashtable
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
//Pointing cursor to each hashtable head
            node *cursor = table[i];
            while (cursor != NULL)
            {
//Creating a temporary node to handle with freeing memory
                node *tmp = cursor;
                cursor = cursor->next;
//Actually freeing the nodes
                free(tmp);
            }
        }
    }
    return true;
}