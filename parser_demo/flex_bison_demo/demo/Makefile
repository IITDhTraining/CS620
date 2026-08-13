NAME = Nikhil Hegde
EMAIL = nikhilh@iitdh.ac.in

compiler: 
	bison -d microParser.ypp
	flex scanner.l
	@g++ -g main.cpp microParser.tab.cpp lex.yy.c -o compiler
clean:
	@rm -f lex.yy.c* *.tab.* compiler

dev:
	@echo $(NAME)
	@echo $(EMAIL)
