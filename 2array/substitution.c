#include<stdio.h>
#include<cs50.h>
#include<ctype.h>
#include<math.h>
#include<string.h>

int main(int argc, string argv[])
{
//conditions of argument inputs - 2 inputs
//2th argument containing "26" non-repeated characters - alphabetical only
    string key = argv[1];
    if (argc != 2)
    {
        printf("ERROR #1 - The second command is missing\n");
        return 1;
    }
    else if (strlen(key) != 26)
    {
        printf("ERROR #2 - Key must contain 26 characters.\n");
        return 1;
    }
//condition denies repeated characters and numbers in the same key but allows mixing off upper and lowercase
    else
    {
        for (int i = 0; i < strlen(key); i++)
        {
            for (int j = i + 1; key[j] != '\0'; j++)

                if ((!isalpha(key[i])) || (!isalpha(key[j])) || (tolower(key[j]) - 32) == toupper(key[i]))
                {
                    printf("ERROR #3 - This argument only supports non-repeated alphabet characters\n");
                    return 1;
                }
        }
//as long all parameters succeed, gets a text input or plaintext from user
        string plain = get_string("Plaintext: ");
        int txtleng = strlen(plain);

//counting plaintext size
        for (int i = 0; i < txtleng; i++)

//assigning the characters positions values of user text to the key character positions values
        {
            if (isupper(plain[i]))
            {
                plain[i] = toupper(key[plain[i] - 65]);
            }
            else if (islower(plain[i]))
            {
                plain[i] = tolower(key[plain[i] - 97]);
            }
        }
        printf("ciphertext: %s\n", plain);
        return 0;
    }
}