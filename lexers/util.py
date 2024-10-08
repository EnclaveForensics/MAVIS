import sys
from pathlib import Path
import contextlib
import importlib
import collections
from typing import TypeVar, List, Iterator, Tuple, Iterable
from antlr4 import *

@contextlib.contextmanager
def sys_path_prepend(paths: List[Path]) -> Iterator[None]:
    sys.path = list(map(str, paths)) + sys.path
    yield
    sys.path = sys.path[len(paths) :]


def get_grammar(grammar_path: Path):
    name = grammar_path.stem.title()
    with sys_path_prepend([grammar_path]):
        mod = importlib.import_module("main", package=None),
        Lexer = getattr( importlib.import_module(f"{name}Lexer", package=None), f"{name}Lexer")
        return (mod[0], Lexer)

class GenericPrintListener(ParseTreeListener):
    depth = 0

    def __init__(self):
        sys.setrecursionlimit(10000)

    def visitTerminal(self, node:TerminalNode):
        #node.symbol is a token
        #print(f"{node.symbol.type} {node.symbol.text}")
        print(node.symbol.type, end=',')

    def enterEveryRule(self, ctx):
        #print(ctx.getRuleContext())
        rule_name = ctx.parser.ruleNames[ctx.getRuleIndex()]
        #print((self.depth * " ") + rule_name)
        #print(rule_name)
        self.depth += 1

    def exitEveryRule(self, ctx):
        self.depth -= 1
        if self.depth <= 0:
            print()
