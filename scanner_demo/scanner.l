%{ 
#include <iostream>
using namespace std;
%} 
  
%%

" "|\n|\t

PROGRAM|BEGIN|END|FUNCTION|READ|WRITE|IF|ELSE|ENDIF|WHILE|BREAK|CONTINUE|ENDWHILE|RETURN|INT|VOID|STRING|FLOAT {cout << "Token Type: KEYWORD"<< endl<<"Value: "<< yytext << endl;}

:=|\+|\-|\*|\/|=|\!=|<|>|\(|\)|\;|,|<=|>= {cout << "Token Type: OPERATOR"<< endl<<"Value: "<< yytext << endl;}

[A-Za-z][A-Za-z0-9]*	{cout << "Token Type: IDENTIFIER"<< endl<<"Value: "<< yytext << endl;}

[0-9]+	{cout << "Token Type: INTLITERAL" << endl<<"Value: "<<yytext << endl;} 

[0-9]*\.[0-9]+	{cout << "Token Type: FLOATLITERAL" <<endl<<"Value: "<< yytext << endl;}

\".*\"	{cout << "Token Type: STRINGLITERAL" <<endl<<"Value: "<< yytext << endl;}

\/\/.*

%% 
//exercise: find out why you need the below definition
int yywrap(){return 1;} 

int main(int argc, char* argv[]){ 
//test2
FILE *fp;
fp = fopen(argv[1],"r"); 
yyin = fp; 
  
yylex(); 
 
fclose(fp);
  
return 0; 
} 
