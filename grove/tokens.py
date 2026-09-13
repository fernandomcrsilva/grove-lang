"""Tabela de tokens da linguagem Grove.

Keywords são cheats de GTA San Andreas (PS2); a estrutura usa os botões do controle.
"""
from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
    # cheats
    VAR = auto()      # HESOYAM
    IF = auto()       # AEZAKMI
    ELSE = auto()     # ASNAEB
    WHILE = auto()    # BAGUVIX
    BREAK = auto()    # GOODBYECRUELWORLD
    PRINT = auto()    # HELLOLADIES
    TRUE = auto()     # FULLCLIP
    FALSE = auto()    # GHOSTTOWN
    # botões
    LBRACE = auto()   # △
    RBRACE = auto()   # ○
    SEMI = auto()     # ×
    NOT = auto()      # □
    LPAREN = auto()   # L1
    RPAREN = auto()   # R1
    AND = auto()      # L2
    OR = auto()       # R2
    # operadores
    ASSIGN = auto()   # =
    EQ = auto()       # ==
    NE = auto()       # !=
    LT = auto()       # <
    GT = auto()       # >
    LE = auto()       # <=
    GE = auto()       # >=
    PLUS = auto()     # +
    MINUS = auto()    # -
    STAR = auto()     # *
    SLASH = auto()    # /
    MOD = auto()      # %
    # literais e fim
    NUMBER = auto()
    STRING = auto()
    IDENT = auto()
    EOF = auto()


# palavras reservadas: cheats + botões escritos como palavra (L1, R1, L2, R2)
WORDS = {
    "HESOYAM": TokenType.VAR,
    "AEZAKMI": TokenType.IF,
    "ASNAEB": TokenType.ELSE,
    "BAGUVIX": TokenType.WHILE,
    "GOODBYECRUELWORLD": TokenType.BREAK,
    "HELLOLADIES": TokenType.PRINT,
    "FULLCLIP": TokenType.TRUE,
    "GHOSTTOWN": TokenType.FALSE,
    "L1": TokenType.LPAREN,
    "R1": TokenType.RPAREN,
    "L2": TokenType.AND,
    "R2": TokenType.OR,
}

# botões de um caractere, com alias ASCII para quem não quer digitar Unicode
BUTTONS = {
    "△": TokenType.LBRACE, "{": TokenType.LBRACE,
    "○": TokenType.RBRACE, "}": TokenType.RBRACE,
    "×": TokenType.SEMI,   ";": TokenType.SEMI,
    "□": TokenType.NOT,    "!": TokenType.NOT,
}

# operadores: os de dois caracteres precisam ser testados antes dos de um
OPERATORS = {
    "==": TokenType.EQ,
    "!=": TokenType.NE,
    "<=": TokenType.LE,
    ">=": TokenType.GE,
    "=": TokenType.ASSIGN,
    "<": TokenType.LT,
    ">": TokenType.GT,
    "+": TokenType.PLUS,
    "-": TokenType.MINUS,
    "*": TokenType.STAR,
    "/": TokenType.SLASH,
    "%": TokenType.MOD,
}


@dataclass(frozen=True)
class Token:
    type: TokenType
    lexeme: str
    line: int
    col: int
    value: object = None  # int para NUMBER, str sem aspas para STRING

    def __str__(self):
        return f"{self.line}:{self.col}\t{self.type.name}\t{self.lexeme}"
