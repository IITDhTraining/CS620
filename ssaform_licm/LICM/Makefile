build: 
	mkdir -p build;cd build; cmake ..;make; cd ..

run:
	clang -S -O1 -Xclang -disable-llvm-passes -emit-llvm ../licm.c -o ../licm.ll
	opt -passes=mem2reg -S ../licm.ll -o ../licm_mem2reg.ll
	opt -load-pass-plugin ./build/src/LICMPass.so -passes=licm-invariant -S ../licm_mem2reg.ll -o ../licm.ll.output 
	opt -passes=dot-cfg -cfg-dot-filename-prefix=licm ../licm.ll
	dot -Tpng licm.main.dot -o ../licm_before_hoisting.png
	opt -passes=dot-cfg -cfg-dot-filename-prefix=licm ../licm.ll.output
	dot -Tpng licm.main.dot -o ../licm_after_hoisting.png

clean:
	rm -f ../licm*.o
	rm -f ../licm*.output
	rm -rf build
	rm -f ../licm*.ll
	rm -f ../licm*.png
	rm -f *.dot
