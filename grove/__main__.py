"""Uso: python -m grove arquivo.cj [--tokens] [--ast]

Sem flags imprime os dois. Sai com código 1 em erro léxico ou sintático.
"""
import argparse
import sys

from . import LexError, ParseError, dump, parse, tokenize


def main(argv=None):
    ap = argparse.ArgumentParser(prog="grove", description=__doc__.splitlines()[0])
    ap.add_argument("arquivo")
    ap.add_argument("--tokens", action="store_true", help="imprime a tabela de tokens")
    ap.add_argument("--ast", action="store_true", help="imprime a AST")
    args = ap.parse_args(argv)
    if not (args.tokens or args.ast):
        args.tokens = args.ast = True

    with open(args.arquivo, encoding="utf-8") as f:
        src = f.read()

    try:
        tokens = tokenize(src)
        if args.tokens:
            print("LINHA:COL\tTIPO\tLEXEMA")
            for t in tokens:
                print(t)
        if args.ast:
            if args.tokens:
                print()
            print(dump(parse(tokens)))
    except (LexError, ParseError) as e:
        print(f"erro: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
