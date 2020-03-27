%{
#include <stdio.h>
int vowels = 0;
int consonants = 0;
%}

%%
[aeiouAEIOU]  vowels++;
[a-zA-Z]  consonants++;
[\n]  ;
.  ;
%%

int main()
{
    printf ("This Lex program counts the number of vowels and ");
    printf ("consonants in given text.");
    printf ("\nEnter the text and terminate it with CTRL-d.\n");
    yylex();
    printf ("Vowels = %d, consonants = %d.\n", vowels, consonants);
    return 0;
}

int yywrap(){
    return 1;
}

/*
helOlo iAm huMan
Vowels = 7, consonants = 7.
*/