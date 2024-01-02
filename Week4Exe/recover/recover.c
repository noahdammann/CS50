#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check arguement is valid
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open file
    FILE *memory_card = fopen(argv[1], "r");

    // Check file is valid
    if (memory_card == NULL)
    {
        printf("File invalid\n");
        return 2;
    }

    // Store blocks of 512 bytes into array
    unsigned char buffer[512];

    // Track number of images
    int counter = 0;

    // File pointer for recovered images
    FILE *output_file = NULL;

    // Allocate memory for filename
    char *filename = malloc(8 * sizeof(char));

    // Read through file
    fread(buffer, sizeof(char), 512, memory_card);

    // Read through the blocks
    while (fread(buffer, sizeof(char), 512, memory_card))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Write the JPEG filenames
            sprintf(filename, "%03i.jpg", counter);

            // Open output_file for writing
            output_file = fopen(filename, "w");

            // Count the number of images
            counter++;
        }
        // Check if output has been used for valid input
        if (output_file != NULL)
        {
            fwrite(buffer, sizeof(char), 512, output_file);
        }
    }
    free (filename);
    fclose (output_file);
    fclose (memory_card);
}