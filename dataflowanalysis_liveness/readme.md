# Liveness Analysis with LLVM

This directory contains a demo of live variable analysis using LLVM. 

First you need to build the pass plugin, `liveness.so`, corresponding liveness analysis. This is implemented as analysis passes in LLVM. Upon successful build, `liveness.so` is created.
To build the plugin `liveness.so` execute the following steps:

```
cd liveness
mkdir build
cd build
cmake ..
make
```

Once you build this successfully, you need to run the liveness analysis on a sample C program.

2. **Running liveness analysis**
 
 `make liveness` - This command by default, runs a liveness analysis on `example4.c` present in the `test` directory. 


## III. Exercise
The `liveness.cpp` present in the `liveness` directory is buggy as shown in class. Fix this to print correct liveIN sets.
