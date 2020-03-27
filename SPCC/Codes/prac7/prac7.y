%{
    #include <stdio.h>
    int yyerror(char *);
    int yylex(void);
%} 

// setting the precedence
// and associativity of operators
%token INTEGER
%left '+' '-'
%left '*' '/'

/* Rule Section */
%%
E : T { printf("Result = %d\n", $$);return 0;}
T : T '+' T {$$ = $1 + $3;}
| T '-' T {$$ = $1 - $3;}
| T '*' T {$$ = $1 * $3;}
| T '/' T {$$ = $1 / $3;}
| INTEGER {$$ = $1;}
;
%%

int main(void){
    printf("Enter the expression\n");
    yyparse();
    return 0;
}

/* For printing error messages */
int yyerror(char* s){
    printf("\nExpression is invalid\n");
    return 0;
}