#include <cs50.h>
#include <stdio.h>

int main(void)
{

int Trow, row, sp, h, hash;

do{
  Trow = get_int("input your height, from 1 to 8 :  \n");
}while(Trow<1 || Trow>8);

/* print spaces
 for(row =1; row <= Trow; row++){
 for(sp =0; sp<=(Trow - row); sp++){
  printf(" ");
 } */

 // printin hash's
  for(hash=1; hash <= Trow); hash++){
   printf("#");
   printf("\n");
 }
}
}


