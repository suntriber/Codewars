/*
https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/c
*/

#include <stdio.h>

void count_char_types (const char *string, unsigned counts[4]);


int main(void){


    return 0;
}

void count_char_types (const char *string, unsigned counts[4]){

    for (int i = 0; i < 4; i++)counts[i] = 0;

    while(*string){
        if (*string >= 'A' && *string <= 'Z')counts[0]++;
        else if (*string >= 'a' && *string <= 'z')counts[1]++;
        else if (*string >= '0' && *string <= '9')counts[2]++;
        else counts[3]++;
        *string++;
    }

}