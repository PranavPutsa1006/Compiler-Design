%{ 
#include<stdio.h>
int ccount = 0, wcount = 0, lcount = 0;
%}
  
%%
\n			{lcount++; ccount++;}
-1 return 0;
[^ \t\n]+	{wcount++; ccount += yyleng;}
.			{ccount++;}
%% 

int yywrap()
{
	return 1;
}

int main(void) 
{   
    yylex();
    printf("number of characters: %d\n", ccount);
    printf("number of words: %d\n", wcount);
    printf("number of lines: %d\n", lcount);
    return 0; 
} 
