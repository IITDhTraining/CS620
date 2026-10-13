#simplifies induction variable (eliminates)
indvarsimplify: invarsimplify.c
	clang -emit-llvm -S -Xclang -disable-O0-optnone $< -o invarsimplify.ll
	opt -passes=mem2reg -S invarsimplify.ll -o invarsimplify_promoted.ll
	opt -passes=indvars -S invarsimplify_promoted.ll -o invarsimplify.output
	opt -passes=dot-cfg -cfg-dot-filename-prefix=invarsimplify invarsimplify.ll
	dot -Tpng invarsimplify.foo.dot -o invarsimplify.png
	
	opt -passes=dot-cfg -cfg-dot-filename-prefix=invarsimplify_promoted invarsimplify_promoted.ll
	dot -Tpng invarsimplify_promoted.foo.dot -o invarsimplify_promoted.png
	
	opt -passes=dot-cfg -cfg-dot-filename-prefix=invarsimplify_output invarsimplify.output
	dot -Tpng invarsimplify_output.foo.dot -o invarsimplify_output.png
clean:
	rm -rf *.ll *.output *.png *.dot
