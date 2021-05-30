%{ 
#include<stdio.h>
#include<stdlib.h>
%}

letter [a-zA-Z]
digit [0-9]
id [a-zA-Z][a-zA-Z0-9]*

%%
"<".*".h>"			printf("A header file: %s\n",yytext);
if|then|begin|end|procedure|function|for		{printf("A keyword: %s\n",yytext);}
">="|">"|"<="|"<"|"=="|"!="			{printf("A relational operator: %s\n",yytext);}
[/][/].*[^\n]		printf("Single line comment\n");
"/*".*(\n|.*|^"/*")*"*/"	printf("Multi line comment\n");
#.*			printf("A preprocessor directive");
{id}		printf("An identifier: %s\n",yytext);
int|float|double|char		printf("A data type: %s\n",yytext);
{digit}		printf("A digit: %s\n",yytext);
-1 return 0;
%% 

int yywrap()
{
	return 1;
}

int main(void) 
{   
    yylex();
    return 0; 
} 
