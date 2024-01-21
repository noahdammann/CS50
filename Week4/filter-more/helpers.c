#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Create loop for each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float sum = image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen;
            int average = (round)(sum / 3.0);
            image[i][j].rgbtRed = image[i][j].rgbtBlue = image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][(width - 1) - j];
            image[i][(width - 1) - j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a buffer
    RGBTRIPLE temp[height][width];

    // Loop through each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float sum_red = 0;
            float sum_blue = 0;
            float sum_green = 0;
            int counter = 0.00;

            // Loop through neighbouring pixels
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int limX = i + x;
                    int limY = j + y;

                    // Check if block within boundaries
                    if (limX < 0 || limX > (height - 1) || limY < 0 || limY > (width - 1))
                    {
                        continue;
                    }

                    // Find totals
                    sum_red += image[limX][limY].rgbtRed;
                    sum_blue += image[limX][limY].rgbtBlue;
                    sum_green += image[limX][limY].rgbtGreen;
                    counter ++;

                }

                // Create buffer
                temp[i][j].rgbtRed = round(sum_red / counter);
                temp[i][j].rgbtBlue = round(sum_blue / counter);
                temp[i][j].rgbtGreen = round(sum_green / counter);
            }
        }
    }

    // Transfer information to image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Create buffer
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    // Create 2D array
    int Gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int Gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};


    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redX, blueX, greenX, redY, blueY, greenY;
            redX = blueX = greenX = redY = blueY = greenY = 0;


            // Loop for neighbouring pixels
            for (int x = 0; x < 3; x++)
            {
                for (int y = 0; y < 3; y++)
                {
                    // Create co-ordinate values
                    int currentX = i - 1 + x;
                    int currentY = j - 1 + y;

                    // Check for values outside the boundaries
                    if (currentX < 0 || currentY < 0 || currentX > (height - 1) || currentY > (width - 1))
                    {
                        continue;
                    }

                    // Calculate Gx
                    redX += image[currentX][currentY].rgbtRed * Gx[x][y];
                    blueX += image[currentX][currentY].rgbtBlue * Gx[x][y];
                    greenX += image[currentX][currentY].rgbtGreen * Gx[x][y];

                    // Calculate Gy
                    redY += image[currentX][currentY].rgbtRed * Gy[x][y];
                    blueY += image[currentX][currentY].rgbtBlue * Gy[x][y];
                    greenY += image[currentX][currentY].rgbtGreen * Gy[x][y];


                }
            }

            // Calculate square root of sum of Gx^2 and Gy^2
            int red = round(sqrt(redX * redX + redY * redY));
            int blue = round(sqrt(blueX * blueX + blueY * blueY));
            int green = round(sqrt(greenX * greenX + greenY * greenY));

            // Check is value is > 255
            if (red > 255)
            {
                red = 255;
            }
            if (blue > 255)
            {
                blue = 255;
            }
            if (green > 255)
            {
                green = 255;
            }

            temp[i][j].rgbtRed = red;
            temp[i][j].rgbtBlue = blue;
            temp[i][j].rgbtGreen = green;
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
        }
    }
    return;
}
