grammar t3_cc2;

CADEIA:
    '"' ~('\n' | '\r' | '"')* '"';

COMENTARIO:
    '#' ~('#' | '\n')* '\n' -> skip;

ESPACO:
    (' ' | '\t' | '\r' | '\n') -> skip;

site:
	'site' titulo_site '{' menu sidebar banner conteudo rodape '}';

titulo_site:
    '(' CADEIA ')';

titulo:
	'titulo' ('(' parametro ')')? '(' CADEIA ')';

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
	'sidebar' '{' item mais_itens '}' | 'sidebar' '=' 'menu' | ;

banner:
	'banner' '{' imagem texto '}' | ;

subtitulo:
	'subtitulo' ('(' parametro ')')? '(' CADEIA ')';

rodape:
	'rodape' '{' texto '}' | ;

conteudo:
	'conteudo' '{' secao mais_secoes '}' | ;

secao:
	'secao' '{' (colunas | coluna) '}';

mais_secoes:
    secao mais_secoes | ;

colunas:
    'colunas' '{' coluna mais_colunas '}' | ;

coluna:
    'coluna' ('(' alinhamento ')')? '{' (imagem | texto) '}';

mais_colunas:
    coluna mais_colunas | ;

texto:
    'texto' ('(' parametro ')')? '{' conteudo_texto '}';

conteudo_texto:
    (titulo | subtitulo | paragrafo) mais_conteudo_texto;

mais_conteudo_texto:
    conteudo_texto mais_conteudo_texto | ;

paragrafo:
    'paragrafo' ('(' parametro ')')? '(' CADEIA ')';

imagem:
	'imagem' '(' CADEIA (',' tamanho)? ')' link | ;

parametro:
    (tamanho | fonte | cor) mais_parametros;

mais_parametros:
    ',' parametro | ;

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
    'azul' | 'verde' | 'amarelo' | 'branco' | 'preto' | 'vermelho' | 'laranja' | 'roxo';

alinhamento:
    'alinhamento' '=' opcao_alinhamento;

opcao_alinhamento:
    'centralizado' | 'esquerda' | 'direita';
