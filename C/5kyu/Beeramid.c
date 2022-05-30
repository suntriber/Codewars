/*
https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/c
*/

#include <stdio.h>

int beeramid(double bonus, double price);


int main(){

    printf("%d <-- Should be 12\n", beeramid(1500, 2));
    printf("%d <-- Should be 2\n", beeramid(10, 2));

    return 0;
}


int beeramid(double bonus, double price){

    int d = 0;
    int i = 0;
    int beer_cans = bonus / price;

    while (1){
        d += i*i;
        i++;

        if (d > beer_cans){
            i--;
            break;
        }
        else if (d == beer_cans)break;
    }
    
    return i-1;
}