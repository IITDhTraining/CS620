
%{ 
#include<iostream>
#include<cstring>
#include "microParser.tab.hpp"
int lineCount=1;
%} 
  
%%


PROGRAM 			{return PROGRAM;}
BEGIN 				{return _BEGIN;}
END 				{return END;}
FUNCTION 			{return FUNCTION;}
READ 				{return READ;}
WRITE 				{return WRITE;}
IF 				{return IF;}
ELSE 				{return ELSE;}
ENDIF 				{return ENDIF;}
WHILE 				{return WHILE;}
ENDWHILE 			{return ENDWHILE;}
BREAK 				{return BREAK;}
CONTINUE			{return CONTINUE;}
RETURN 				{return RETURN;}
INT 				{return INT;}
VOID 				{return VOID;}
STRING				{return STRING;}
FLOAT				{return FLOAT;}


\+				{return SUM;}
-				{return SUB;}
\*				{return MUL;}
\/				{return DIV;}
=				{return EQ;}
!=				{return NEQ;}
\<				{return LT;}
\>				{return GT;}
\<=				{return LTE;}
\>=				{return GTE;}
,				{return COMMA;}
;				{return SEMICOLON;}
:=				{return ASSIGNOP;}
\(				{return LPAREN;}
\)				{return RPAREN;}

([0-9])*\.([0-9])+		{ return FLOATLITERAL;}
([a-zA-Z])([a-zA-Z]|[0-9])*	{ return IDENTIFIER;}
[0-9]+			{ yylval.intliteraldata=new std::pair<int, int>(); (yylval.intliteraldata)->first=atoi(yytext);(yylval.intliteraldata)->second=lineCount;return INTLITERAL;}
\"[^\"]*\"		{ yylval.stringliteraldata=new std::pair<std::string, int>; (yylval.stringliteraldata)->first=std::string(yytext);(yylval.stringliteraldata)->second=lineCount;return STRINGLITERAL;}
\n 			{lineCount++;}

.|\t {}


\--.* {}

%% 

int yywrap(){return 1;} 
 
