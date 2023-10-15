#include <cs50.h>
#include <stdio.h>

// variable decleration
int get_cents(void);
int quarters(int cents);
int dimes(int cents);
int nickels(int cents);
int pennies(int cents);

int main(void)
{

    int cents = get_cents();
    int quarters = quarters(cents);
    int dimes=  dimes(cents);
    int nickels = nickels(cents);
    int pennies = pennies(cents);
    int Final_coins = quarters + dimes + nickels + pennies ;


printf("%d\n", Final_coins);
return 0;
}

int get_cents(void)
{
    int cents ;
    do{
    // prompt the user to get the change that is owed
        cents = get_int("Change the amount that is owed: ");
    } while (cents < 0 );

    return cents ;
}

int quarters(int cents)
{
return cents/25 ;
}

int dimes(int cents)
{
    return (cents %25)/10 ;
}
int pennies(int cents)
{
    return ((cents %25)%10)%5 ; 
}