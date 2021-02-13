#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


#define BLOCKFAT 512
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: most provide ./recover image\n");
        return 1;
    }

    FILE *inputF = fopen(argv[1], "r");
    if (inputF == NULL)
    {
        fprintf(stderr, "Could not open file %s.\n", argv[1]);
        return 2;
    }

    BYTE buffer[BLOCKFAT];
    int counter = 0;
    FILE *outputF = NULL;
    BYTE JpegHeader[4] = {0xff, 0xd8, 0xff, 0xe0};
    int findJPG = 0;

    while (fread(buffer, BLOCKFAT, 1, inputF) == 1)
    {

        if (buffer[0] == JpegHeader[0] &&
            buffer[1] == JpegHeader[1] &&
            buffer[2] == JpegHeader[2] &&
            (buffer[3] & 0xf0) == JpegHeader[3])
        {

            if (findJPG == 1 && outputF != NULL)
            {
                fclose(outputF);
            }
            else
            {
                findJPG = 1;
            }
            
            char fileName[8];    
            sprintf(fileName, "%03i.jpg", counter);
            outputF = fopen(fileName, "a");
            counter++;
        }
            
        if (findJPG == 1)
        {
            fwrite(&buffer, BLOCKFAT, 1, outputF);
        }
    }

    fclose(outputF);
    fclose(inputF);

    return 0;
}
