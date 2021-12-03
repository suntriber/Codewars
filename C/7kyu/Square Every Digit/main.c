#include <stdio.h>
#include <string.h>
typedef unsigned long long ull;

#define square(x) ((x) * (x))

/*
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.

Note: The function accepts an integer and returns an integer
 */

unsigned long long square_digits (unsigned long long n);
int my_atoi(char c[]);
ull square_digits_2 (unsigned n);

int main() {
    //printf("%llu\t%d\n", square_digits(9119), 811181);
    printf("%llu\t%d\n", square_digits(3212), 9414);
    printf("%llu\t%d\n", square_digits_2(3212), 9414);
    return 0;
}


unsigned long long square_digits (unsigned long long n){
    unsigned char arr[128]; int i = 0; int j; unsigned char r;
    while (n != 0){
        r = n % 10;
        r *= r;
        if (r > 9) {
            arr[i] = r / 10;
            arr[i+1] = r % 10;
            i += 2;
        }
        else {
            arr[i] = r;
            printf("%c", r);
            i++;
        }
        n = n / 10;
    }
    arr[i] = '\0';

    unsigned long long value = 0; i = 0;


    for (j = 0; j < i; j++) {
        value = 10 * value + arr[j];
    }
    return value;

}




ull square_digits_2 (unsigned n)
{
  ull squared[40];
  int nb_digits = 0;

  do {
    squared[nb_digits++] = square((ull)(n % 10));
    n /= 10;
  } while (n != 0);

  ull result = 0;
int i;
  for (i = nb_digits - 1; i >= 0; i--) {
    ull shift = (squared[i] < 10) ? 10 : 100;
    result *= shift;
    result += squared[i];
  }
  return result;
}
