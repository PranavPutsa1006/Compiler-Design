%{ 
#include<stdio.h>
int count = 0;
%} 

DIGIT [0-9]
LETTER [a-zA-Z]
ID [a-z A-z _][a-z A-z 0-9]*
  
%%
{LETTER}({LETTER}|{DIGIT}|"_")*	count++;
-1 return 0;
%% 

int yywrap()
{
	return 1;
}

int main(void) 
{   
    yylex();
    printf("number of identifiers: %d\n", count);
    return 0; 
} 
