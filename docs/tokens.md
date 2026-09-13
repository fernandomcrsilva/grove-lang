# Tabela de tokens

Saída da análise léxica: cada token tem **tipo**, **lexema**, **linha** e **coluna**. `NUMBER` e `STRING` carregam também o **valor** (inteiro / texto sem aspas).

## Palavras reservadas (cheats de GTA San Andreas)

| Lexema | Token | Papel | O que faz no jogo | Por que virou isso |
|---|---|---|---|---|
| `HESOYAM` | `VAR` | declara variável | vida e colete cheios + $250.000 | o cheat que "dá" recursos: aqui dá um valor à variável |
| `TURNUPTHEHEAT` | `IF` | condicional | +2 estrelas de procurado | a polícia vem checar: "e se?" |
| `BRINGITON` | `ELIF` | senão se | 6 estrelas de procurado | sobe ainda mais o calor: outra condição |
| `TURNDOWNTHEHEAT` | `ELSE` | senão | zera o nível de procurado | par do de cima: senão, esfria |
| `KANGAROO` | `WHILE` | laço | pulo gigante | pula de novo, de novo, de novo |
| `GOODBYECRUELWORLD` | `BREAK` | sai do laço | CJ morre na hora | adeus, laço |
| `HELLOLADIES` | `PRINT` | imprime | sex appeal no máximo | todo programa começa com "Hello, World" |
| `FULLCLIP` | `TRUE` | verdadeiro | munição infinita | pente cheio |
| `GHOSTTOWN` | `FALSE` | falso | ruas vazias, sem carros e pedestres | cidade vazia, nada |

Todos são os códigos da versão de PC; no PS2 cada um corresponde a uma sequência de botões.

## Botões do controle (estrutura)

| Lexema | Alias ASCII | Token | Papel |
|---|---|---|---|
| `△` | `{` | `LBRACE` | abre bloco |
| `○` | `}` | `RBRACE` | fecha bloco |
| `×` | `;` | `SEMI` | fim de instrução (confirmar) |
| `□` | `!` | `NOT` | negação lógica |
| `L1` | `LPAREN` | abre parênteses |
| `R1` | `RPAREN` | fecha parênteses |
| `L2` | `AND` | e lógico |
| `R2` | `OR` | ou lógico |

`△ ○ × □` são os caracteres Unicode U+25B3, U+25CB, U+00D7, U+25A1; os aliases ASCII produzem o mesmo token e podem ser misturados. `L1 R1 L2 R2` são escritos como palavras e por isso não podem ser usados como nome de variável.

## Operadores

| Lexema | Token |
|---|---|
| `=` | `ASSIGN` |
| `==` `!=` | `EQ` `NE` |
| `<` `>` `<=` `>=` | `LT` `GT` `LE` `GE` |
| `+` `-` `*` `/` `%` | `PLUS` `MINUS` `STAR` `SLASH` `MOD` |

## Literais e outros

| Padrão | Token | Exemplo |
|---|---|---|
| `[0-9]+` | `NUMBER` | `250000` |
| `"..."` (uma linha, sem escape) | `STRING` | `"Grove Street"` |
| `[A-Za-z_][A-Za-z0-9_]*` que não é reservada | `IDENT` | `estrelas` |
| `#` até o fim da linha | ignorado | `# comentário` |
| espaços, tabs, quebras de linha | ignorado | |
| fim do arquivo | `EOF` | |

## Erros léxicos

Qualquer caractere fora das classes acima gera `LexError` com linha e coluna, por exemplo:

```
erro: linha 1, coluna 13: caractere inesperado '$'
```

String sem `"` de fechamento na mesma linha também é erro.

## Exemplo

Entrada:

```
HESOYAM n = 5 ×
```

Saída de `python -m grove arquivo.cj --tokens`:

```
LINHA:COL	TIPO	LEXEMA
1:1	VAR	HESOYAM
1:9	IDENT	n
1:11	ASSIGN	=
1:13	NUMBER	5
1:15	SEMI	×
1:16	EOF	
```
