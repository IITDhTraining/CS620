# CS620 Demo 
This directory contains code examples for viewing phi nodes in LLVM IR, CFG, Dominators, Dominator Tree, Dominance frontier, and loop-invariant-code-motion optimization (licm).

- execute the make command with different targets as mentioned in the makefile. To execute some of the targets, you need to build `MyPass.so`. To do this, check the `fnmodpass` directory.
- to visualize the licm optimization, `cd LICM` and follow the README mentioned therein.

exercise: `make domfrontier` may not print the info that you see on the slide. Fix this.


