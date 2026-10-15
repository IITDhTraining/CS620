# This codebase contains examples showing loop unrolling and fusion in LLVM.
-`make looppeel` to see loop unrolling with `looppeel.c` present in the `test` directory. Change `x=y` to `x=y+1` in the `looppeel.c` and observe the changes.

-`make looppeel2` to see loop unrolling with `looppeel.c` present in the `test` directory. In this example you can see that the loop body is rid of conditionals (if-else).

- `make unroll1` to see that unrolling takes effect with inlining of a function. In this example, `unroll1.c` present in the `test` directory is used. 

- `make unroll2` to see unrolling being done dynamically at runtime. You can specify arguments to LLVM's `opt` specifying unroll count, the number of iterations to unroll.
 
- Change directory to `Loop\_Fusion` and  `make run` produces unoptimized LLVM IR for a sample program, `loopfusion.c`, translates this to optimized version using the `mem2reg` pass, then chains a sequence of optimizations (including `loop-fusion`) and passes them to the `opt` pass pipeline to produce the IR with fused loops in `loop_fused.ll`.

Also, `.png` files for CFG corresponding to unoptimized and fused LLVM IR are produced.
