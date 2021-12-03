#include <stdio.h>
/*
 * This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
 */

int simple_multiplication(int number);

int main() {
    printf("%d\t16\n", simple_multiplication(2));
    printf("%d\t9\n", simple_multiplication(1));
    printf("%d\t64\n", simple_multiplication(8));
    printf("%d\t%d\n", simple_multiplication(4), 32);
    printf("%d\t%d\n", simple_multiplication(5), 45);
    return 0;
}


int simple_multiplication(int number){
    if (number % 2 == 0){
        return number * 8;
    }
    else {
        return number * 9;
    }
}




/*
 int simple_multiplication(int a) {
    return a * (a % 2 == 0 ? 8 : 9);
}


int simple_multiplication(int number) {
  return number * (number % 2 == 0 ? 8 : 9);
}


int simple_multiplication(int num)
{
    return num * (num & 1 ? 9 : 8);
}


int simple_multiplication(int number) {
    return number % 2 == 0 ? number * 8 : number * 9;
}






 */