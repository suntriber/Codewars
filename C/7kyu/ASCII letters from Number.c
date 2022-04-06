/*
https://www.codewars.com/kata/589ebcb9926baae92e000001/train/c
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *to_uppercase_letters (char *letters, const char *numbers);

int main(){

    char *letters;
    const char *numbers = "656667";
    to_uppercase_letters(letters, numbers);
    printf("656667 -> %s\n", letters);
    
    return 0;
}


char *to_uppercase_letters (char *letters, const char *numbers){

    size_t n = strlen(numbers);
    printf("size_t n = %zu\n", n);

    char s[n/2];
    char *buf = malloc(2);
    buf[2] = '\0';
    int tmp;
    int j = 0;
    char *p = &buf[0];

    for (size_t i = 0; i < n; i+=2){
        buf[i%2] = numbers[i];
        buf[i%2+1] = numbers[i+1];
        
        tmp = atoi(p);
        letters[j] = (char) tmp;
        j++;
        memset(buf, '\0', 2);
        buf[2] = '\0';

    }  
    letters[j] = '\0';
    return letters;
}



/*
#include <stdio.h>

char *to_uppercase_letters (char *letters, const char *numbers)
{
  char *retval = letters;
  unsigned char charcode;

  for (; sscanf(numbers, "%2hhu", &charcode) > 0; numbers += 2)
    *(letters++) = charcode;

  *letters = '\0';
  return retval;
}
*/


/*
char *to_uppercase_letters(char *letters, const char *numbers) {
    char *ptr = letters;
    while(*numbers) {
        *ptr    = (*numbers++ - 48) * 10;
        *ptr++ +=  *numbers++ - 48;
    }
    *ptr = '\0';
    return letters;
}
*/

/*
char *to_uppercase_letters (char *letters, const char *numbers)
{
  unsigned long i,j;
  for(i=0,j=0;numbers[i];i+=2,j++){
    letters[j]=10*(numbers[i]-'0')+numbers[i+1]-'0';
  }
  letters[j] = '\0';
  return letters;
}
*/
