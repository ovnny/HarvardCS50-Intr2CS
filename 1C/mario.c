#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int pyramidH, row, space, block;

    do
        pyramidH = get_int("What's the height: ");

    while (pyramidH < 1 || pyramidH > 8);

    for (row = 1; row <= pyramidH; row++)
    {
        for (space = 1; space <= (pyramidH - row); space++)
            printf(" ");

        for (block = 0; block <= (pyramidH - space); block++)
            printf("#");
        printf("  ");

        for (block = 0; block >= (space - pyramidH); block--)
            printf("#");

        printf("\n");
    }
}
