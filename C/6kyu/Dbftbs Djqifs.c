/*
https://www.codewars.com/kata/546937989c0b6ab3c5000183/train/c
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char *encryptor (char *str_out, const char *str_in, int key);


int main(){

    char *str = malloc(sizeof(char)*32);
    // printf("%s --> %s\n", encryptor(str, "", 13), "");
	// printf("%s --> %s\n", encryptor(str, "no cypher", 0), "no cypher");
	// printf("%s --> %s\n", encryptor(str, "Caesar Cipher", 13), "Pnrfne Pvcure");
	// printf("%s --> %s\n", encryptor(str, "Hello World!", -5), "Czggj Rjmgy!");
	// printf("%s --> %s\n", encryptor(str, "Whoopi Goldberg", 27), "Xippqj Hpmecfsh");
	printf("%s --> %s\n", encryptor(str, "lV8!c6dXf", -64), "zJ8!q6rLt");
    return 0;
}



char *encryptor (char *str_out, const char *str_in, int key)
{
	char *p_str_out = str_out;
	char c;
	if (key < 0)key%=-26;
	else key%=26;

	if (!(*str_in)){*str_out='\0';return str_out;}

	while (*str_in){
		c = *str_in++;
		if (isupper(c)){

			if (c+key > 90)      c = c+key-26;
			else if (c+key < 65) c = c+key+26;
			else                 c = c+key;
		}
		else if (islower(c)){
			if (c+key > 122)     c = c+key-26;
			else if (c+key < 97) c = c+key+26;
			else                 c = c+key;
		}
		*p_str_out++=c;
	}


	*p_str_out = '\0';
	
	return str_out;
}


/*
#include <ctype.h>

char* encryptor(char* str_out, const char* str_in, int key) {
    char* p = str_out;
    for (char c = *str_in++; c; c = *str_in++) {
        if (isalpha(c)) {
            char offset = isupper(c) ? 'A' : 'a';
            *p = (c - offset + key % 26 + 26) % 26 + offset; 
        } else {
            *p = c;
        }
        ++p;
    }
    *p = '\0';
    return str_out;
}
*/


