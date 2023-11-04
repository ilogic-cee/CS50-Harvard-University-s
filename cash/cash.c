#include <cs50.h>
#include <stdio.h>

// Function decleration
int get_cents(void);
int calculate_coins(int cents);

/*
int quarters(int cents);
int dimes(int cents);
int nickels(int cents);
int pennies(int cents);
*/

// the main function
int main(void)
{

    int cents = get_cents();
    int coins = calculate_coins(cents);

/*
    int quarters = cents/25;
    int dimes =  dimes(cents);
    int nickels = nickels(cents);
    int pennies = pennies(cents);
    int Final_coins = quarters + dimes + nickels + pennies ;
*/

printf("%d\n", coins);
return 0;
}

int get_cents(void)
{
    int cents ;
    do{
    // prompt the user to get the change that is owed
        cents = get_int("Change the amount that is owed: ");
        if (cents < 0 )
        {
            printf("Invalid input. Please enter a non negative integer value \n");
        }
    } while (cents < 0 );

    return cents ;
}

int quarters(int cents)
{
return cents/25 ;
}

int calculate_coins(int cents)
{
    int coins = 0 ;


// to calculate the number of quarters
coins += cents/ 25;
cents %= 25;

// to calculate the number of dimes
  coins += cents/10;
  cents %= 10;

// to calculate the number of nickels
  coins += cents/5 ;
  cents %= 5 ;

coins += cents ;

return coins;

}

/*
int dimes(int cents)
{
    return (cents %25)/10 ;
}
int pennies(int cents)
{
    return ((cents %25)%10)%5 ;
}

*/