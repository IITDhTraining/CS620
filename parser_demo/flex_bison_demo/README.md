
# Parser usage and demo
This directory contains the starter materials to demonstrate the use of a parser generator tool called Bison. Bison takes a grammar file as input and produces C/C++ code. This C/C++ file becomes the implementation of your parser. The parser expects tokens from scanner implementation. So, if you are using Flex to generate your scanner implementation, then you need to know how to pass data from scanner to parser. Please see `Bison_QuickStart.pdf` present in this repo.

`scanner.l` contains regular expressions to match integer literals, plus symbol, newline and take some action.

`grammar.y` contains the definitions of tokens, grammar rules (productions), and prologue and epilogue code to be inserted in the Bison generated `grammar.tab.c` file. Using this file with Bison as in:

`bison -d grammar.y` (-d is for generating the header file called grammar.tab.h)

results in a warning: `grammar.y: warning: 1 shift/reduce conflict [-Wconflicts-sr]`. This is because the grammar specified in the `grammar.y` file is ambiguous. To resolve the ambiguity, we chose to specify `%left PLUS` in the declarations section of `grammar.y` file (note: the `grammar.y` file provided doesn't have this line inserted. As an exercise, you need to insert this line in the declarations section.). 

Executing `make` command generates the scanner file, `lex.yy.c` and parser files: `grammar.tab.c` and `grammar.tab.h`. Also, the generated c files are compiled to produce an executable called `compiler`. Executing this would expect you to input an expression such as 2+3 on the terminal.  
```
./compiler
```

If you want to print the result of the expression 2+3, you need to pass values from scanner to the parser. 

1. To pass INTLITERAL value from the scanner, insert `yylval=atoi(yytext);` in the action block corresponding to `[0-9]+` pattern in `scanner.l` (note that you can insert any valid C/C++ code in the action block. ).

2. Now in the action block of a grammar rule (wherever you want to print), you need to catch the value passed from scanner. To do this, insert `$$=$1 + $3;` in the action block corresponding to `E: E PLUS E` rule and `$$=$1;` in the action block of the `E: INTLITERAL` rule. With these changes, the values of E get set correctly and flow up the parse tree.  

3. To print the values, you need to make changes in the `printf` statements of the action blocks.


**Discussion**: this code example uses the default type, int, for `yylval`. If you want to pass objects, check the `demo` directory in this repository. 

## Prerequisites
```
sudo apt install flex
sudo apt install bison
```



