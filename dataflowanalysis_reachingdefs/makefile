TESTCASE=test/example4

reachingdefs: $(TESTCASE).c ./reachingdefs/reachingdefs.cpp
	clang -cc1 -disable-O0-optnone $< -emit-llvm  -O0
	opt -load-pass-plugin=./reachingdefs/build/reachingdefs.so -passes="my-module-pass" -disable-output  $(TESTCASE).ll
	opt -passes=dot-cfg -cfg-dot-filename-prefix=$(TESTCASE) $(TESTCASE).ll
	dot -Tpng $(TESTCASE).test.dot -o $(TESTCASE).png

clean:
	rm -f $(TESTCASE).ll 
	rm -f ./reachingdefs/build/reachingdefs.so ./liveness/build/liveness.so

