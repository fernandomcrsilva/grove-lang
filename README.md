# Grove

Linguagem de programação em que as palavras-chave são os cheats de **GTA San Andreas** e a estrutura são os **botões do PlayStation 2**. Projeto da disciplina de Compiladores.

```
# fatorial de 5
HESOYAM n = 5 ×
HESOYAM r = 1 ×
KANGAROO L1 n > 1 R1 △
    r = r * n ×
    n = n - 1 ×
○
HELLOLADIES r ×
```

| Você escreve | Significa | O cheat no jogo |
|---|---|---|
| `HESOYAM x = 1 ×` | declara `x` | vida e colete cheios + $250.000 |
| `TURNUPTHEHEAT L1 cond R1 △ … ○` | if | +2 estrelas de procurado |
| `BRINGITON L1 cond R1 △ … ○` | else if | 6 estrelas de procurado |
| `TURNDOWNTHEHEAT △ … ○` | else | zera o nível de procurado |
| `KANGAROO L1 cond R1 △ … ○` | while | pulo gigante |
| `GOODBYECRUELWORLD ×` | break | CJ morre na hora |
| `HELLOLADIES expr ×` | print | sex appeal no máximo |
| `FULLCLIP` | true | munição infinita |
| `GHOSTTOWN` | false | ruas vazias, sem carros e pedestres |
| `△` `○` `×` | `{` `}` `;` | botões triângulo, bola, xis |
| `□` | `not` | botão quadrado |
| `L1` `R1` `L2` `R2` | `(` `)` `and` `or` | gatilhos do controle |

Tabela completa em [docs/tokens.md](docs/tokens.md); gramática em [docs/gramatica.md](docs/gramatica.md); semântica em [docs/interpretador.md](docs/interpretador.md).

## Rodar

Só precisa de Python 3.10+. Nenhuma dependência.

```bash
python -m grove examples/fatorial.cj            # executa → 120
python -m grove examples/fatorial.cj --tokens   # só a tabela de tokens
python -m grove examples/fatorial.cj --ast      # só a AST
python -m unittest                              # testes
```

## Como digitar os botões

`△ ○ × □` são Unicode. Quem não quiser digitar pode usar os aliases ASCII `{ } ; !`, que geram os mesmos tokens:

```
HESOYAM n = 5;
KANGAROO L1 n > 1 R1 {
    n = n - 1;
}
```

No Linux com tecla Compose, `Compose` + `x` + `x` dá `×`. Ou copie de [examples/fatorial.cj](examples/fatorial.cj).

## Falas do jogo

Ao rodar, o Grove toca um clipe do jogo: "MISSION PASSED" quando dá certo, "WASTED" em erro léxico, Big Smoke ("follow the damn train, CJ!") em erro sintático, CJ ("Ah shit, here we go again") em erro de execução. Os `.wav` não vêm no repositório; veja [assets/README.md](assets/README.md) para os nomes. Sem arquivo, fica em silêncio.

## Estrutura

```
grove/tokens.py    tipos de token + tabelas cheat → token
grove/lexer.py     análise léxica  (texto → tokens)
grove/ast.py       nós da AST + impressão
grove/parser.py    análise sintática (tokens → AST), descida recursiva
grove/interpreter.py  back-end: executa a AST (tree-walking)
grove/sounds.py    toca assets/<evento>.wav ao compilar ou dar erro
grove/__main__.py  linha de comando
assets/            clipes .wav (não versionados)
docs/              entregáveis: tabela de tokens, gramática, semântica
examples/          programas de exemplo (.cj)
tests/             unittest
```
