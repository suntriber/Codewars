/*
https://www.codewars.com/kata/58039f8efca342e4f0000023/train/c
*/

#include <stdio.h>
#include <ctype.h>
#include <string.h>

char *change_it_up (char *str_out, const char *str_in);


int main(){ 


    char *ss = malloc(sizeof(char)*100);

    printf("dbU30 -> %s\n", change_it_up(ss, (const char*)"Cat30"));
	printf("bmjdf -> %s\n", change_it_up(ss, (const char*)"Alice"));
	printf("tqpOhf1 -> %s\n", change_it_up(ss, (const char*)"sponge1"));
	printf("Ifmmp xpsmE -> %s\n", change_it_up(ss, (const char*)"Hello World"));
	printf("Epht -> %s\n", change_it_up(ss, (const char*)"dogs"));
	printf("A -> %s\n", change_it_up(ss, (const char*)"z"));
	printf(" -> %s\n", change_it_up(ss, (const char*)""));
    return 0;
}


char *change_it_up (char *str_out, const char *str_in)
{
  
    int len = strlen(str_in);
  
    if(!(*str_in)){
      *str_out='\0';
      return str_out;
    }
  
    char *tmp = str_out;
    const char *tmp2 = str_in;
    

    for (int i = 0; i < len; i++){
        if (isalpha(*tmp2))*tmp = *tmp2 + 1;
        else *tmp = *tmp2;
        if (*tmp == 91 || *tmp == 123)*tmp = 'A';
        *tmp++;
        *tmp2++;
        }
    
    
    char *ntmp = str_out;
    const char *tmp3 = str_out;



    for (int i = 0; i < len; i++){
        if (*tmp3 == 'e' || *tmp3 == 'E')*ntmp='E';
        else if (*tmp3 == 'i' || *tmp3 == 'I')*ntmp='I';
        else if (*tmp3 == 'o' || *tmp3 == 'O')*ntmp='O';
        else if (*tmp3 == 'u' || *tmp3 == 'U')*ntmp='U';
        else if (*tmp3 >= 66 && *tmp3 <= 90)*ntmp+=32;
        *ntmp++;
        *tmp3++;
    }

     *ntmp = '\0';
  return str_out;
}


/*
#include <ctype.h>
#include <string.h>

char *change_it_up (char *str_out, const char *str_in)
{
  char *retval = str_out;

  for (char ch; (ch = *str_in); str_in++, str_out++) {
    if (isalpha(ch)) {
      ch = 'a' + ((tolower(ch) - 'a' + 1) % 26);
      if (strchr("aeiou", ch))
        ch = toupper(ch);
    }
    *str_out = ch;
  }
  *str_out = '\0';
  return retval;
}
*/


/*
#include <ctype.h>

char *change_it_up (char *o, const char *str_in)
{
  int i=-1;
  while (str_in[++i]){
    switch (tolower(str_in[i])){
        case 'a':o[i]='b';break;
        case 'b':o[i]='c';break;
        case 'c':o[i]='d';break;
        case 'd':o[i]='E';break;
        case 'e':o[i]='f';break;
        case 'f':o[i]='g';break;
        case 'g':o[i]='h';break;
        case 'h':o[i]='I';break;
        case 'i':o[i]='j';break;
        case 'j':o[i]='k';break;
        case 'k':o[i]='l';break;
        case 'l':o[i]='m';break;
        case 'm':o[i]='n';break;
        case 'n':o[i]='O';break;
        case 'o':o[i]='p';break;
        case 'p':o[i]='q';break;
        case 'q':o[i]='r';break;
        case 'r':o[i]='s';break;
        case 's':o[i]='t';break;
        case 't':o[i]='U';break;
        case 'u':o[i]='v';break;
        case 'v':o[i]='w';break;
        case 'w':o[i]='x';break;
        case 'x':o[i]='y';break;
        case 'y':o[i]='z';break;
        case 'z':o[i]='A';break;
        default: o[i]=str_in[i];
    }
  }
  o[i] = '\0';
  return o;
}
*/