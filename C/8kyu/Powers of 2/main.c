#include <stdio.h>
/*
 * Complete the function that takes a non-negative integer n as input, and returns a list
 * of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).
 *
 * Examples
 * n = 0  ==> [1]        # [2^0]
 * n = 1  ==> [1, 2]     # [2^0, 2^1]
 * n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
 *
 */
#include <inttypes.h>
#include <math.h>
void powers_of_two (size_t n, uint64_t powers[n + 1]);

int main() {

    size_t n = 4;
    uint64_t powers[5] = {1, 2, 4, 8, 16};

    powers_of_two(n, powers);

    for(int i = 0; i < n+1; i++){
        printf("%d\n", powers[i]);
    }
    return 0;
}

void powers_of_two (size_t n, uint64_t powers[n + 1]){
    for (int i = 0; i < n; i++){
        powers[i] = pow(2, i);
    }
}


