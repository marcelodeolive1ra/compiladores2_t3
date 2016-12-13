grammar t3_cc2;

CADEIA:
    '"' ~('\n' | '\r' | '"')* '"';

COMENTARIO:
    '//' ~('/' | '\n')* '\n' -> skip;

ESPACO:
    (' ' | '\t' | '\r' | '\n') -> skip;

site:
	'site' titulo_site '{' menu sidebar banner conteudo rodape '}';

titulo_site:
    '(' CADEIA ')';

titulo:
	'titulo' '(' CADEIA ')';

menu:
	'menu' '{' item '}';

item:
	'item' '(' CADEIA ')' link? mais_itens;

link:
    '->' CADEIA;

mais_itens:
	item | ;

sidebar:
	'sidebar' '{' item '}' | 'sidebar' '=' 'menu' | ;

banner:
	'banner' '{' imagem	titulo subtitulo '}' | ;

subtitulo:
	'subtitulo' '(' CADEIA ')';

rodape:
	'rodape' '{' titulo subtitulo '}' | ;

conteudo:
	'conteudo' '{' secao mais_secoes '}' | ;

secao:
	'secao' '{' colunas '}';

mais_secoes:
    secao | ;

colunas:
    'colunas' '{' coluna mais_colunas '}' | coluna |;

coluna:
    'coluna' '{' (imagem | titulo subtitulo texto) '}';

mais_colunas:
    coluna | ;

texto:
	'texto' '(' CADEIA ')' | ;

imagem:
	'imagem' '(' CADEIA ')' link;