# Tabela de tokens

Saída da análise léxica: cada token tem **tipo**, **lexema**, **linha** e **coluna**. `NUMBER` e `STRING` carregam também o **valor** (inteiro / texto sem aspas).

## Palavras reservadas (cheats de GTA San Andreas)

| Lexema | Token | Papel | Referência ao jogo |
|---|---|---|---|
| `HESOYAM` | `VAR` | declara variável | vida, colete e $250.000: o cheat que "dá" recursos |
| `AEZAKMI` | `IF` | condicional | nunca procurado: a condição que muda o jogo |
| `ASNAEB` | `ELSE` | senão | limpa o nível de procurado: o outro caminho |
| `BAGUVIX` | `WHILE` | laço | vida infinita: o laço não morre |
| `CPKTNWT` | `BREAK` | sai do laço | explode todos os carros: para tudo |
| `CJPHONEHOME` | `PRINT` | imprime | "phone home": manda pra fora |
| `FULLCLIP` | `TRUE` | verdadeiro | munição infinita: cheio |
| `GHOSTTOWN` | `FALSE` | falso | cidade fantasma: vazio |

## Botões do controle (estrutura)

| Lexema | Token | Papel |
|---|---|---|
| `△` | `LBRACE` | abre bloco |
| `○` | `RBRACE` | fecha bloco |
| `×` | `SEMI` | fim de instrução (confirmar) |
| `□` | `NOT` | negação lógica |
| `L1` | `LPAREN` | abre parênteses |
| `R1` | `RPAREN` | fecha parênteses |
| `L2` | `AND` | e lógico |
| `R2` | `OR` | ou lógico |

`△ ○ × □` são os caracteres Unicode U+25B3, U+25CB, U+00D7, U+25A1. `L1 R1 L2 R2` são escritos como palavras e por isso não podem ser usados como nome de variável.

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
