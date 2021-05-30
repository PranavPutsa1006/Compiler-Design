%{ 
#include<stdio.h>
#include<stdlib.h>
int ccount = 0, vcount = 0;
%}

letter [a-zA-Z] 

%%
[aeiouAEIOU]		vcount++;
{letter}			ccount++; 
-1 return 0;
%% 

int yywrap()
{
	return 1;
}

int main(void) 
{   
    yyout = fopen("def.txt","w");
    yylex();
    printf("number of vowels: %d\n", vcount);
    printf("number of consonants: %d\n", ccount);
    fclose(yyout);
    return 0; 
} 
