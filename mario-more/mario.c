#include <cs50.h>
#include <stdio.h>

int main(void)
{

`int Trow, row, sp, h, hash;

do{
  Trow = get_int("input your height, from 1 to 8 :  \n");

 // print spaces
for(row =1; row <= Trow; row++){
 for(sp =1; sp<=(Trow - row); sp++){
  printf(" ");
 }

 // printin hash's
  for(hash=1; hash <= 2*row; hash++){
   printf("#");
   printf("\n");
 }
}
Trow = get_int("input your height, from 1 to 8 :  \n");

 // print spaces
for(row =1; row <= Trow; row++){
 for(sp =1; sp<=(Trow - row); sp++){
  printf(" ");
 }

 // printin hash's
  for(hash=1; hash <= 2*row; hash++){
   printf("#");
   printf("\n");
 }
}while(Trow<=1 || Trow>=8);



}


