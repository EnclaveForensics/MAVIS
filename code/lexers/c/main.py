import sys
from antlr4 import *
from CLexer import CLexer
from CParser import CParser
from CListener import CListener

class CPrintListener(CListener):
    def enterExpression(self, ctx: CParser.ExpressionContext):
        print(ctx)

def get_parse_tree(input_stream):
    lexer = CLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    return parser.translationUnit()

def main(argv):
    input_stream = FileStream(argv[1])
    tree = get_parse_tree(input_stream)
    printer = CPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
