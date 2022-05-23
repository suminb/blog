---
categories:
  - Review
published: true
date: 2015-03-26
redirect_from:
  - /post/an-introduction-to-opencl-programming-model
title: Paper Review - An Introduction to OpenCL Programming Model
---

This paper nicely outlines the basic concepts of general purpose GPU programming with OpenCL. This article will summarize some of the important concepts.

### Hardware Architecture

OpenCL provides a level of abstraction to execute general purpose code written in a subset of C on computing devices such as GPUs and CPUs. The basic concept is that a host controls multiple *compute devices* that are comprised of *compute units*. All these compute units execute OpenCL *kernels*; informally speaking, a kernel is a function that is executed on the compute units in parallel.

(TODO: explain marketing terminologies...)

### Execution Models

One of the somewhat unfamiliar concepts from the OpenCL programming is execution of kernels over N-dimensional arrays; this is called a *domain*. Each independent element of execution in this domain is called a *work-item*, and these work-items are grouped together into independent *work-groups*.

OpenCL exploincets both (fine-grained data parallelism and thread parallelism)

* Data-parallel programming: simultaneous execution of the identical function over the elements of a dataset
* Task-parallel programming: simultaneous execution of different functions across the same or different datasets

Copying data from DRAM to global GPU memory is slow.
Copying data from global GPU memory to local work-group memory is also slow.

Single-Instruction, Multiple-Thread (SIMT) architecture allows for more compact thread execution logic, but it *probably* limits more sophisticated functionalities that are available on x86 processors such as branch prediction, speculative execution, and out-of-order executions.

### Memory Models

The OpenCL memory hierarchy resembles that of a host machine in which has multiple levels of cache memories and the main (global) memory. Sensibly, the further away the momory from the processing unit, the larger and slower the memory becomes.

Work-groups may share data through shared memory, but each work-group is assigned with local memory from which cannot be accessed outside the work-group.

An important issue is that memory access, either global or local, is not protected in any way. Referencing a memory block outside the *boundary* will not be detected, which implies memory blocks reserved the operating system may be intruded; this can result in peculiar behaviors ranging from blinking screens up to unrecoverable crashes.