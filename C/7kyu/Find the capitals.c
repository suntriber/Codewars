/*
https://www.codewars.com/kata/539ee3b6757843632d00026b/train/c
*/

#include <stdio.h>
#include <string.h>
#include <stddef.h>
#include <ctype.h>
#include <stdlib.h>
#define NELEMS(x) sizeof(x) / sizeof(x[0])

size_t *find_capitals (const char *word, size_t *nb_uppercase);


int main(){

    char *s1 = "CodEWaRs";

    size_t *var1 = 0;
    size_t *var2;

    var2 = find_capitals(s1, var1);


    for (int i = 0; i < 4; i++){
        printf("%zu\n", var2[i]);
    }

    return 0;
}


size_t *find_capitals (const char *word, size_t *nb_uppercase){

 size_t size = strlen(word);
    size_t *var = malloc(size * sizeof(size_t));
    *nb_uppercase = 0;

    for (size_t i = 0; i < size; i++){
        if (word[i] == toupper(word[i]) && isalpha(word[i])){
            var[(*nb_uppercase)++] = i;
        }
    }
    return var;
}



/*
#include <string.h>
#include <stdlib.h>

size_t *find_capitals(const char *word, size_t *nb_uppercase) {
    size_t n = strlen(word);
    size_t *array = (size_t *) calloc(n, sizeof(size_t));
    size_t j = 0;
    for(size_t i=0; i<n; i++) {
        if(word[i] > 64 && word[i] < 91) {
            array[j++] = i;
        }
    }
    *nb_uppercase = j;
    return realloc(array, j * sizeof(size_t));
}
*/


/*
#include <stddef.h>
#include <stdlib.h>
#include <ctype.h>

size_t *find_capitals (const char *word, size_t *nb_uppercase)
{
  size_t count = 0, i = 0;
  const char *p = word;
  size_t *ret = NULL;

  while (*p) {
    if (isupper(*p++))
      count++;
  }

  *nb_uppercase = count;
  ret = malloc(sizeof(size_t) * count);
  count = 0;
  p = word;

  while (*p) {
    if (isupper(*p++))
       ret[count++] = i;
    i++;
  }

  return ret;
}
*/



/*
#include <ctype.h>
#include <stddef.h>

size_t *find_capitals (const char *word, size_t *nb_uppercase)
{
    size_t len = strlen(word);
    size_t *upper = malloc(len * sizeof(size_t));
    *nb_uppercase = 0;
    for (size_t i = 0; i < len; i++) {
        if (isupper(word[i]))
            upper[(*nb_uppercase)++] = i;
    }
    return upper;
}
*/
