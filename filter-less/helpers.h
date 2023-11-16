#ifndef HELPERS_H
#define HELPERS_H

#include "bmp.h"
#include <math.h>

// Function prototypes
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width]);

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width]);

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width]);

// Detect edges in image
void edges(int height, int width, RGBTRIPLE image[height][width]);


#endif // HELPERS_H
