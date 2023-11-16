#ifndef HELPERS_H
#define HELPERS_H

#include "bmp.h"
#include <math.h>

// Function prototypes
RGBTRIPLE get_clamped_sepia_pixel(RGBTRIPLE original_pixel);

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width]);

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width]);

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width]);

#endif // HELPERS_H
