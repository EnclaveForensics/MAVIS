---
layout: ../layouts/Basic.astro
title: Abstract Syntax Trees
---
An **Abstract Syntax Tree (AST)** is a data structure used primarily in compilers and interpreters to represent the structure of source code in a hierarchical, tree-like form. Unlike the concrete syntax or parse tree, which closely mirrors the grammar and structure of the source code (including all syntax details like parentheses, commas, and keywords), an AST abstracts away extraneous syntactic details and focuses on the semantic structure of the program.

### Structure and Purpose

An AST represents programming language constructs as tree nodes. Each node corresponds to a language construct, such as a variable declaration, expression, statement, or function. The children of a node represent its components. For example, an assignment expression like `x = a + b` would be represented in an AST as a root node for the assignment operation (`=`), with `x` as the left child and an addition node (`+`) as the right child, which in turn has `a` and `b` as its children.

The AST serves as an intermediate representation (IR) in the compilation pipeline. It is used in various phases of the compilation process, including:

* **Semantic analysis**: Verifying that the program is semantically correct (e.g., type checking, variable scope resolution).
* **Optimization**: Simplifying or transforming the code to improve performance or efficiency.
* **Code generation**: Translating the AST into target code, such as machine code or bytecode.

An AST is often confused with a *Parse Tree*.

### AST vs. Parse Tree

The **parse tree** is a direct representation of the grammar rules applied during parsing, and contains all syntactic details, including punctuation, grouping symbols, comments, and more. In contrast, the AST omits these details and retains only the essential structure necessary for further analysis or execution. For example, while a parse tree for `(x + y)` would include nodes for the parentheses, the AST would only include a binary operation node with `x` and `y` as children.

### Construction of AST

ASTs are typically constructed by parsers during or after the parsing phase. There are two main types of parsers in this context:

* **Top-down parsers**, such as recursive descent parsers, can build ASTs incrementally as they recognize each production rule.
* **Bottom-up parsers**, such as LR parsers, may use semantic actions during reductions to construct AST nodes.

Each parser rule in a grammar can be associated with an action that creates or modifies AST nodes.

### Example

Consider the code:

```c

/* A function named sum */
int sum(int a, int b) {
    /* This function will add inputs and return the sum */
    return a + b;
}


```

The AST for this code would contain nodes for:

* A function declaration (`sum`)
* Parameter list (`a`, `b`)
* Return statement
* Binary operation (`+`)
* Variable references (`a`, `b`)

All syntactic details like semicolons, parentheses, comments and similar are excluded from the AST. This provides us a cleaner and somewhat standardized way to identify the actual logic in the code.

### Benefits

* **Simplification**: Reduces complexity by eliminating redundant syntax.
* **Manipulability**: Easier to traverse and manipulate for tasks such as optimization or transformation.
* **Portability**: Abstract representation makes it adaptable for various backend targets.
