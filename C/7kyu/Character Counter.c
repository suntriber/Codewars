/*
https://www.codewars.com/kata/56786a687e9a88d1cf00005d/train/c
*/

#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool validate_word(const char *word);
int count_characters(const char *str, char c);
#define formatBool(b) ((b) ? "true" : "false")


int main(){
    //test cases
    printf("%s --> true\n", formatBool(validate_word("")));
    printf("%s --> true\n", validate_word("ABCabc")? "true":"false");
    printf("%s --> false\n", validate_word("abc:abc")? "true":"false");

    return 0;
}


bool validate_word(const char *word){

    int size = strlen(word);
    int i;
    int count = count_characters(word, toupper(word[0]));

    for (i = 1; i < size; i++){
        if (count_characters(word, toupper(word[i])) != count) return false;
    }

    return true;
}


int count_characters(const char *str, char c){

const char *p = str;
int count = 0;

do {
    if (toupper(*p) == c)count++;
    }while(*(p++));
return count;
}
