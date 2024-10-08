from pathlib import Path
import typer
import json
from typing_extensions import Annotated
from antlr4 import *

import util

app = typer.Typer()

@app.command()
def tokenize(
    grammar_path: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=False,
            dir_okay=True,
        ),
    ],
    input: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
        ),
    ] = "/dev/stdin",
):
    _, Lexer = util.get_grammar(grammar_path)
    stream = FileStream(input, encoding='utf-8')
    lexer = Lexer(stream)
    token_type_map = {
        symbolic_id + len(lexer.literalNames) - 1: symbolic_name
        for symbolic_id, symbolic_name in enumerate(lexer.symbolicNames)
    }

    print(token_type_map)
    while True:
        token = lexer.nextToken()
        print(token.type)
        type_ = token_type_map.get(token.type, "literal")
        text_ = token.text.strip()
    
        if(text_):
            print(f"{type_}: {text_}")
        else:
            print(type_)

        if token.type == token.EOF:
            break


@app.command()
def parse(
    grammar_path: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=False,
            dir_okay=True,
        ),
    ],
    input: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
        ),
    ] = "/dev/stdin",
):
    stream = FileStream(input, encoding='utf-8')
    mod, _ = util.get_grammar(grammar_path)
    tree = mod.get_parse_tree(stream)
    printer = util.GenericPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == "__main__":
    app()