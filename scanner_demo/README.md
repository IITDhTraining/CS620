
# Scanner implementation and demo
This directory contains the starter materials to demonstrate the use of a scanner generator tool called Flex. Flex translates input regular expressions and produces a c/c++ file. This C/C++ file becomes the implementation of your scanner.

`scanner.l` is the input to the Flex tool. This contains the definition of tokens (defined using regular expressions). 

`fibonacci.micro` is a sample program in a toy language called MICRO. You can tokenize this program. See next.

The command `flex scanner.l` produces `lex.yy.c`, which is the scanner implementation. Currently, this program accepts a file name (in the current directory) as argument.  You can pass `fibonacci.micro` as an argument on the command line as in:

```
./compiler fibonacci.micro
```

To obtain the executable `compiler` see usage next.

## Prerequisites
```
sudo apt install flex
```

## Usage
```
make scanner
make compiler
./compiler fibonacci.micro
```

`make scanner` actually executes the command `flex scanner.l`. This produces `lex.yy.c`. `make compiler` compiles the `lex.yy.c` using g++ to produce an executable called `compiler`.

When you execute the command `./compiler fibonacci.micro` you see lot of printing on the terminal. This is actually telling you what the tokens of the input `fibonacci.micro` are and what category they belong to.


