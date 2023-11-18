#include <stdio.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open forensic image file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        fprintf(stderr, "Could not open %s for reading.\n", argv[1]);
        return 1;
    }

    // Variables for file reading
    BYTE buffer[512];
    int count = 0;
    FILE *img = NULL;

    // Read blocks from file
    while (fread(buffer, sizeof(BYTE), 512, file) == 512)
    {
        // Check for the start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If a JPEG is already open, close it
            if (img != NULL)
            {
                fclose(img);
            }

            // Create a new JPEG file
            char filename[8];
            sprintf(filename, "%03i.jpg", count++);
            img = fopen(filename, "w");

            if (img == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", filename);
                return 1;
            }
        }

        // Write the block to the current JPEG file
        if (img != NULL)
        {
            fwrite(buffer, sizeof(BYTE), 512, img);
        }
    }

    // Close files
    fclose(file);
    if (img != NULL)
    {
        fclose(img);
    }

    return 0; 
}
