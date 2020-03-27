/*lex program to count number of words*/
%{ 
#include<stdio.h> 
#include<string.h> 
int words = 0; 
int spaces = 0;
int lines = 0;
%} 
  
/* Rules Section*/
%%
[\n] lines++;
([a-zA-Z0-9])* words++;
([ ]) spaces++;
. ;
%% 
  
int main() 
{    
    printf ("This Lex program counts the number of words, blank spaces and lines");
    printf ("\nEnter the text and terminate it with CTRL-d.\n");
    // The function that starts the analysis 
    yylex();
    printf("The number of words are %d\n", words);
    printf("The number of spaces are %d\n", spaces);
    printf("The number of lines are %d\n", lines);
    return 0;
} 

int yywrap(){
    return 1;
}

/*
Output
This Lex program counts the number of words, blank spaces and lines
Enter the text and terminate it with CTRL-d.
Hi I am human
I come in peace
The number of words are 8
The number of spaces are 6
The number of lines are 2
*/