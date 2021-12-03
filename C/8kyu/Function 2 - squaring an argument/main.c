#include <stdio.h>
#include <stdint.h>

int32_t square(int32_t n);

/*
 Now you have to write a function that takes an argument and returns the square of it.
 */


int main() {
    printf("%d\t%d\n", square(1), 1);
    printf("%d\t%d\n", square(2), 4);
    printf("%d\t%d\n", square(3), 9);
    printf("%d\t%d\n", square(4), 16);
    printf("%d\t%d\n", square(5), 25);
    return 0;
}


int32_t square(int32_t n){
    return n*n;
}
