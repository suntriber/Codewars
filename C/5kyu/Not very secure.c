/*
https://www.codewars.com/kata/526dbd6c8c0eb53254000110/train/c
*/

#include <stdio.h>
#include <stdbool.h>

bool alphanumeric(const char* strin);

int main(){
    
    const char *s = "PassW0rd";
    printf("String [%s] return [%d] from function", s, alphanumeric(s));
    return 0;
}


bool alphanumeric(const char* s) {

    int i = 0;
    char c;

    while (*s){
        c = *s++;
        i++;
        if ((c >= 'a' && c <= 'z') || 
            (c >= 'A' && c <= 'Z') || 
            (c >= '0' && c <= '9')) continue;
        else if (c == '_' || c == ' ') return false;
        else return false;
    }
    
    return i != 0 ? true : false;

}


/*
bool alphanumeric(const char* strin) {
  if (*strin == '\0') return false;
  while (*strin) if (!isalnum(*strin++)) return false;
  return true;
}
*/

/*
bool alphanumeric(const char *s) {
  do if (!isalnum(*s)) return 0; while (*++s);
  return 1;
}
*/