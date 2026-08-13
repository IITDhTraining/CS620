#include<iostream>
#include "microParser.tab.hpp"
extern FILE * yyin;
int main(int argc, char* argv[]){ 
	FILE *fp;
	fp = fopen(argv[1],"r"); 
	yyin = fp; 
	yyparse(); 
  
return 0; 
}

void yyerror(char const* errmsg) {
	printf("Not accepted\n");
}


