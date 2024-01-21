#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Create loop for each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float total = image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen;
            int average = (round)(total / 3.0);
            image[i][j].rgbtRed = image[i][j].rgbtBlue = image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Create loop through each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float original_r = image[i][j].rgbtRed;
            float original_g = image[i][j].rgbtGreen;
            float original_b = image[i][j].rgbtBlue;

            // Perform calculations to arrive at filtered values
            int new_r = (round)(0.393 * original_r + 0.769 * original_g + 0.189 * original_b);
            int new_g = (round)(0.349 * original_r + 0.686 * original_g + 0.168 * original_b);
            int new_b = (round)(0.272 * original_r + 0.534 * original_g + 0.131 * original_b);

            // For Red
            if (new_r > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else if (new_r <= 255)
            {
                image[i][j].rgbtRed = new_r;
            }
            // For Green
            if (new_g > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else if (new_g <= 255)
            {
                image[i][j].rgbtGreen = new_g;
            }
            // For Blue
            if (new_b > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else if (new_b <= 255)
            {
                image[i][j].rgbtBlue = new_b;
            }


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
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create buffer
    RGBTRIPLE temp[height][width];

    // Create loop for each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float total_red = 0;
            float total_blue = 0;
            float total_green = 0;
            int counter = 0.00;

            // Create co-ordinates for blocks surrounding [i][j]
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int limitX = i + x;
                    int limitY = j + y;

                    // Check for side or corner blocks
                    if (limitX < 0 || limitX > (height - 1) || limitY < 0 || limitY > (width - 1))
                    {
                        continue;
                    }

                    // Sum operation
                    total_red += image[limitX][limitY].rgbtRed;
                    total_green += image[limitX][limitY].rgbtGreen;
                    total_blue += image[limitX][limitY].rgbtBlue;

                    counter++;

                }

                // Create buffer
                temp[i][j].rgbtRed = round(total_red / counter);
                temp[i][j].rgbtGreen = round(total_green / counter);
                temp[i][j].rgbtBlue = round(total_blue / counter);
            }
        }
    }

    // Transfer buffer to image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        }
    }
}
