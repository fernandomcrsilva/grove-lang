"""Uso: python -m grove arquivo.cj [--tokens] [--ast]

Sem flags executa o programa. Com --tokens e/ou --ast só mostra essas etapas.
Sai com código 1 em erro léxico, sintático ou de execução.
"""
import argparse
import sys

from . import LexError, ParseError, RuntimeError_, dump, parse, run, tokenize
from .sounds import play


def main(argv=None):
    ap = argparse.ArgumentParser(prog="grove", description=__doc__.splitlines()[0])
    ap.add_argument("arquivo")
    ap.add_argument("--tokens", action="store_true", help="imprime a tabela de tokens em vez de executar")
    ap.add_argument("--ast", action="store_true", help="imprime a AST em vez de executar")
    args = ap.parse_args(argv)

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
        if not (args.tokens or args.ast):
            run(parse(tokens))
    except (LexError, ParseError, RuntimeError_) as e:
        print(f"erro: {e}", file=sys.stderr)
        play({LexError: "lex_error", ParseError: "parse_error"}.get(type(e), "runtime_error"))
        return 1
    play("passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
