/*
* https://www.codewars.com/kata/595519279be6c575b5000016/train/c
*/

#include <stdio.h>

const char *battle(const char *group_1, const char *group_2);

int main(){

    battle("AAA", "Z");

    return 0;
}


const char *battle(const char *group_1, const char *group_2){

    int sum1 = 0;
    int sum2 = 0;

    for (int i = 0; i < strlen(group_1); i++) sum1 += (int) group_1[i] - 64;
    for (int i = 0; i < strlen(group_2); i++) sum2 += (int) group_2[i] - 64;

    if (sum1 > sum2) return group_1;
    else if (sum2 > sum1) return group_2;
    else return "Tie!";
}




/*
const char *battle (const char *a, const char *b)
{
  int n = 0;
  const char *ra = a, *rb = b;

  while (*a) n += *a++ - 'A' + 1;
  while (*b) n -= *b++ - 'A' + 1;

  return  n >  0 ? ra : n < 0 ? rb : "Tie!";
}
*/


/*
const char *battle (const char *g1, const char *g2) {
  int pon1 = 0, pon2 = 0;

  for(int i = 0; g1[i] != '\0'; i++) pon1 += (g1[i] - 'A') + 1;
  for(int i = 0; g2[i] != '\0'; i++) pon2 += (g2[i] - 'A') + 1;

  return (pon1 > pon2) ? g1 : (pon1 < pon2) ? g2 : "Tie!";
}
*/
