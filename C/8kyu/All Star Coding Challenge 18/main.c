#include <stdio.h>
#include <stddef.h>
/*
 * This Kata is intended as a small challenge for my students

All Star Code Challenge #18

Create a function that accepts 2 string arguments and returns an integer of the count of
 occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

 ("Hello", "o")  ==>  1
("Hello", "l")  ==>  2
("", "z")       ==>  0
 */


size_t str_count(const char *str, char letter);


int main() {
    printf("%llu\n%d", str_count("Hello", 'o'), 1);
    printf("%llu\n%d", str_count("Hello", 'l'), 2);
    printf("%llu\n%d", str_count("", 'z'), 0);
    return 0;
}


size_t str_count(const char *str, char letter){
    size_t count = 0;

    while(*str){
        if (str[count] == letter){
            printf("%c", str[count]);
            count++;
            str++;
        }
    }

    return count;
}