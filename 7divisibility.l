%{ 
#include<stdio.h>
int i;
%}

digit [0-9]

%%

{digit}+		{i=atoi(yytext);
				if(i%7==0)
					printf("Divisible by 7");
				else
					printf("Not divisible by 7");
			}
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
