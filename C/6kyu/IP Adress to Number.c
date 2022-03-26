/*
https://www.codewars.com/kata/541a354c39c5efa5fa001372
*/

#include <stdio.h>
#include <inttypes.h>
#include <string.h>
#include <stdlib.h>

uint32_t IP_to_num (const char *IP);
char *num_to_IP (uint32_t num, char *IP);
char *int_2_bin (uint8_t target, char *binary);

int main(){

    int i = 196;
    int b = 0b0001;
    int c = 0b00000000;
    uint32_t d = 0;
    printf("size of int : %d\n", sizeof(i));
    char buffer[65];
    atoi(itoa(i, buffer, 2));

    puts(buffer);

    const char *IP = "192.168.1.1";
    while (*IP)printf("%c", *IP++);
    printf("\n");
    //char *buffer2;
    //int_2_bin(i, buffer2);
    //puts(buffer2);

    uint32_t r = 9876;

    //r = IP_to_num(IP);

    printf("%d\n", r);

    char st[] ="Where there is will, there is a way.";
    char *ch;
    ch = strtok(st, " ");
    while (ch != NULL) {
    printf("%s\n", ch);
    ch = strtok(NULL, " ,");
    }
    getch();



return 0;
}


char *int_2_bin (uint8_t target, char *binary){

    int n, k;

    for (int i = 0; i < 8; i++){
        k = target >> i;

        if (k & 1) binary[i] = '1';
        else binary[i] = '0';
    }
    binary[8] = '\0';
    return binary;
}


uint32_t IP_to_num (const char *IP)
{
    const char *p = IP;
    char buf[4]; char *bin;
    char all_four[33];
    int i;
    uint8_t num;
    i = 0;
    char c;


    while(*p){
        c = *p++;
        if (c == '.'){
            printf("%c\n", c);
            num = atoi(buf);
            int_2_bin(num, bin);
            strcat(all_four, bin);
            puts(bin);
            buf[0] = buf[1] = buf[2] = buf[3] = '\0';
            i = 0;num = 0;
            continue;
        }
        buf[i++] = c;
        puts(all_four);
    }

	return -1;
}

char *num_to_IP (uint32_t num, char *IP)
{
// write to IP and return it
	*IP = '\0';
	return IP;
}
