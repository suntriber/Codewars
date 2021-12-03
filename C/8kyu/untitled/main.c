#include <stdio.h>
#include <string.h>
/*
Description:
Make a simple function called greet that returns the most-famous "hello world!".

Style Points
Sure, this is about as easy as it gets. But how clever can you be to create the most creative
hello world you can think of? What is a "hello world" solution you would want to show your friends?

 */

char* greet();

int main() {
    printf("%s\nHello, World!\n", greet());
    return 0;
}

char* greet(){
    return "Hello, World!";
}


/*
const char *greet(){
  return ! "why" ? "am i doing this": "hello world!";
}


__asm__(".globl greet\nl: .asciz \"hello world!\"\ngreet: mov $l, %rax\nret\n");


void ft_putchar(char c)
{
  write(1, &c, 1);
}

void ft_putstr(char *s)
{
  int i;
  i = 0;

  while (s[i] != '\0')
  {
    ft_putchar(s[i]);
    i++;
  }
}

void greet()
{
  ft_putstr("hello world!");
}


const char* greet() {
  char *result = malloc(13);

  result[12] = (result[11] = ((result[5] = (result[10] = (result[8] = (result[6] = (result[7] = result[4] = (result[9] = result[3] = result[2] = (result[1] = (result[0] = 104) - 3) + 7) + 3) + 8) - 5) - 14) - 68) + 1)) - 33;

  return result;
}


 */