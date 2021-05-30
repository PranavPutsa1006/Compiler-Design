%{
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int yylex();
int yyerror(char* s);
%}

%token num

%%
S:E
{
	printf("Result = %d\n", $$);
}
E:E'+'T	{$$=$1+$3;}
|E'-'T	{$$=$1-$3;}
|T		{$$=$1;}
;
T:T'*'F	{$$=$1*$3;}
|T'/'F	{$$=$1/$3;}
|F		{$$=$1;}
;
F:num	{$$=$1;}
|'('E')'{$$=$2;}
;
%%

int main()
{
	printf("Enter an expression\n");
	yyparse();
	return 0;
}

int yyerror(char* s)
{
	printf("\nInvalid Expression\n");
	exit(0);
}
