/* https://www.codewars.com/kata/58249d08b81f70a2fc0001a4/train/c */

#include <stdio.h>

int round_to_10 (int n);


int main(){

    printf("%d -> %d\n", round_to_10(0), 0);
    printf("%d -> %d\n", round_to_10(10), 10);
    printf("%d -> %d\n", round_to_10(22), 20);
    printf("%d -> %d\n", round_to_10(25), 30);
    printf("%d -> %d\n", round_to_10(-5), -10);
    printf("%d -> %d\n", round_to_10(-22), -20);

    return 0;
}




int round_to_10 (int n){

    // edge case if n is negative, rounding should go other way ^_^
    if (n > 0){
        if ((n % 10) < 5)return n - (n % 10);
        else return (n + 10) - (n % 10);
    }
    else {
        if ( (n % 10) > -5) return n - (n % 10);
        else return (n - 10) - (n % 10);
    }
}


/*
#include <math.h>

int round_to_10 (int n)
{
  return round(n / 10.0) * 10;
}
*/


/*
int round_to_10 (int n) {
  if(n < 0)
    return (n - 5) / 10 * 10;
  return (n + 5) / 10 * 10;
}
*/


/*
int round_to_10 (int n)
{
  float x=n<0?-5:5;
  return (int)((n+x)/10)*10;
}
*/
