import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprListener import ExprListener

class ExprPrintListener(ExprListener):
    # def enterProg(self, ctx):
    #     print(ctx.expr())

    def enterExpr(self, ctx):
        token = ctx.INT()
        if token is not None:
            print(ctx.INT())

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    printer = ExprPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
