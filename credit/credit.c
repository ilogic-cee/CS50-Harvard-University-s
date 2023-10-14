#include <cs50.h>
#include <stdio.h>

// calling the function is_valid_card
bool is_valid_card(long long cardN);

int length = strlen(cardN);

if (length == 15 && cardN[0] == '3' && (cardN[1] == '4' || cardN[1] == '7')) {
  // AMEX card
} else if (length == 16 && (cardN[0] == '5' && (cardN[1] == '1' || cardN[1] == '2' || cardN[1] == '3' || cardN[1] == '4' || cardN[1] == '5')) {
  // Mastercard card
} else if (length == 16 && cardN[0] == '4') {
  // VISA card
} else {
  // Invalid credit card number
}


int main(void)

 int length = string(cardN);

 {
  long long cardN;
  // prompt for users credit card Number
  cardN = get_long_long("Enter your credit card Number fully : ");

  // checking if the card is valid or not based on the is valid function
  if (is_valid_card(cardN))
  {
    printf("VALID\n");
  }
  else
  {
    printf("INVALID\n");
  }
}

bool is_valid_card(long long cardN)
{
  int total = 0;
  int count = 0;


  while (cardN > 0)
   {
    // getting the rightmost digit of the card Number
    int digit = cardN % 10;

    // if the count is odd, double the digit
    if (count % 2 == 1) {
      digit *= 2;
    }

    // add the digit to the total, even if it is double-digits
    total += digit;

    // remove the rightmost digit from the card number
    cardN /= 10;

    // increment the count
    count++;
  }

  return total % 10 == 0;
}
