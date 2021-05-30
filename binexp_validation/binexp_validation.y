%{
#include<stdio.h>
#include<stdlib.h>
int yylex();
int yyerror(char* s);
%}

%token num

%%
P:P'@'Q
|Q
;
Q:Q'&'R
|R
;
R:'('P')'
|num
;
%%

int main()
{
	printf("Enter an expression\n");
	yyparse();
	printf("Valid expression\n");
	return 0;
}

int yyerror(char* s)
{
	printf("\nInvalid Expression\n");
	exit(0);
}

