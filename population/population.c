#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start, end, years = 0 ;

do
{
start = get_int("Enter the starting population size: ");
}
while(start < 9);


    // TODO: Prompt for end size

    do
    {
        end = get_int("End size: ");
    }
    while (end < start);

    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
}
