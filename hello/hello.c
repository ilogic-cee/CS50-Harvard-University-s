#include <stdio.h>
#include <cs50.h>

int main(){

    string name = get_string("what is your name:  ");
    printf("hello Mr/Ms %s \n ", name );
}