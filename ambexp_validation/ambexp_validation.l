%{
#include "y.tab.h"
%}

%%
[0-9]+ {return NUMBER;}
[a-zA-Z]+ {return ID;}
. {return yytext[0];}
\n {return 0;}
%%
