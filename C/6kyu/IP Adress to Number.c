/*
https://www.codewars.com/kata/541a354c39c5efa5fa001372
*/

#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#include <string.h>
#include <stdlib.h>

uint32_t IP_to_num (const char *IP);
char *num_to_IP (uint32_t num, char *IP);
char *int_2_bin (uint8_t target, char *binary);
char *reverse_string(char *s);

int main(){

    char ip[16] = "192.168.1.1";

    char bin[9];

    char *p = ip;

    uint8_t tar;

    char *token = strtok(p, ".");

    puts(token);
    char buffer[33];
    memset(buffer, NULL, 32);
    while (token != NULL){
        tar = atoi(token);
        int_2_bin(tar, bin);
        reverse_string(bin);
        puts(bin);
        strcat(buffer, bin);
        puts(buffer);
        token = strtok(NULL, ".");
    }
    puts(buffer);
    long ret;


    char *pp = buffer;
    uint32_t total = 0;

    while (*pp){
        total <<= 1;
        if (*pp++ == '1')total^=1;
    }
    printf("%u\n", total);




return 0;
}


char *reverse_string(char *s){
 int i;
 char temp;
 for (i = 0; i < 8/2; i++){
     temp = s[i];
     s[i] = s[8-i-1];
     s[8-i-1] = temp;
 }
 return s;
}


char *int_2_bin (uint8_t target, char *binary){

 int n, k, i;

 for (i = 0; i < 8; i++){
     k = target >> i;

     if (k & 1) binary[i] = '1';
     else binary[i] = '0';
 }
 binary[8] = '\0';
 return binary;
}


uint32_t IP_to_num (const char *ip){

    char IP[16] = "192.168.1.1";
    char *buffer;
    char bin[9];

    const char *p = &IP;
    uint8_t tar;

    char *token = strtok(p, ".");

    //puts(token);

    while (token != NULL){
        tar = atoi(token);
        int_2_bin(tar, bin);
        reverse_string(bin);
        //puts(bin);
        strcat(buffer, bin);
        //puts(buffer);
        token = strtok(NULL, ".");
    }
    puts(buffer);
    uint32_t ret;
    char *pp;
    strtol(buffer, &pp, 2);
}


char *num_to_IP (uint32_t num, char *IP)
{
// write to IP and return it
 *IP = '\0';
 return IP;
}

/*
11000000 10101000 00000001 00000001
11000000 10101000 00000001 00000001
 */
