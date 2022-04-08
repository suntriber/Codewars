/*
https://www.codewars.com/kata/56c1c1ed0e10121d77000a56/train/c
*/
#include <stdio.h>
int next_power_of_2 (int n);


int main(){
    printf("%d --> %d\n", next_power_of_2(4), 8);
    printf("%d --> %d\n", next_power_of_2(-16), -8);
    printf("%d --> %d\n", next_power_of_2(16), 32);
    printf("%d --> %d\n", next_power_of_2(-2), -1);
    printf("%d --> %d\n", next_power_of_2(1 << 29), 1 << 30);
    printf("%d --> %d\n", next_power_of_2(-(1 << 31)), -(1 << 30));
    return 0;
}

int next_power_of_2 (int n)
{
  return n>0 ? n<<1:n>>1;
}