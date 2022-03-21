#include <stdio.h>

/* Function prototype */
int evaporator(double content, double evap_per_day, double threshold);


int main() {
    printf("%d\n", evaporator(10,10,10));
    printf("%d\n", evaporator(10,10,5));
    printf("%d\n", evaporator(10,10,5));
    return 0;
}


int evaporator(double content, double evap_per_day, double threshold) {
    // content = ml
    // evap_per_day = percent
    // percent
    content = 1.0;
    evap_per_day *= 0.01;
    threshold *= 0.01;
    int i = 0;
    while (content > threshold){
        content = content * (1.0-evap_per_day);
        i++;
        printf("content %f after %d iterations\n", content, i);
    }
    return i;
}