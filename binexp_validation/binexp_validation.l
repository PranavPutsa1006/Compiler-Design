%{
#include "y.tab.h"
%}

%%
[01]+ {return num;}
. {return yytext[0];}
\n {return 0;}
%%

