%{ 
#include<stdio.h>
#include<stdlib.h>
int intcount = 0, vlcount = 0;
%}

letter [a-zA-Z]
digit [0-9] 
vowel [aeiouAEIOU]

%%
[aeiouAEIOU]+.[a-zA-Z0-9.]*				vlcount++;
{digit}*[^"000"]+{digit}*				intcount++;
%% 

int yywrap()
{
	return 1;
}

int main(void) 
{   
    yyin = fopen("input.txt","r");
    yylex();
    printf("number of lines starting with vowels: %d\n", vlcount);
    printf("number of integers: %d\n", intcount);
    fclose(yyin);
    return 0; 
} 

