#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

/*
 * https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/c
 *
 * This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
 */

char *accum(const char *source);


int main() {

    char test1[] = "ZpglnRxqenU";
    char test2[] = "AbCd";
    char test3[] = "RqaEzty";
    char *test4 = "HbideVbxncC";

    puts(accum(test1));
    puts(accum(test2));
    puts(accum(test3));
    puts(accum(test4));

    return 0;
}


char *accum(const char *source) {

    int i, j, k;
    k = 0;
    int size = (int) strlen(source);
    int t_size = size * (size+1) / 2 + size;
    char *buf = malloc(t_size);

    for (i = 0; i < size; i++){
        for (j = -1; j < i; j++){
            if (j == -1){
                buf[k] = toupper(source[i]);
            }
            else {
                buf[k] = tolower(source[i]);
            }
            k++;
        }
        buf[k] = '-';
        k++;
    }

    buf[k-1] = '\0';

    return buf;
}


/*
#include <malloc.h>
#include <string.h>
#include <ctype.h>

char *accum(const char *source) {
  int len = strlen(source);
  char *str = (char*)malloc(len * (len + 1));
  int i = 0;

  for (int j = 0; j < len; j++, i++) {
    for (int k = 0; k < (j + 1); k++, i++) str[i] = !k ? toupper(source[j]) : tolower(source[j]);
    str[i] = '-';
  }
  str[i-1] = '\0';
  return str;
}
 */


/*
#include <malloc.h>
#include <string.h>
#include <ctype.h>

char *accum(const char *source) {
  int len = strlen(source);
  char *str = (char*)malloc(len * (len + 1) / 2 + len);
  int i = 0;

  for (int j = 0; j < len; j++, i++) {
    for (int k = 0; k < (j + 1); k++, i++) str[i] = !k ? toupper(source[j]) : tolower(source[j]);
    str[i] = '-';
  }
  str[i-1] = '\0';
  return str;
}
 */



/*
char *accum(const char *s) {
  char *r = calloc(strlen(s) * (strlen(s)+1) + 1, 1), *q = r;
  for (char *p = s; *p; p++) {
    if (p != s) *q++ = '-';
    for (int j = 0; j <= p-s; j++) *q++ = j == 0 ? toupper(*p) : tolower(*p);
  }
  return r;
}
 */