%{
#include <stdio.h>
int valid = 0;
int invalid = 0;
%}

%%
[\n] ;
(^[0-9])|[^_a-zA-Z0-9] invalid++;
^[_a-zA-Z][_a-zA-Z0-9]*$ valid++;
.  ;
%%

int main()
{
    printf ("This Lex program counts the number of valid and invalid identifies in text\n");
    printf ("Enter the text and terminate it with CTRL-d.\n");
    yylex();
    printf ("Invalid: %d, Valid = %d\n", invalid, valid);
    return 0;
}

int yywrap(){
    return 1;
}

// This Lex program counts the number of valid and invalid identifies in text
// Enter the text and terminate it with CTRL-d.
// abc
// 0abc
// #sas
// sad#
// asd_as
// asd7asd
// _
// asd$qw4
// Invalid: 3, Valid = 4