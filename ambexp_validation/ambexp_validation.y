%{
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int yylex();
int yyerror(char* s);
%}

%token NUMBER ID
%left '+' '-'
%left '*' '/' '%'
%right '^'
%left UMINUS
%left '(' ')'

%%
T:T'+'T
|T'-'T
|T'*'T
|T'/'T
|T'^'T
|'-'T
|'('T')'
|NUMBER
|ID
;
%%

int main()
{
	printf("Enter the expression\n");
	yyparse();
	printf("Valid expression\n");
	return 0;
}

int yyerror(char* s)
{
	printf("\n Expression is invalid\n");
}
