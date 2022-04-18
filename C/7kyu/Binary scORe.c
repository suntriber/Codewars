/*
https://www.codewars.com/kata/56cafdabc8cfcc3ad4000a2b/train/c
*/

#include <stdio.h>
#include <limits.h>

unsigned score (unsigned n);


int main(){
    printf("%u", score(49));
    return 0;
}




unsigned score (unsigned n){
  unsigned i = 0;
  unsigned d = n;
  
  while (d!=0){d>>=1;i++;}

  return n==0 ? 0 : n==1 ? 1 : n==UINT_MAX ? UINT_MAX : (1<<i)-1;
  }