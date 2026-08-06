compiler: scanner
	g++ lex.yy.c -o compiler

scanner: scanner.l
	flex $<

clean:
	rm -f lex.yy.c
	rm -f compiler
