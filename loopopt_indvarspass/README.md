# CS620 Demo 
This directory contains a code example for visualizing induction variable simplification using the `indvars` pass in LLVM.
The `invarsimplify.c` contains the C code. The `makefile` begins by emitting LLVM IR for this file using some flags. A noteworthy mention is the `disable-O0-optnone` flag: when you compile the code with `-O0` flag, LLVM inserts flags to IR that prevents further optimizations. `disable-O0-optnone` flag says not to enable this flag and allow further optimizations. In our example we want further optimizations (induction variable simplification).  

execute `make` and observe `_promoted.ll` and `.output` files. You can also visualize the corresponding CFG by opening the `.png` files with corresponding names.



