/*
https://www.codewars.com/kata/58039f8efca342e4f0000023/train/c
*/

#include <stdio.h>
#include <ctype.h>

char *change_it_up (char *str_out, const char *str_in);


int main(){ 

    // const char ass[] = "abcdefghijklmnopqrstuvxyz";
    // const char *s = &ass[0];
    char *ss;
    char *sss;

    const char *s = "zZzZABcd";
    

    printf("dbU30 -> %s\n", change_it_up(ss, (const char*)"Cat30"));
	// printf("bmjdf -> %s\n", change_it_up("Alice", s));
	// printf("tqpOhf1 -> %s\n", change_it_up("sponge1", s));
	// printf("Ifmmp xpsmE -> %s\n", change_it_up("Hello World", s));
	// printf("Epht -> %s\n", change_it_up("dogs", s));
	// printf("A -> %s\n", change_it_up(sss, s));
	// printf(" -> %s\n", change_it_up("", s));
    return 0;
}


char *change_it_up (char *str_out, const char *str_in){

    char *tmp = str_out;
    const char *tmp2 = str_in;
    

    while(*tmp2){
        if (isalpha(*tmp2))*tmp = *tmp2 + 1;
        else *tmp = *tmp2;
        if (*tmp == 91 || *tmp == 123)*tmp = 'A';
        *tmp++;
        *tmp2++;
        }
    
    
    char *ntmp = str_out;
    const char *tmp3 = str_out;



    while(*tmp3){
        if (*tmp3 == 'e' || *tmp3 == 'E')*ntmp='E';
        else if (*tmp3 == 'i' || *tmp3 == 'I')*ntmp='I';
        else if (*tmp3 == 'o' || *tmp3 == 'O')*ntmp='O';
        else if (*tmp3 == 'u' || *tmp3 == 'U')*ntmp='U';
        else if (*tmp3 >= 66 && *tmp3 <= 90)*ntmp+=32;
        *ntmp++;
        *tmp3++;
    }

    // *tmp = '\0';
	return str_out;
}