#include <stdio.h>

/*
https://www.codewars.com/kata/545a4c5a61aa4c6916000755
*/
int gimme (const int triplet[3]);
#define MAX(a, b, c) ((a > b && a > c) ? a: (b > c) ? b : c)
#define MIN(a, b, c) ((a < b && a < c) ? a: (b < c) ? b : c)


int main(){

    printf("%d -> %d\n", gimme((int[3]){2, 1, 3}), 0);
    printf("%d -> %d\n", gimme((int[3]){2, 3, 1}), 0);
    printf("%d -> %d\n", gimme((int[3]){1, 2, 3}), 1);
    printf("%d -> %d\n", gimme((int[3]){3, 2, 1}), 1);

    printf("%d\n", MAX(55, 10, 25));
    printf("%d\n", MIN(19, 10, 12));
    return 0;
}



int gimme (const int triplet[3]){

    int i;
    for (i = 0; i < 3; i++){
        if (triplet[i] != MAX(triplet[0], triplet[1], triplet[2]) && triplet[i] != MIN(triplet[0], triplet[1], triplet[2]))return i;
    }
}


/*
int gimme (const int triplet[3])
{
  int a = triplet[0], b = triplet[1], c = triplet[2];
  return a <= b ? (b <= c ? 1 : (c <= a ? 0 : 2)) :
                  (a <= c ? 0 : (b <= c ? 2 : 1));
}
*/


/*
int gimme (const int triplet[3])
{
  int a = triplet[0], b = triplet[1], c = triplet[2];

  return (a>b||a>c) && (a<b||a<c) ? 0 : (b>a||b>c) && (b<a||b<c) ? 1 : 2;
}
*/


/*
int between (const int a, const int b, const int c)
{
  return b<a && a<c || c<a && a<b;
}

int gimme (const int t[3])
{
  return between(t[0], t[1], t[2]) ? 0 : between(t[1], t[0], t[2]) ? 1 : 2;
}
*/
