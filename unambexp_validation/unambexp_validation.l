%{
#include "y.tab.h"
%}

%%
[0-9]+ {return num;}
. {return yytext[0];}
\n {return 0;}
%%
