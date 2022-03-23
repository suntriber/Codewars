/*
* https://www.codewars.com/kata/566fc12495810954b1000030/train/c
*/

#include <stdio.h>

int nbDig(int n, int d);


int main(){

    printf("%d == %d\n", nbDig(10, 1), 4);
    printf("%d == %d\n", nbDig(5750, 0), 4700);
    printf("%d == %d\n", nbDig(11011,2), 9481);

    return 0;
}

int nbDig(int n, int d){

    int total = 0;
    int temp;

    for(int i = 0; i <= n; i++){

        temp = i*i;
        if(temp==0 && d == 0)total++;

        while (temp != 0){
            if (temp%10 == d)total++;
            temp/=10;
        }
    }
    return total;
}

