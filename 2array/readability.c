#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
// Get input from user
    string textInput = get_string("Text: ");
    int countLett = 0, countWord = 1, countSent = 0;
    

//Objects counting cases (letters, words and sentences)
    for (int i = 0, n = strlen(textInput); n > i; i++)
    {
        if (isalpha(textInput[i]))
        {
            countLett++;
        }
        if ((isspace(textInput[i])) || (isblank(textInput[i]))) 
        {
            countWord++;
        }
        if (textInput[i] == '.' || textInput[i] == '!' || textInput[i] == '?')
        {
            countSent++;
        }
    }

//Coleman-Liau test aplication
    float L = (float)countLett / (float)countWord * 100, S = (float)countSent / (float)countWord * 100;
    float grade = 0.0588 * L - 0.296 * S - 15.8;
    
//Conditional of grade's level
    if (round(grade) >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (round(grade) < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(grade));
    }

}