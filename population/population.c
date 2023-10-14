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
    
int years = 0;

    while (start < end)
    {

        int born = start/3;
        int passed = start/4 ;
        start = start +born -passed ;

    }


    // TODO: Print number of years
}
