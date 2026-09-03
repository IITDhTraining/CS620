# (Clang AST)

This directory contains code examples to traverse AST in clang and more. You will be doing an in-tree build and linking with libraries that are built from LLVM source.

## I. Installing `llvm`

```
git clone https://github.com/llvm/llvm-project.git
git checkout tags/llvmorg-20.1.0
```

Building with cmake:
```
mkdir llvm-project/build
cd llvm-project
cmake -S llvm -B build -G Ninja \
   -DLLVM_ENABLE_PROJECTS=llvm;clang;clang-tools-extra;lldb;lld \
   -DLLVM_BUILD_EXAMPLES=ON \
   -DLLVM_TARGETS_TO_BUILD="Native;NVPTX;AMDGPU" \
   -DCMAKE_BUILD_TYPE=Debug \
   -DLLVM_ENABLE_ASSERTIONS=ON \
   -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DLLVM_ENABLE_LLD=ON
ninja -C -build . 
```
If you have the `llvm-project` created other than in the home drive, you need to modify `setenv.sh` to tell the `PATH` variable to find the newly built compiler in the specific location. 

execute the command `source setenv.sh`

## II. Usage
`find-class-decls` contains the source code. copy this directory inside the llvm/clang-tools-extra directory. 

Execute `ninja` command to build the library (your AST analyzer)

`./bin/find-class-decls “namespace n { namespace m {class C {}; }}”`

To refer to the class C in the code snippet passsed as argument above, one would use n::m::C and this is the pattern that we are trying to match. In the input argument to find-class-decls we provide a code snippet with matching pattern and hence, we see print statement on the terminal.

To view the AST corresponding to any C program, say in `test.c`:
`clang -Xclang -ast-dump -fsyntax-only test.c`

In the above command, what follows `-Xclang` are arguments to Clang parser. `-ast-dump` is telling to dump the AST. `-fsyntax-only` is telling Clang to stop processing at semantic processing stage. Note that the C program in `test.c` need not have a `main` function. If you were to omit `-fsyntax-only` you would see a linker error.
