#include <stdio.h>
#include <stdbool.h>

bool lovefunc(int flower1, int flower2);


int main() {
    printf("%d\n", lovefunc(1, 4));
    printf("%d\n", lovefunc(0, 1));
    printf("%d\n", lovefunc(2, 2));
    printf("%d\n", lovefunc(0, 0));
    return 0;
}

bool lovefunc(int flower1, int flower2){
    if ((flower1%2==1) & (flower2%2==0)){
        return true;
    }
    else if ((flower1%2==0) & (flower2%2==1)){
        return  true;
    }
    else {
        return false;
    }
}



/*
 * bool lovefunc(int flower1, int flower2) {
  return flower1 % 2 != flower2 % 2;
}
 *
 *
 *
 * bool lovefunc(int flower1, int flower2) {
  return (flower1 + flower2) % 2;
}
 *
 *
 * bool lovefunc(int flower1, int flower2) {
  if( (flower2 % 2) == (flower1 % 2) )
  return false;
  else{
    return true;
  }
}
 *
 *
 * bool lovefunc(int flower1, int flower2) {
  return (flower1 % 2 == 0 && flower2 % 2) || (flower1 % 2 && flower2 % 2 == 0);
}
 *
 *
 */