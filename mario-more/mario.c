#include <cs50.h>
#include <stdio.h>

int main(void)
{

int Trow, row, sp, h, hash;

do{
 Trow = get_int("input your height, from 1 to 8 :  \n");
}while(Trow<1 || Trow>8);

// print space's
 for(row =0; row < Trow; row++){

  // print space's
  for(sp =0; sp<(Trow - row-1); sp++){
  printf(" ");
 }

 // printin hash's
  for(hash=0; hash <= row; hash++){
   printf("#");
 }

    printf("  ") ;

    for(hash=0; hash <= row; hash++){
   printf("#");
 }
 printf("\n");
}

}
