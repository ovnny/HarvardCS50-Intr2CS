#include <stdio.h>

int main(void)
{
    int x;
    printf("x: ");
    scanf("%i", &x); //similar to printf scan values of user. %i = what do you wanna scan?
    //&x = pointer for variable values. No pass by value but by reference (Adress)
    printf("x: %i\n", x);
}