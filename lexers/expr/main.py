import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener

class ExprPrintListener(ExprListener):
    def enterExpr(self, ctx):
        print(ctx)

def get_parse_tree(input_stream):
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    return parser.prog()

def main(argv):
    input_stream = FileStream(argv[1])
    tree = get_parse_tree(input_stream)
    printer = ExprPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
