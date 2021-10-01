#include <stdio.h>
#include <string.h>

char *accum(char *source);

/*
 * This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
 */



int main() {


    char txt[] = "12345\0abcdef";

    char test1[] = "ZpglnRxqenU";
    char test2[] = "AbCd";
    char test3[] = "RqaEzty";

    char expected1[] = "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu";
    char expected2[] = "A-Bb-Ccc-Dddd";
    char expected3[] = "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy";



    //printf("%s",accum(test2));
    accum(test2);
    return 0;
}


char *accum(char *source) {
    int i;
    int len = (int) strlen(source);
    int counter = len;

    char test[len];

    for (i = 0; i < len; i++) {
        char tmp = source[i];
        if (tmp >= 65 && tmp <= 90) {
            tmp += 32;
            test[i] = tmp;
        } else {
            test[i] = tmp;
        }
        counter+= (i+1) * 1;
        printf("%c", test[i]);
    }

    char test2[counter];


    for (i = 0; i < counter; i++){

        if (test[i+1] == test[i]){
            
        }

        test2[i] = test[i];


    }

    printf("%d", (int) sizeof(test2));

    return NULL;
}
