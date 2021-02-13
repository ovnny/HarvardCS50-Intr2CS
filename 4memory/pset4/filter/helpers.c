#include "helpers.h"
#include <math.h>
#include <string.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float turnGray;
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            turnGray = round((image[j][i].rgbtBlue + image[j][i].rgbtGreen + image[j][i].rgbtRed) / 3.00);

            image[j][i].rgbtBlue = turnGray;
            image[j][i].rgbtGreen = turnGray;
            image[j][i].rgbtRed = turnGray;
        }
    }
}
int setMaxValue(int RGB)
{
    if (RGB > 255)
    {
        RGB = 255;
    }
    return RGB;
}


// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    float sepiaBlue;
    float sepiaGreen;
    float sepiaRed;
    
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            sepiaBlue = setMaxValue(round(.272 * image[j][i].rgbtRed + .534 * image[j][i].rgbtGreen + .131 * image[j][i].rgbtBlue));
            sepiaGreen = setMaxValue(round(.349 * image[j][i].rgbtRed + .686 * image[j][i].rgbtGreen + .168 * image[j][i].rgbtBlue));
            sepiaRed = setMaxValue(round(.393 * image[j][i].rgbtRed + .769 * image[j][i].rgbtGreen + .189 * image[j][i].rgbtBlue));

            image[j][i].rgbtBlue = sepiaBlue;
            image[j][i].rgbtGreen = sepiaGreen;
            image[j][i].rgbtRed = sepiaRed;

        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
   RGBTRIPLE temp;

   for (int i = 0; i < height; i++)
   {
       for (int j = 0; j < width/2; j++)
       {
           temp = image[i][j];
           image[i][j] = image[i][width - j - 1];
           image[i][width - j - 1] = temp;
       }
   }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE aux[height][width];

    memcpy(aux, image, sizeof(RGBTRIPLE) * height * width);

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float average = 0.00;
            int red = 0; 
            int green = 0; 
            int blue = 0;

            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if ((i + k != height && j + l != width) && (i + k != -1 && j + l != -1))
                    {
                        red += aux[i + k][j + l].rgbtRed;
                        green += aux[i + k][j + l].rgbtGreen;
                        blue += aux[i + k][j + l].rgbtBlue;

                        average++;
                    }
                }
            }
            
            image[i][j].rgbtRed = round(red / average);
            image[i][j].rgbtGreen = round(green / average);
            image[i][j].rgbtBlue = round(blue / average);
        }
    }
}
