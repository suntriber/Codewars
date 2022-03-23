/*
https://www.codewars.com/kata/5590961e6620c0825000008f/train/c
*/
#include <stdio.h>
#include <string.h>

char *swap_case(const char *string, char *swapped);


int main(){

    const char *one = "ABCabc1234";
    char two[15];

    char *ret = swap_case(one, two);
    puts(one);
    puts(two);
    puts(ret);
    return 0;
}


char *swap_case (const char *string, char *swapped){

    int size = strlen(string);
    if (strcmp(string, "") == 0){
        *swapped = '\0';
        return swapped;
    }

    for (int i = 0; i < size; i++){
        if (string[i] <= 90 && string[i] >= 65){
            swapped[i] = string[i] + 32;
        }
        else if (string[i] <= 122 && string[i] >= 97){
            swapped[i] = string[i] - 32;
        }
        else swapped[i] = string[i];
    }
    swapped[size] = '\0';
	return swapped;
}


/*
#include <ctype.h>

char *swap_case (const char *string, char *swapped)
{
  char *retval = swapped;

  for (char ch; (ch = *string); string++, swapped++)
    *swapped = isupper(ch) ? tolower(ch) : toupper(ch);

  *swapped = '\0';
  return retval;
}
*/


/*
char *swap_case(const char *string, char *swapped) {
  char *dst = swapped;
  while (*string != '\0') {
    char c = *string++, lc = c | 'A' ^ 'a';
    *dst++ = 'a' <= lc && lc <= 'z' ? c ^ 'A' ^ 'a' : c;
  }
  *dst = '\0';
  return swapped;
}
*/



/*

*/
