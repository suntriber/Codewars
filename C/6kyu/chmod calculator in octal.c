#include <stdio.h>
#include <stdlib.h>

char *chmod_calculator (char octal[4],
	const char user[3], const char group[3], const char other[3]);

int main(){


    char *octal = malloc(sizeof(char)*4);

    printf("%s --> %s\n", chmod_calculator(octal, "rw-", "rw-", "rw-"), "666");
    printf("%s --> %s\n", chmod_calculator(octal, NULL, "rw-", NULL), "666");



    

    return 0;
}



char *chmod_calculator (char octal[4],
	const char user[3], const char group[3], const char other[3])
{

    int i, sum;
    const char *p[3] = {user, group, other};

    for (i = 0; i < 3; i++){
    sum = 0;

    if (!(p[i])){
      octal[i]='0';
      continue;
    }
    
    if (p[i][0] == 'r')sum+=4;
    
    if (p[i][1] == 'w')sum+=2;
    
    if (p[i][2] == 'x')sum+=1;
    
    octal[i] = (char) sum + 48;
    }

	octal[i] = '\0';
	return octal;

}