/*
https://www.codewars.com/kata/56c1c1ed0e10121d77000a56/train/c
*/
#include <stdio.h>
#include <inttypes.h>
int next_power_of_2 (int n);


int main(){
    /*
    printf("%d --> %d\n", next_power_of_2(4), 8);
    printf("%d --> %d\n", next_power_of_2(-16), -8);
    printf("%d --> %d\n", next_power_of_2(16), 32);
    printf("%d --> %d\n", next_power_of_2(-2), -1);
    printf("%d --> %d\n", next_power_of_2(1 << 29), 1 << 30);
    printf("%d --> %d\n", next_power_of_2(-(1 << 31)), -(1 << 30));

    printf("----------------------------------------------\n");
    */
    printf("%d --> %d\n", next_power_of_2(1009231899), 1073741824);
    // printf("%d\n", (uint64_t)1009231899);
    return 0;
}

int next_power_of_2 (int n)
{
    printf("N INCOMING IS EQUAL TO : %d\n", n);
    n = (uint64_t)n;

    uint64_t power = 1;
    int cnt = 0;

    if (n < 0){
    power = -1;
    while (power > n)power*=2;
    }
    else if (n > 0){
    while (n > power){
        power*=2;
        cnt+=1;
        printf("%d --> cnt: %d\n", power, cnt);
        }
    }
    return n>0 ? power<<1:power>>1;
}
