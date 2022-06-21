#include <cs50.h>
#include <stdio.h>

int main(void)
{

int  row, sp, h, hash;

do{
 h = get_int("input your height, from 1 to 8 :  \n");
}while(h<1 || h>8);

// print space's
 for(row =1; row < h; row++){

  // print space's
  for(sp =0; sp<(h - row-1); sp++){
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
