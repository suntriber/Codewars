/*
https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/c
*/

#include <stdio.h>
#include <string.h>

char *rot13 (char *str_out, const char *str_in);

int main(){

    const char *s = "EBG13 rknzcyr.";

    char *ss = malloc(sizeof(char)*strlen(s));

    rot13(ss, s);

    while(*ss)printf("%c", *ss++);

    return 0;
}


char *rot13 (char *str_out, const char *str_in){

    char *start = str_out;
    char c;

    while(*str_in){
        c = *str_in++;
        if (c >= 'A' && c <= 'Z') c = 'A' + (c - 'A' + 13) % 26;
        else if (c >= 'a' && c <= 'z') c = 'a' + (c - 'a' + 13) % 26;
        *str_out++ = c;
    }

  *str_out = '\0';
  return start;
}