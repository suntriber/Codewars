#include <stdio.h>
/*
https://www.codewars.com/kata/541c8630095125aba6000c00/train/c
*/

int digital_root(int n);


int main(){
    printf("Expected %d, got %d\n", 7, digital_root(16));
    printf("Expected %d, got %d\n", 6, digital_root(195));
    printf("Expected %d, got %d\n", 2, digital_root(992));
    printf("Expected %d, got %d\n", 9, digital_root(167346));
    printf("Expected %d, got %d\n", 0, digital_root(0));
    return 0;
}


int digital_root(int n){
    int sum = 0;

    while (n>0){
        sum += n%10;
        n/=10;
        if (n==0 && sum >= 10){
            n=sum;
            sum=0;
        }
    }
    return sum;
}


/*
int digital_root(int Z) {
  return --Z % 9 + 1;
}
*/

/*
int digital_root(int n) {
  return (n-1)%9 + 1;
}
*/

/*
int digital_root(int n) {
  return n ? ((n = n % 9) ? n : 9) : 0;
}
*/

/*

*/
