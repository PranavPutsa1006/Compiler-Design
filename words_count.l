%{ 
#include<stdio.h>
int wcount = 0;
%}
  
%%
-1 return 0;
[^ \t\n]+	{wcount++;}
%% 

int yywrap()
{
	return 1;
}

int main(void) 
{   
    yylex();
    printf("number of words: %d\n", wcount);
    return 0; 
} 
