import sys
from antlr4 import *
from CLexer import CLexer
from CParser import CParser
from CListener import CListener

class CPrintListener(CListener):
    def enterExpression(self, ctx: CParser.ExpressionContext):
        print(ctx)

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.translationUnit()
    printer = CPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
