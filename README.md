# Grove

Linguagem de programação em que as palavras-chave são os cheats de **GTA San Andreas** e a estrutura são os **botões do PlayStation 2**. Projeto da disciplina de Compiladores.

```
# fatorial de 5
HESOYAM n = 5 ×
HESOYAM r = 1 ×
BAGUVIX L1 n > 1 R1 △
    r = r * n ×
    n = n - 1 ×
○
CJPHONEHOME r ×
```

| Você escreve | Significa |
|---|---|
| `HESOYAM x = 1 ×` | declara `x` |
| `AEZAKMI L1 cond R1 △ … ○ ASNAEB △ … ○` | if / else |
| `BAGUVIX L1 cond R1 △ … ○` | while |
| `CPKTNWT ×` | break |
| `CJPHONEHOME expr ×` | print |
| `FULLCLIP` / `GHOSTTOWN` | true / false |
| `△` `○` `×` | `{` `}` `;` |
| `L1` `R1` `L2` `R2` `□` | `(` `)` `and` `or` `not` |

Tabela completa em [docs/tokens.md](docs/tokens.md); gramática em [docs/gramatica.md](docs/gramatica.md).

## Rodar

Só precisa de Python 3.10+. Nenhuma dependência.

```bash
python -m grove examples/fatorial.cj            # tokens + AST
python -m grove examples/fatorial.cj --tokens   # só a tabela de tokens
python -m grove examples/fatorial.cj --ast      # só a AST
python -m unittest                              # testes
```

## Como digitar os botões

`△ ○ × □` são Unicode. Quem não quiser digitar pode usar os aliases ASCII `{ } ; !`, que geram os mesmos tokens:

```
HESOYAM n = 5;
BAGUVIX L1 n > 1 R1 {
    n = n - 1;
}
```

No Linux com tecla Compose, `Compose` + `x` + `x` dá `×`. Ou copie de [examples/fatorial.cj](examples/fatorial.cj).

## Estrutura

```
grove/tokens.py    tipos de token + tabelas cheat → token
grove/lexer.py     análise léxica  (texto → tokens)
grove/ast.py       nós da AST + impressão
grove/parser.py    análise sintática (tokens → AST), descida recursiva
grove/__main__.py  linha de comando
docs/              entregáveis: tabela de tokens, gramática
examples/          programas de exemplo (.cj)
tests/             unittest
```

## Estado

- [x] Análise léxica e tabela de tokens
- [x] Análise sintática e AST
- [ ] Back-end (interpretador)
- [ ] Pitch

## Equipe

4 pessoas. Sugestão de divisão: léxico + tabela de tokens, sintático + AST, back-end, documentação + pitch.
