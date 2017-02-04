// UNIVERSIDADE FEDERAL DE SÃO CARLOS
// Construção de Compiladores 2 - 2016/2
// Trabalho 3

// Marcelo de Oliveira da Silva

grammar t3_cc2;

// ----------------------------------------------
// REGRAS LÉXICAS
// ----------------------------------------------
CADEIA:
    '"' ~('\n' | '\r' | '"')* '"';

COMENTARIO:
    '#' ~('#' | '\n')* '\n' -> skip;

ESPACO:
    (' ' | '\t' | '\r' | '\n') -> skip;

ERRO: .;

// ----------------------------------------------
// REGRAS SINTÁTICAS
// ----------------------------------------------
site:
	'site' ('(' parametros ')')? '{' menu? sidebar? banner? conteudo rodape? '}' EOF;

titulo_site:
    'titulo' '=' CADEIA;

titulo:
	'titulo' ('(' parametros ')')? '(' CADEIA ')';

menu:
	'menu' '{' item mais_itens '}';

item:
	'item' '(' CADEIA ')' link?;

link:
    '->' nova_aba? CADEIA;

nova_aba:
    '+';

mais_itens:
	item mais_itens | ;

sidebar:
	'sidebar' '{' item mais_itens '}' | 'sidebar' '=' 'menu';

banner:
	'banner' ('(' parametros ')')?  '{' texto '}';

subtitulo:
	'subtitulo' ('(' parametros ')')? '(' CADEIA ')';

rodape:
	'rodape' '{' (texto | (texto? colunas) | (texto? coluna)) '}';

conteudo:
	'conteudo' '{' secao mais_secoes '}';

secao:
	'secao' '{' (texto | (texto? colunas) | (texto? coluna)) '}';

mais_secoes:
    secao mais_secoes | ;

colunas:
    'colunas' '{' coluna mais_colunas '}';

coluna:
    'coluna' ('(' parametros ')')? '{' (imagem | texto) '}';

mais_colunas:
    coluna mais_colunas | ;

texto:
    'texto' '{' conteudo_texto '}';

conteudo_texto:
    (titulo | subtitulo | paragrafo) mais_conteudo_texto;

mais_conteudo_texto:
    conteudo_texto mais_conteudo_texto | ;

paragrafo:
    'paragrafo' ('(' parametros ')')? '(' CADEIA ')' link?;

imagem:
	'imagem' ('(' parametros ')')? '(' CADEIA ')' link?;

// Embora diversas regras façam uso do regra parametros, nem todos os parâmetros podem ser utilizados para todas as
// regras, bem como a quantidade de parâmetros em cada regra é limitada.
// A validação do correto uso dos parâmetros é feita no Analisador Semântico
parametros:
    (tamanho | fonte | cor | fundo | alinhamento | titulo_site) mais_parametros;

mais_parametros:
    ',' parametros | ;

tamanho:
    'tamanho' '=' opcao_tamanho;

opcao_tamanho:
    'extra-pequeno' | 'pequeno' | 'medio' | 'grande' | 'extra-grande';

fonte:
    'fonte' '=' opcao_fonte;

opcao_fonte:
    'Arial' | 'Helvetica' | 'Times New Roman' | 'Lato' | 'Roboto' | 'Open Sans';

cor:
    'cor' '=' opcao_cor;

opcao_cor:
    'azul' | 'verde' | 'amarelo' | 'branco' | 'preto' | 'vermelho' | 'laranja' | 'roxo' | 'rosa' | 'cinza' | 'marrom' |
    'azul-claro';

fundo:
    'fundo' '=' (cor | imagem);

alinhamento:
    'alinhamento' '=' opcao_alinhamento;

opcao_alinhamento:
    'centralizado' | 'esquerda' | 'direita';
