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
	'menu' '{' item mais_itens '}';

item:
	'item' '(' CADEIA ')' link?;

link:
    '->' nova_aba? CADEIA;

nova_aba:
    '+';

mais_itens:
	(item)* | ;

sidebar:
	'sidebar' '{' item mais_itens '}' | 'sidebar' '=' 'menu' | ;

banner:
	'banner' '{' imagem	texto '}' | ;

subtitulo:
	'subtitulo' '(' CADEIA ')';

rodape:
	'rodape' '{' texto '}' | ;

conteudo:
	'conteudo' '{' secao mais_secoes '}' | ;

secao:
	'secao' '{' colunas '}';

mais_secoes:
    secao | ;

colunas:
    'colunas' '{' coluna mais_colunas '}' | coluna |;

coluna:
    'coluna' '{' (imagem | texto) '}';

mais_colunas:
    coluna | ;

texto:
    'texto' '{' conteudo_texto mais_conteudo_texto '}';

conteudo_texto:
    (titulo | subtitulo | paragrafo) mais_conteudo_texto;

mais_conteudo_texto:
    conteudo_texto | ;

paragrafo:
    'paragrafo' '(' CADEIA ')';

imagem:
	'imagem' '(' CADEIA ')' link;