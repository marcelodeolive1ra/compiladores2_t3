# Construção de Compiladores 2 - Trabalho 3

**UNIVERSIDADE FEDERAL DE SÃO CARLOS**<br>
Centro de Ciências Exatas e de Tecnologia<br>
Departamento de Computação<br>
Construço de Compiladores 2 - Semestre 2016/2<br>
Prof.ª Dr.ª Helena Caseli e Prof. Dr. Daniel Lucrédio

## Descrição do trabalho

O terceiro e último trabalho prático da disciplina consiste na implementação de um compilador completo para a linguagem especificada no Trabalho 2. O compilador deve, portanto, possui analisador léxico e sintático, analisador semântico e realizar geração de código ou interpretação.

## Descrição da linguagem

A ideia de linguagem deste trabalho foi criar uma linguagem de criação simplificada de websites. Nesta linguagem:

- Os sites criados são automaticamente responsivos
- O código é mais simples que o HTML (e pelos testes, cerca de metade do tamanho)
- Os componentes da linguagem são semanticamente nomeados em português
- O código gerado após a compilação é um site completo com HTML, CSS e eventualmente JavaScript, que ainda permite customizações posteriores
- O código gerado é baseado no framework responsivo Semantic UI

## Sintaxe da linguagem

O arquivo `t3_cc2.g4` do projeto possui a gramática da linguagem com sua sintaxe. Para um exemplo de uso da linguagem, que faz uso de todos os componentes definidos na gramática, verifique o caso de teste `ct_gerador_20.txt` em `casos_de_teste/entrada/geracao-codigo` e o resultado de sua sua compilação em `casos_de_teste/saida/geracao-codigo/ct_gerador_20.html`.

## Instruções de uso do compilador

###Preparando o ambiente

O compilador desenvolvido neste trabalho foi escrito em Python 3 com auxílio do gerador ANTLR, versão 4.6. Para executá-lo, é necessário, além do Python 3 instalado, a instalação da biblioteca `antlr4` no ambiente de execução do Python. 

Caso tenha o pip instalado no computador, basta executar:

```$ pip3 install antlr4-python3-runtime```

Caso não tenha o `pip` instalado no computador, instruções de instalação podem ser encontradas em: [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/). 

###Compilando arquivos

Como Python é uma linguagem interpretada, não há necessidade de compilar o projeto previamente. Basta executá-lo. O programa principal é o arquivo `Main.py`, e este programa aceita alguns parâmetros:

```Main.py [-h] [-t TESTES] [-e ENTRADA] [-s SAIDA]```

O parâmetro `-h` mostra instruções resumidas de uso do compilador. O parâmetro `-t` é utilizado para rodar os casos de teste, que serão detalhados a seguir. Para compilar um arquivo, os parâmetros `-e` e `-s` são os que importam.

`-e` serve para especificar o caminho do arquivo de entrada para o compilador

`-s` serve para especificar o caminho do arquivo de saída, que será gerado se o programa fonte estiver livre de erros léxicos, sintáticos ou semânticos. Para já ficar pronto para uso, este arquivo deve ter extensão `.html`.

Assim, um exemplo de compilação seria (assumindo que o usuário já esteja no mesmo diretório do compilador):

```$ python3 ./Main.py -e ~/Desktop/programa1.txt -s ~/Desktop/programa1.html```

***Importante observar que, caso o programa fonte inclua referências para imagens, estas imagens devem ser colocadas no mesmo diretório do arquivo de saída do compilador.***

Se ocorrerem erros durante a compilação, a compilação é interrompida e o usuário recebe uma mensagem especificando tais erros.

Pode acontecer também do arquivo conter warnings (mais detalhes na seção Análise semântica do relatório). Neste caso, o compilador informará e fará sugestões, mas a compilação não será interrompida.

###Executando os casos de teste

Para o desenvolvimento deste compilador, foram escritos 118 casos de teste, sendo 44 casos para a análise léxica e sintática, 54 para a análise semântica e 20 para o gerador de código. Os casos de teste estão em `casos_de_teste/entrada/` (em relação ao diretório do projeto). Cada caso de teste tem um comentário nas linhas iniciais indicando o que está sendo testado do compilador.

É possível executar cada tipo de teste (sintático, semântico ou gerador de código) separadamente ou todos em conjunto, utilizando o parâmetro `-t` do programa `Main.py`:

```
$ python3 ./Main.py -t sintatico
$ python3 ./Main.py -t semantico
$ python3 ./Main.py -t gerador
$ python3 ./Main.py -t todos
```

Todos os casos de teste sintáticos e semânticos devem reportar erro e todos os casos de teste do gerador devem gerar arquivos de saída em `casos_de_teste/saida/gerador/`. Este diretório já contém as imagens que são utilizadas nos casos de teste.


## Análise semântica

O compilador foi desenvolvido para identificar os seguintes erros semânticos:

- Uso da regra `sidebar=menu` sem a declaração de um `menu`.
- Verificação da consistência de parâmetros nas regras que suportam parâmetros, sendo as seguintes opções possíveis:
  - `site(titulo, alinhamento)`
  - `banner(fundo)`, onde quando `fundo=imagem()`, a imagem utilizada não pode ter parâmetros de imagem e também não pode ter links
  - `coluna(alinhamento)`
  - `imagem(alinhamento, tamanho)`
  - `titulo(alinhamento, cor)`
  - `subtitulo(alinhamento, cor)`
  - `paragrafo(alinhamento, cor)`
- Os parâmetros são sempre opcionais, e se forem utilizados, não é necessário utilizar todos os parâmetros permitidos para o componente. O compilador verifica também a existência de mais parâmetros que o permitido para o componente e reporta erro nesta situação. Interessante notar que a ordem dos parâmetros não importa. O compilador entenderá corretamente, por exemplo, tanto `imagem(tamanho, alinhamento)` quanto `imagem(alinhamento, tamanho)`.
- Verificação de parâmetros repetidos. Por exemplo, `titulo(cor=azul, cor=verde)` acusaria erro semântico.

Como um extra, o analisador semântico faz também a verificação de dois pontos que não impedem a geração de código, mas que são interessantes de serem notificados ao programador. Durante a compilação, eles serão acusados como ***warnings***:

- Uso do componente `colunas` com apenas uma coluna dentro. Neste caso, o programador poderia utilizar apenas `coluna` diretamente, evitando um aninhamento desnecessário de elementos no código gerado.
- Verificação se o tamanho da imagem utilizado cabe dentro da coluna em que a imagem foi declarada. Por exemplo, se foi utilizado `tamanho=grande` em uma imagem que está dentro de um grupo de três colunas, cada coluna terá 1/3 de tamanho e, com isso, uma imagem de tamanho grande não caberia e seria redimensionada. A mesma verificação acontece para todos os outros tamanhos.


##Geração de código

O código gerado pelo compilador, caso o arquivo de entrada não tenha erros, é baseado em HTML5 com CSS3 e, quando utilizado o componente `sidebar`, trechos de JavaScript.
Foi utilizado também o framework responsivo Semantic UI versão 2.2.6 ([http://semantic-ui.com](http://semantic-ui.com)) para auxílio na geração de código.
Como os parâmetros dos componentes que os permitem são opcionais, a omissão de parâmetros faz com que o gerador de código adote os seguintes valores padrões:

- `site(titulo_site="", fonte=Lato)`
- `banner(fundo=cor=preto)`
- `coluna(alinhamento=centralizado)`
- `imagem(tamanho=medio, alinhamento=centralizado)`
- `titulo(alinhamento=esquerda, cor=preto)`
- `subtitulo(alinhamento=esquerda, cor=preto)`
- `paragrafo(alinhamento=esquerda, cor=preto)`
