%{
#include "y.tab.h"
extern yylval;
%}

%%
[0-9]+	{yylval = atol(yytext); return num;}
[\t]+ 	;
\n		{return 0;}
.		{return yytext[0];}

%%
