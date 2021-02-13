#include<stdio.h>
#include<stdlib.h>
#include<cs50.h>

int main(void)
{
    string name = get_string("%s", name);
    
    for(int i = 0; i < 10; i++)
    {
        printf("%s", name);
        printf("\n");
    }
}