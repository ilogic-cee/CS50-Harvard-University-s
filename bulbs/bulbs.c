#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void) {
  // Get the message from the user
  char message[1024];
  printf("Enter a message: ");
  fgets(message, sizeof(message), stdin);

  // Convert each character to its 8-bit binary representation
  for (int i = 0; i < strlen(message); i++) {
    int character = message[i];

    // Print each bit of the binary representation
    for (int j = BITS_IN_BYTE - 1; j >= 0; j--) {
      int bit = (character >> j) & 1;
      print_bulb(bit);
    }

    printf("\n");
  }

  return 0;
}

void print_bulb(int bit) {
  if (bit == 0) {
    // Dark emoji
    printf("\U000026AB");
  } else if (bit == 1) {
    // Light emoji
    printf("\U0001F7E1");
  }
}
