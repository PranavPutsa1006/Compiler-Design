%{
#include<stdio.h>
#include<stdlib.h>
int yylex();
int yyerror(char* s);
%}

%token num

%%
E:E'+'T
|E'-'T
|T
;
T:T'*'F
|T'/'F
|F
;
F:num
|'('E')'
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
